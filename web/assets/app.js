"use strict";

const $ = (id) => document.getElementById(id);
const controls = ["run", "model", "cell", "period"];
const dataRoot = new URL("./data/", document.baseURI);
const number = new Intl.NumberFormat("ko-KR", { maximumFractionDigits: 3 });
const date = new Intl.DateTimeFormat("sv-SE", {
  timeZone: "UTC", year: "numeric", month: "2-digit", day: "2-digit",
  hour: "2-digit", minute: "2-digit", hourCycle: "h23",
});
const state = { manifest: null, run: null, metrics: null, points: [], chart: null, epoch: 0, controller: null };

function text(id, value) { $(id).textContent = value; }
function time(value) { return date.format(new Date(value)); }
function options(id, items) {
  $(id).replaceChildren(...items.map(([value, label]) => new Option(label, value)));
}
function status(message, error = false) {
  text("status", message);
  $("status").classList.toggle("error", error);
}
function begin() {
  state.controller?.abort();
  state.controller = new AbortController();
  state.epoch += 1;
  controls.forEach((id) => { $(id).disabled = true; });
  $("retry").hidden = true;
  $("results").hidden = true;
  $("results").setAttribute("aria-busy", "true");
  status("결과를 불러오고 있습니다.");
  return state.epoch;
}
function finish() {
  controls.forEach((id) => { $(id).disabled = false; });
  $("results").hidden = false;
  $("results").setAttribute("aria-busy", "false");
  status("결과를 불러왔습니다. 모델과 셀을 선택해 비교해 보세요.");
}
function fail(error, epoch) {
  if (epoch !== state.epoch || error.name === "AbortError") return;
  $("results").hidden = true;
  $("results").setAttribute("aria-busy", "false");
  $("retry").hidden = false;
  status(error.message || "결과를 불러오지 못했습니다. 잠시 후 다시 시도해 주세요.", true);
}
async function read(relative) {
  const url = new URL(relative, dataRoot);
  if (url.origin !== dataRoot.origin || !url.pathname.startsWith(dataRoot.pathname)) {
    throw new Error("결과 파일 경로가 올바르지 않습니다.");
  }
  const response = await fetch(url, { signal: state.controller.signal, cache: "no-cache" });
  if (!response.ok) throw new Error("결과 파일을 불러오지 못했습니다. 다시 시도해 주세요.");
  const data = await response.json();
  if (data.schema_version !== "1.0") throw new Error("지원하지 않는 결과 형식입니다.");
  return data;
}
function currentModel() {
  return state.run.models.find((model) => model.id === $("model").value);
}
function chooseCells() {
  const previous = $("cell").value;
  options("cell", currentModel().series.map((series) => [series.cell_id, "셀 " + series.cell_id]));
  if (currentModel().series.some((series) => series.cell_id === previous)) $("cell").value = previous;
}
async function readSeries(epoch) {
  const model = currentModel();
  const series = model.series.find((entry) => entry.cell_id === $("cell").value);
  if (!series) throw new Error("이 모델에 표시할 셀이 없습니다.");
  const data = await read(series.path);
  if (epoch !== state.epoch) return;
  if (data.run_id !== state.run.id || data.model_id !== model.id || data.cell_id !== series.cell_id) {
    throw new Error("선택한 실험과 결과 파일이 일치하지 않습니다.");
  }
  if (!Array.isArray(data.points) || !data.points.length) throw new Error("선택한 결과에 표시할 시점이 없습니다.");
  state.points = data.points;
  renderMetrics();
  renderRecord();
  renderChart();
  finish();
}
async function loadRun(epoch) {
  state.run = state.manifest.runs.find((run) => run.id === $("run").value);
  if (!state.run?.models?.length) throw new Error("이 실험에 등록된 모델이 없습니다.");
  options("model", state.run.models.map((model) => [model.id, model.label]));
  chooseCells();
  const metrics = await read(state.run.metrics_path);
  if (epoch !== state.epoch) return;
  if (metrics.run_id !== state.run.id) throw new Error("선택한 실험과 평가 결과가 일치하지 않습니다.");
  state.metrics = metrics;
  await readSeries(epoch);
}
async function boot() {
  const epoch = begin();
  try {
    const manifest = await read("manifest.json");
    if (epoch !== state.epoch) return;
    state.manifest = manifest;
    if (!manifest.runs?.length) throw new Error("아직 공개된 실험 결과가 없습니다.");
    text("dataset-notice", manifest.dataset.kind === "synthetic"
      ? "합성 데이터 데모 · 실제 연구 성능을 나타내지 않습니다."
      : "실험 결과 · 아래 데이터와 평가 조건을 확인해 주세요.");
    options("run", manifest.runs.map((run) => [run.id, run.label]));
    await loadRun(epoch);
  } catch (error) { fail(error, epoch); }
}
function cells(values, header = false) {
  return values.map((value, index) => {
    const cell = document.createElement(header && index === 0 ? "th" : "td");
    if (header && index === 0) cell.scope = "row";
    cell.textContent = value;
    return cell;
  });
}
function renderMetrics() {
  const model = currentModel();
  const row = state.metrics.rows.find((item) => item.model_id === model.id);
  if (!row) throw new Error("선택한 모델의 평가 지표가 없습니다.");
  text("mae", number.format(row.mae));
  text("rmse", number.format(row.rmse));
  text("macro-rmse", number.format(row.macro_rmse));
  text("metric-scope", model.label + " · 전체 " + row.n_cells + "개 셀 / " + row.n_points + "개 표본");
  $("metric-rows").replaceChildren(...state.metrics.rows.map((item) => {
    const tr = document.createElement("tr");
    tr.classList.toggle("selected", item.model_id === model.id);
    const label = state.run.models.find((entry) => entry.id === item.model_id)?.label || item.model_id;
    tr.append(...cells([label, number.format(item.mae), number.format(item.rmse), number.format(item.macro_rmse)], true));
    return tr;
  }));
}
function renderRecord() {
  const run = state.run;
  const provenance = run.provenance;
  text("dataset-description", state.manifest.dataset.description);
  const entries = [
    ["데이터", state.manifest.dataset.id],
    ["평가 구간", time(run.test_start) + " – " + time(run.test_end) + " UTC"],
    ["단위", state.manifest.dataset.unit],
    ["결과 생성", time(run.generated_at) + " UTC"],
    ["코드 버전", (provenance.commit?.slice(0, 10) || "기록 없음") + (provenance.dirty ? " · 생성 당시 미커밋 변경 포함" : "")],
  ];
  $("record").replaceChildren(...entries.flatMap(([label, value]) => {
    const dt = document.createElement("dt");
    const dd = document.createElement("dd");
    dt.textContent = label;
    dd.textContent = value;
    return [dt, dd];
  }));
}
function renderChart() {
  const count = $("period").value;
  const points = count === "all" ? state.points : state.points.slice(-Number(count));
  text("chart-caption", currentModel().label + " / 셀 " + $("cell").value + " / " + state.manifest.dataset.unit);
  text("chart-range", time(points[0].timestamp) + " – " + time(points.at(-1).timestamp) + " UTC · " + points.length + "개 시점");
  $("point-rows").replaceChildren(...points.map((point) => {
    const tr = document.createElement("tr");
    tr.append(...cells([time(point.timestamp), number.format(point.actual), number.format(point.predicted)]));
    return tr;
  }));
  if (typeof Chart === "undefined") throw new Error("차트 파일을 불러오지 못했습니다. 페이지를 새로고침해 주세요.");
  state.chart?.destroy();
  state.chart = new Chart($("forecast"), {
    type: "line",
    data: {
      labels: points.map((point) => time(point.timestamp)),
      datasets: [
        { label: "실제 값", data: points.map((point) => point.actual), borderColor: "#146d60", backgroundColor: "#146d60" },
        { label: "예측 값", data: points.map((point) => point.predicted), borderColor: "#bb6a30", backgroundColor: "#bb6a30", borderDash: [6, 4] },
      ],
    },
    options: {
      responsive: true, maintainAspectRatio: false, animation: false,
      interaction: { mode: "index", intersect: false },
      elements: { line: { borderWidth: 2 }, point: { radius: 2, hoverRadius: 4 } },
      plugins: { legend: { display: false } },
      scales: {
        x: { grid: { display: false }, ticks: { maxRotation: 0, maxTicksLimit: 7, callback(value) { return this.getLabelForValue(value).slice(11); } } },
        y: { beginAtZero: true, title: { display: true, text: state.manifest.dataset.unit }, grid: { color: "#edf1ed" } },
      },
    },
  });
}
$("run").addEventListener("change", async () => {
  const epoch = begin();
  try { await loadRun(epoch); } catch (error) { fail(error, epoch); }
});
$("model").addEventListener("change", async () => {
  const epoch = begin();
  try { chooseCells(); await readSeries(epoch); } catch (error) { fail(error, epoch); }
});
$("cell").addEventListener("change", async () => {
  const epoch = begin();
  try { await readSeries(epoch); } catch (error) { fail(error, epoch); }
});
$("period").addEventListener("change", () => {
  try { renderChart(); } catch (error) { fail(error, state.epoch); }
});
$("retry").addEventListener("click", boot);
boot();
