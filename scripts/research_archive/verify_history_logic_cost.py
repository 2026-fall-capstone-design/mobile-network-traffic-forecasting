"""모델 없이 61번의 저장 Bayes MAE·구조적 비용·원장 변화를 검수한다."""

from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import json
import math
from datetime import UTC, datetime
from fractions import Fraction
from pathlib import Path


def integrated_risk(probability: Fraction, noise: Fraction) -> Fraction:
    """간격 1인 두 Uniform 구간의 중앙값에서 절대 오차를 정확히 적분한다."""
    if not Fraction(1, 2) <= probability <= 1 or not 0 < noise < Fraction(1, 2):
        raise ValueError("분리된 두 구간과 높은 쪽의 확률이라는 가정이 필요함")
    median = -noise + noise / probability
    within = ((median + noise) ** 2 + (noise - median) ** 2) / (4 * noise)
    other = 1 - median
    return probability * within + (1 - probability) * other


def fraction_value(value: Fraction) -> dict:
    """정확 분수와 표시용 소수를 함께 보존한다."""
    return {"fraction": str(value), "decimal": float(value)}


def verify(manifest_path: Path) -> dict:
    """보존 원문을 읽고 별도 적분·행렬 수·전체 원장 차이와 대조한다."""
    manifest_path = manifest_path.resolve()
    archive_root = manifest_path.parents[2]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    checks, errors = [], []

    def check(name: str, condition: bool) -> None:
        """검사 결과를 기록하며 의미 검수나 모델 재현을 대신하지 않는다."""
        checks.append(name)
        if not condition:
            errors.append(name)

    def exact(name: str, value: Fraction, recorded: dict) -> None:
        """저장 분수와 표시용 소수를 모두 대조한다."""
        check(name + ":fraction", Fraction(recorded["fraction"]) == value)
        check(
            name + ":decimal",
            math.isclose(recorded["decimal"], float(value), rel_tol=1e-12, abs_tol=1e-15),
        )

    paths = {}
    for row in manifest["sources"]:
        path = (manifest_path.parent / row["archive_path"]).resolve()
        if not path.is_relative_to(archive_root):
            raise ValueError("보존 경로가 연구 아카이브 밖을 가리킴")
        raw = path.read_bytes()
        check(
            row["source_id"] + ":bytes",
            len(raw) == row["size_bytes"] and hashlib.sha256(raw).hexdigest() == row["sha256"],
        )
        paths[row["source_id"]] = path

    def data(sid: str) -> dict:
        """JSON만 해석하고 보존한 Python 코드는 import하지 않는다."""
        return json.loads(paths[sid].read_text(encoding="utf-8"))

    saved, started, finished = (data(sid) for sid in ["SRC-0027870", "SRC-0027872", "SRC-0027871"])
    before, after = data("SRC-0027869"), data("SRC-0000901")
    identities = {
        key: hashlib.sha256(paths[sid].read_bytes()).hexdigest()
        for key, sid in [
            ("plan", "SRC-0021961"),
            ("code", "SRC-0022880"),
            ("rctl_structure", "SRC-0023048"),
        ]
    }
    check("recorded_identities", identities == saved["sha256"] == started["sha256"])
    code = ast.parse(paths["SRC-0022880"].read_text(encoding="utf-8"))
    imports = {
        alias.name
        for node in ast.walk(code)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {node.module for node in ast.walk(code) if isinstance(node, ast.ImportFrom)}
    check(
        "original_arithmetic_imports",
        imports == {"pathlib", "fractions", "time", "json", "hashlib"},
    )
    check("noise_half_width", saved["toy"]["observation_noise_half_width"] == "1/20")
    noise = Fraction(1, 20)
    known = integrated_risk(Fraction(9, 10), noise)
    one = integrated_risk(Fraction(1, 2), noise)
    cases, two = [], Fraction(0)
    for previous in [0, 1]:
        for current in [0, 1]:
            persistence = [Fraction(9, 10), Fraction(1, 10)]
            joints = [Fraction(1, 4) * (p if previous == current else 1 - p) for p in persistence]
            event = sum(joints)
            next_one = (
                sum(
                    joint * (p if current == 1 else 1 - p)
                    for joint, p in zip(joints, persistence, strict=True)
                )
                / event
            )
            high = max(next_one, 1 - next_one)
            risk = integrated_risk(high, noise)
            check(
                f"state_pair:{previous}{current}",
                event == Fraction(1, 4)
                and high == Fraction(41, 50)
                and risk == Fraction(409, 2050),
            )
            two += event * risk
            cases.append(
                dict(
                    states=[previous, current],
                    event_probability=fraction_value(event),
                    posterior_cell0=fraction_value(joints[0] / event),
                    next_state1_probability=fraction_value(next_one),
                    risk=fraction_value(risk),
                )
            )
    risks = {
        "known_cell_any_length": known,
        "unknown_cell_length1": one,
        "unknown_cell_length2": two,
        "history_gain_pooled_minus_known": one - two,
    }
    for key, value in risks.items():
        exact(key, value, saved["toy"][key])
    check("strict_order", known < two < one)
    check("stored_label_is_not_pooled_minus_known", one - two != one - known)
    structure = saved["rctl_arithmetic"]
    check(
        "fixed_channels_and_lengths",
        structure["channels"] == 9 and set(structure["metrics"]) == {"2", "8"},
    )
    blocks = []
    for index, (a, c) in enumerate(
        zip([9, 16, 32, 64, 64, 32], [16, 32, 64, 64, 32, 16], strict=True), 1
    ):
        matrices = dict(
            conv1=3 * a * c,
            conv2=3 * c * c,
            shortcut1=a * c,
            shortcut2=a * c,
            lstm_input=4 * c * c,
            lstm_hidden=4 * c * c,
        )
        biases = dict(conv_and_shortcut=4 * c, lstm_input=4 * c, lstm_hidden_frozen=4 * c)
        blocks.append(
            dict(
                block=index,
                input_channels=a,
                output_channels=c,
                matrix_components=matrices,
                bias_components=biases,
                batchnorm_affine=4 * c,
                matrix_MAC_per_step=sum(matrices.values()),
                total_parameters=sum(matrices.values()) + sum(biases.values()) + 4 * c,
                frozen_parameters=4 * c,
            )
        )
    projections = sum(c * c for c in [16, 32, 64])
    projection_biases = sum([16, 32, 64])
    root_weight, root_bias = 9 * 16, 16
    per_step = sum(b["matrix_MAC_per_step"] for b in blocks) + projections + root_weight + 16
    fixed = (
        sum(b["total_parameters"] for b in blocks)
        + projections
        + projection_biases
        + root_weight
        + root_bias
    )
    frozen = sum(b["frozen_parameters"] for b in blocks)
    check("frozen_extra_recurrent_bias", frozen == 896)
    metrics = {}
    for length in [2, 8]:
        mac, parameters = length * per_step, fixed + 16 * length + 1
        check(
            "MAC:" + str(length), structure["metrics"][str(length)]["matrix_MAC_per_sample"] == mac
        )
        check(
            "parameters:" + str(length),
            structure["metrics"][str(length)]["parameters"] == parameters,
        )
        metrics[str(length)] = dict(
            matrix_MAC_per_sample=mac,
            parameters=parameters,
            trainable_parameters=parameters - frozen,
            frozen_parameters=frozen,
        )
    exact("MAC_ratio", Fraction(1, 4), structure["MAC_ratio_L2_L8"])
    exact("parameter_reduction", Fraction(96, 174433), structure["parameter_reduction_ratio"])
    check(
        "cost_exclusions",
        structure["exclusions"]
        == [
            "activations",
            "BatchNorm",
            "bias adds",
            "memory movement",
            "training/backprop",
            "actual runtime",
        ],
    )
    check(
        "historical_no_model_calls",
        all(structure[k] == 0 for k in ["RCTL_instantiations", "RCTL_forward_calls", "RCTL_fits"])
        and all(
            saved["cost"][k] == 0 for k in ["TabICL_contexts", "TabICL_query_rows", "RCTL_fits"]
        ),
    )
    duration = saved["cost"]["cheap_numeric_seconds"]
    check(
        "duration_and_finished",
        0 < duration < 5 and finished["seconds"] == duration and finished["hashes_unchanged"],
    )
    stage = "history_logic_cost_61"
    check("not_previously_accounted", stage not in before["new_cheap_diagnostic_seconds"])
    expected = copy.deepcopy(before)
    expected["new_cheap_diagnostic_seconds"][stage] = duration
    check("whole_ledger_transition", expected == after)
    check(
        "unchanged_model_budgets",
        after["used"] == before["used"]
        and after["remaining_count_budgets"] == before["remaining_count_budgets"]
        and after["used"]["TabICL_contexts"] == 65
        and after["used"]["TabICL_query_rows"] == 38016
        and after["used"]["RCTL_fits"] == 29,
    )
    cheap = sum(after["new_cheap_diagnostic_seconds"].values())
    total = cheap + sum(
        after["used"][k]
        for k in [
            "TabICL_fit_predict_seconds",
            "RCTL_wall_seconds",
            "RCTL_frozen_inference_seconds",
        ]
    )
    return dict(
        success=not errors,
        checked_at_utc=datetime.now(UTC).isoformat(),
        checks=len(checks),
        check_names=checks,
        errors=errors,
        risk_values={k: fraction_value(v) for k, v in risks.items()},
        two_observation_cases=cases,
        label_correction=dict(
            stored_field="history_gain_pooled_minus_known",
            actual_calculation="unknown_cell_length1 - unknown_cell_length2",
            actual_value=fraction_value(one - two),
            pooled1_minus_known=fraction_value(one - known),
            pooled2_minus_known=fraction_value(two - known),
            original_preserved=True,
        ),
        rctl_block_counts=blocks,
        projection_weights=projections,
        projection_biases=projection_biases,
        root_weights=root_weight,
        root_biases=root_bias,
        matrix_MAC_per_step=per_step,
        metrics=metrics,
        after61_cheap_seconds=cheap,
        after61_recorded_modeling_seconds=total,
        new_model_runs=0,
        original_scripts_executed=False,
        random_draws=0,
        independent_model_reproduction=False,
        scope=(
            "동일한 cell 혼합과 cell에 독립인 잠재 상태 정상분포를 명시한 "
            "정확 적분·구조적 행렬 수·원장 대조다. 당시 모델 실행이나 실제 지연을 재현하지 않았다. "
            "RCTL 구조는 보존된 특정 코드 버전의 정적 독해를 전제로 한다."
        ),
    )


def main() -> None:
    """검수 결과를 저장하고 불일치가 있으면 실패로 종료한다."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = verify(args.manifest)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({k: result[k] for k in ["success", "checks", "errors"]}))
    raise SystemExit(0 if result["success"] else 1)


if __name__ == "__main__":
    main()
