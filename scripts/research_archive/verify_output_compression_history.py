"""74번의 저장 배열·원장·출력공간을 모델 실행 없이 검수한다."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from datetime import UTC, datetime
from fractions import Fraction
from itertools import combinations
from pathlib import Path

import numpy as np


def verify(manifest_path: Path) -> dict:
    """정확사본 해시 확인 뒤 작은 저장 배열과 선택 원자료만 재계산한다."""
    manifest_path = manifest_path.resolve()
    folder = manifest_path.parent
    archive_root = manifest_path.parents[2]
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    checks = []
    paths = {}

    def check(name, condition):
        if not condition:
            raise ValueError(name)
        checks.append(name)

    def close(name, actual, expected):
        check(name, np.allclose(actual, expected, rtol=1e-10, atol=1e-12))

    for row in manifest["sources"]:
        saved = (folder / row["archive_path"]).resolve()
        check(row["source_id"] + " path within archive", saved.is_relative_to(archive_root))
        raw = saved.read_bytes()
        check(
            row["source_id"] + " exact bytes",
            len(raw) == row["size_bytes"] and hashlib.sha256(raw).hexdigest() == row["sha256"],
        )
        for sid in row["exact_alias_source_ids"]:
            paths[sid] = saved

    def source(sid):
        return paths[sid]

    with np.load(source("SRC-0029270"), allow_pickle=False) as n:
        a = {k: n[k] for k in n.files}
    check(
        "39 numeric arrays",
        len(a) == 39 and all(v.dtype.kind in "iuf" and np.isfinite(v).all() for v in a.values()),
    )
    check(
        "partial and final share registered exact copy",
        source("SRC-0029271").read_bytes() == source("SRC-0029270").read_bytes(),
    )
    r = json.loads(source("SRC-0029276").read_bytes())
    s = json.loads(source("SRC-0029279").read_bytes())
    check("result settings equal saved settings", r["settings"] == s)
    check(
        "known cell order",
        s["cell_ids"] == [3737, 3765, 6137, 6165] and np.array_equal(a["cell_ids"], s["cell_ids"]),
    )
    for k in ["context_times", "query_times", "train_times"]:
        check(k + " saved array matches settings", np.array_equal(a[k], s[k]))
    check(
        "context exact predeclared grid",
        np.array_equal(a["context_times"], np.rint(np.linspace(168, 671, 256)).astype(int)),
    )
    check(
        "query and train boundaries",
        np.array_equal(a["query_times"], np.arange(672, 1008))
        and np.array_equal(a["train_times"], np.arange(168, 840)),
    )
    check(
        "original run counts",
        s["contexts"] == 4
        and s["query_rows"] == 1344
        and s["simple_fits"] == 26
        and s["RCTL_fits"] == 0
        and s["Tab_output"] == "mean"
        and not s["independent_test"],
    )
    check("actual target shape", a["actual"].shape == (336, 4))
    y = a["actual"][168:]
    mu = a["center"]
    yc = a["actual"][:168] - mu

    def metric_values(prediction, target):
        sq = np.square(prediction - target)
        return dict(
            MSE=float(np.mean(sq)),
            MAE=float(np.mean(np.abs(prediction - target))),
            half_MSE=[float(np.mean(sq[:84])), float(np.mean(sq[84:]))],
            daily_MSE=[float(np.mean(sq[d * 24 : (d + 1) * 24])) for d in range(7)],
            cell_MSE=np.mean(sq, axis=0).tolist(),
            negative_predictions=int(np.count_nonzero(prediction < 0)),
            clipped_MSE=float(np.mean(np.square(np.clip(prediction, 0, None) - target))),
        )

    metric_groups = 0

    def compare_metrics(name, prediction, saved):
        nonlocal metric_groups
        actual = metric_values(prediction, y)
        check(name + " complete metric schema", set(actual) == set(saved))
        for key, value in actual.items():
            close(name + " " + key, value, saved[key])
        metric_groups += 1

    for name, saved in r["teacher"].items():
        compare_metrics("teacher " + name, a["teacher_" + name][168:], saved)
    compare_metrics(
        "HGB uncompressed", a["HGB_full_actual_targets"], r["actual_target_HGB_reference"]
    )
    for name, saved in r["actual_target_HGB_latent"].items():
        compare_metrics("HGB latent " + name, a["HGB_latent_" + name], saved)
    for name, choice in r["choices"].items():
        u = a["U_" + name]
        sm = a["S_" + name]
        ug = a["U_global_" + name]
        check(name + " matrix shapes", u.shape == ug.shape == (4, 2) and sm.shape == (4, 4))
        close(name + " symmetric matrix", sm, sm.T)
        close(name + " local orthonormal columns", u.T @ u, np.eye(2))
        close(name + " global orthonormal columns", ug.T @ ug, np.eye(2))
        close(name + " eigenvalues", np.linalg.eigvalsh(sm), choice["eigenvalues"])
        close(name + " retained objective", np.trace(u.T @ sm @ u), choice["retained_score"])
        close(
            name + " global optimum",
            np.linalg.eigvalsh(sm)[-2:].sum(),
            choice["global_rank2_score"],
        )
        close(
            name + " global retained objective",
            np.trace(ug.T @ sm @ ug),
            choice["global_rank2_score"],
        )
        check(
            name + " seven distinct candidates",
            len(choice["candidate_scores"])
            == len({json.dumps(c["partition"]) for c in choice["candidate_scores"]})
            == 7,
        )
        for i, c in enumerate(choice["candidate_scores"]):
            close(
                name + f" candidate {i} retained score",
                sum(np.linalg.eigvalsh(sm[np.ix_(g, g)])[-1] for g in c["partition"]),
                c["score"],
            )
        winner = max(choice["candidate_scores"], key=lambda c: c["score"])
        check(name + " selected candidate", winner["partition"] == choice["partition_indices"])
        check(
            name + " partition IDs",
            [[int(a["cell_ids"][i]) for i in g] for g in choice["partition_indices"]]
            == choice["partition_cell_ids"],
        )
        close(
            name + " actual reconstruction diagnostic",
            np.mean(np.square((y - mu) - (y - mu) @ u @ u.T)),
            choice["actual_target_reconstruction_MSE_not_forecast"],
        )
        for teacher, saved in choice["projected_teacher"].items():
            compare_metrics(
                name + " projected " + teacher,
                mu + (a["teacher_" + teacher][168:] - mu) @ u @ u.T,
                saved,
            )
        pred = a["HGB_latent_" + name] - mu
        residual = y - mu
        close(name + " lifted prediction in retained span", pred, pred @ u @ u.T)
        close(
            name + " rowwise orthogonal SSE identity",
            np.sum((residual - pred) ** 2, axis=1),
            np.sum((residual - residual @ u @ u.T) ** 2, axis=1)
            + np.sum((residual @ u - pred @ u) ** 2, axis=1),
        )
        if name == "raw_calibration":
            close(name + " original moment from saved actual", sm, yc.T @ yc / 168)
        elif name != "raw_all":
            teacher = "TabICL" if name.startswith("Tab_") else name.split("_")[0]
            g = a["teacher_" + teacher][:168] - mu
            moment = (
                g.T @ g / 168 if name.endswith("_plugin") else (g.T @ yc + yc.T @ g - g.T @ g) / 168
            )
            close(name + " original moment from saved predictions", sm, moment)

    for scale, saved in r["toy"].items():
        alpha = Fraction(scale)
        for key, value in [
            ("plugin_signal", 4 * alpha**2),
            ("corrected_signal", 4 * (2 * alpha - alpha**2)),
            ("other_signal", Fraction(1)),
        ]:
            check(
                "toy " + scale + " " + key + " rational", Fraction(saved[key]["fraction"]) == value
            )
            close("toy " + scale + " " + key + " decimal", saved[key]["decimal"], float(value))
        check(
            "toy " + scale + " decisions",
            saved["plugin_correct"] == (4 * alpha**2 > 1)
            and saved["corrected_correct"] == (4 * (2 * alpha - alpha**2) > 1),
        )
    check(
        "no historical RCTL validation claimed",
        not r["RCTL_validated"]
        and not r["independent_test"]
        and r["cost"]["RCTL_fits"] == r["cost"]["RCTL_forward_calls"] == 0,
    )

    provenance = json.loads((folder / "selected-source-data-provenance.json").read_bytes())
    selected_path = folder / "selected-source-data.npz"
    check(
        "selected data preserved hash",
        hashlib.sha256(selected_path.read_bytes()).hexdigest()
        == provenance["selected_data_sha256"],
    )
    with np.load(selected_path, allow_pickle=False) as selected:
        raw_values = selected["raw_activity"]
        dates = selected["timestamps"]
        check(
            "selected original dimensions",
            raw_values.shape == (1008, 4)
            and dates.shape == (1008,)
            and np.array_equal(selected["cell_ids"], a["cell_ids"]),
        )
    scales = raw_values[:672].mean(axis=0)
    normalized = raw_values / scales
    center = normalized[a["context_times"]].mean(axis=0)
    close("HDF selected scale", scales, a["scales"])
    close("HDF selected center", center, mu)
    close("HDF selected target", normalized[a["query_times"]], a["actual"])
    train = normalized[a["train_times"]] - center
    close("HDF raw_all second moment", train.T @ train / len(train), a["S_raw_all"])
    for index, date in provenance["dates"].items():
        check("HDF date " + index, str(dates[int(index)]) == date)
    check(
        "HDF selection identity",
        provenance["source_sha256"] == s["hashes"]["data"]
        and provenance["time_range_inclusive"] == [0, 1007]
        and provenance["stored_cell_indices"] == [3736, 3764, 6136, 6164]
        and provenance["activity_channel_index"] == 2,
    )
    for item in provenance["identities"]:
        check(
            "original input identity " + item["role"], item["sha256"] == s["hashes"][item["role"]]
        )
    expected_partitions = sorted(
        [[0, *subset], [i for i in [1, 2, 3] if i not in subset]]
        for k in range(3)
        for subset in combinations([1, 2, 3], k)
    )
    for name, choice in r["choices"].items():
        check(
            name + " exhaustive ordered partitions",
            [x["partition"] for x in choice["candidate_scores"]] == expected_partitions,
        )
        check(
            name + " positive definite observed matrix", np.linalg.eigvalsh(a["S_" + name])[0] > 0
        )
        expected = (
            [[3737, 6165], [3765, 6137]]
            if name == "raw_calibration"
            else [[3737], [3765, 6137, 6165]]
        )
        check(name + " documented chosen membership", choice["partition_cell_ids"] == expected)
        u = a["U_" + name]
        for col, group in enumerate(choice["partition_indices"]):
            check(
                name + f" disjoint support {col}",
                np.allclose(u[[i for i in range(4) if i not in group], col], 0),
            )
        latent = r["actual_target_HGB_latent"][name]
        baseline = r["actual_target_HGB_reference"]
        check(
            name + " worse overall and halves",
            latent["MSE"] > baseline["MSE"]
            and np.all(np.array(latent["half_MSE"]) > baseline["half_MSE"]),
        )
        if name != "raw_calibration":
            close(
                name + " singleton cell equals baseline",
                latent["cell_MSE"][0],
                baseline["cell_MSE"][0],
            )
            check(
                name + " preserved day six benefit",
                latent["daily_MSE"][5] < baseline["daily_MSE"][5],
            )
    check(
        "calibration partition cell 6137 exception",
        r["actual_target_HGB_latent"]["raw_calibration"]["cell_MSE"][2]
        < r["actual_target_HGB_reference"]["cell_MSE"][2],
    )
    for simple in ["Ridge", "HGB"]:
        for field in ["MSE", "MAE", "half_MSE", "daily_MSE", "cell_MSE"]:
            check(
                "direct Tab advantage " + simple + " " + field,
                np.all(np.array(r["teacher"]["TabICL"][field]) < r["teacher"][simple][field]),
            )

    # Static AST only: these nn modules are never imported, constructed or called.
    tree = ast.parse(source("SRC-0023048").read_text(encoding="utf-8"))
    widths = next(
        ast.literal_eval(n.value)
        for n in ast.walk(tree)
        if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == "fs" for t in n.targets)
    )
    check("static six block widths", widths == [16, 32, 64, 64, 32, 16])
    assignments = {
        ast.unparse(t): ast.unparse(n.value)
        for n in ast.walk(tree)
        if isinstance(n, ast.Assign)
        for t in n.targets
        if isinstance(t, ast.Attribute)
    }
    expected_layers = {
        "self.c1": "CausalConv(inc, c, 3, dilation=dilation)",
        "self.c2": "CausalConv(c, c, 3, dilation=dilation)",
        "self.s1": "nn.Conv1d(inc, c, 1)",
        "self.s2": "nn.Conv1d(inc, c, 1)",
        "self.lstm": "nn.LSTM(c, c, batch_first=True)",
        "self.final_shortcut": "nn.Conv1d(channels, 16, 1)",
        "self.dense": "nn.Linear(steps * 16, 1)",
        "self.projections": "nn.ModuleList([nn.Conv1d(c, c, 1) for c in fs[:3]])",
    }
    for name, expression in expected_layers.items():
        check("static layer " + name, assignments[name] == expression)

    def mac(outputs):
        length, channels = 2, 24
        block_weights = sum(
            5 * i * o + 11 * o * o for i, o in zip([channels, *widths[:-1]], widths, strict=True)
        )
        return length * (
            block_weights + sum(v * v for v in widths[:3]) + 16 * channels + 16 * outputs
        )

    expected_mac = dict(
        four_scalar_calls=4 * mac(1),
        two_cluster_rank1_calls_plus_decoder=2 * mac(1) + 4,
        two_cluster_full_rank2_calls=mac(1) + mac(3),
        single_full_rank4_call=mac(4),
    )
    check(
        "all four hypothetical MAC totals",
        expected_mac == r["RCTL_arithmetic"]["same_information_L2_channels24"],
    )
    check(
        "RCTL arithmetic is not a runtime",
        r["RCTL_arithmetic"]["MAC_only_not_runtime"] and r["RCTL_arithmetic"]["RCTL_calls"] == 0,
    )

    before, after, update, calls, finished, started = [
        json.loads(source(sid).read_bytes())
        for sid in [
            "SRC-0029273",
            "SRC-0029272",
            "SRC-0029274",
            "SRC-0029275",
            "SRC-0029277",
            "SRC-0029278",
        ]
    ]
    cost = r["cost"]
    check(
        "run hashes and finish",
        started["hashes"] == s["hashes"]
        and finished["hashes_unchanged"]
        and finished["cost"] == cost,
    )
    for side, sid in [("before", "SRC-0029273"), ("after", "SRC-0029272")]:
        check(
            "budget hash " + side,
            hashlib.sha256(source(sid).read_bytes()).hexdigest() == update["sha256_" + side],
        )
    changed = {
        "model_calls_by_stage",
        "used",
        "remaining_count_budgets",
        "new_cheap_diagnostic_seconds",
        "cheap_stage_details",
    }
    check("same ledger fields", set(before) == set(after))
    for key in set(before) - changed:
        check("unchanged ledger " + key, before[key] == after[key])
    stage = "output_compression_74"
    check(
        "one appended model stage",
        after["model_calls_by_stage"][:-1] == before["model_calls_by_stage"]
        and all(x["stage"] != stage for x in before["model_calls_by_stage"])
        and after["model_calls_by_stage"][-1]
        == dict(
            stage=stage,
            contexts=4,
            predicted_query_rows=1344,
            fit_predict_seconds=cost["TabICL_seconds"],
            ensemble=1,
        ),
    )
    deltas = dict(
        TabICL_contexts=4, TabICL_query_rows=1344, TabICL_fit_predict_seconds=cost["TabICL_seconds"]
    )
    for key, value in before["used"].items():
        close("used delta " + key, after["used"][key], value + deltas.get(key, 0))
    for key, value in before["remaining_count_budgets"].items():
        close(
            "remaining delta " + key,
            after["remaining_count_budgets"][key],
            value - deltas.get(key, 0),
        )
    check(
        "cheap one append",
        stage not in before["new_cheap_diagnostic_seconds"]
        and after["new_cheap_diagnostic_seconds"]
        == {**before["new_cheap_diagnostic_seconds"], stage: cost["cheap_numeric_seconds"]},
    )
    expected_detail = dict(
        stage=stage,
        new_simple_fits=26,
        methods=["Ridge", "HGB"],
        entire_stage_seconds=cost["stage_seconds"],
        TabICL_seconds_accounted_separately=cost["TabICL_seconds"],
        fit_predict_seconds_included_in_cheap_stage=cost["simple_fit_seconds"],
        cost_not_counted_twice=True,
    )
    check(
        "cheap details one append",
        after["cheap_stage_details"] == [*before["cheap_stage_details"], expected_detail],
    )
    check(
        "four ordered complete calls",
        len(calls) == 4
        and [c["cell_id"] for c in calls] == s["cell_ids"]
        and all(
            c["status"] == "complete"
            and c["context_rows"] == 256
            and c["query_rows"] == 336
            and c["features"] == 28
            for c in calls
        ),
    )
    for call in calls:
        close(
            "call time " + str(call["cell_id"]),
            call["fit_seconds"] + call["predict_seconds"],
            call["seconds"],
        )
    close("Tab summed call time", sum(c["seconds"] for c in calls), cost["TabICL_seconds"])
    close(
        "separate cheap time",
        cost["stage_seconds"] - cost["TabICL_seconds"],
        cost["cheap_numeric_seconds"],
    )
    check(
        "no budget resets or RCTL addition",
        update["accounted_once"]
        and update["cap_changes"] == update["RCTL_fit_changes"] == 0
        and cost["simple_fits"] == 26,
    )
    index = source("SRC-0001144").read_text(encoding="utf-8")
    progress = source("SRC-0001151").read_text(encoding="utf-8")
    check(
        "13 actual decision rows versus historical 14",
        len([x for x in index.splitlines() if x.startswith("|")]) - 2 == 13
        and "14가지" in progress.splitlines()[17],
    )
    check(
        "unread primary evidence remains pending",
        not manifest["whole_associated_packet_reviewed"]
        and manifest["whole_primary_papers_read"] == 0,
    )
    return dict(
        success=True,
        checked_at_utc=datetime.now(UTC).isoformat(),
        checks=len(checks),
        check_names=checks,
        arrays=len(a),
        metric_groups=metric_groups,
        source_references=len(manifest["sources"]),
        teacher_MSE={k: v["MSE"] for k, v in r["teacher"].items()},
        HGB_reference_MSE=r["actual_target_HGB_reference"]["MSE"],
        HGB_latent_MSE={k: v["MSE"] for k, v in r["actual_target_HGB_latent"].items()},
        hypothetical_MAC=expected_mac,
        cheap_before=sum(before["new_cheap_diagnostic_seconds"].values()),
        cheap_after=sum(after["new_cheap_diagnostic_seconds"].values()),
        new_model_runs=0,
        original_scripts_executed=False,
        random_draws=0,
        scope=(
            "저장39배열/32지표군·선택 HDF 값·정적 구조 MAC·원장 산술. "
            "모델 재현·원논문 독해·전체 HDF 재검사가 아니다."
        ),
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = verify(args.manifest)
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "check_names"}, ensure_ascii=False))
