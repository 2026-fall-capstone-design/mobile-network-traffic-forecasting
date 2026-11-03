"use strict";

const $ = (id) => document.getElementById(id);
const controls = ["run", "model", "cell", "period"];
const dataRoot = new URL("./data/", document.baseURI);
const number = new Intl.NumberFormat("en-US", { maximumFractionDigits: 3 });
// "sv-SE" prints "YYYY-MM-DD HH:mm"; the chart's hour ticks rely on that shape.
const date = new Intl.DateTimeFormat("sv-SE", {
  timeZone: "UTC", year: "numeric", month: "2-digit", day: "2-digit",
  hour: "2-digit", minute: "2-digit", hourCycle: "h23",
});
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
const state = {
  manifest: null, run: null, metrics: null,
  points: [],   // all points of the selected series
  view: [],     // points currently shown in the forecast chart
  chart: null, errorChart: null, metricChart: null,
  epoch: 0, controller: null,
  anim: { raf: 0, progress: 0, playing: false, started: false, start: 0, base: 0, duration: 6000 },
};

function text(id, value) { $(id).textContent = value; }
function time(value) { return date.format(new Date(value)); }
function options(id, items) {
  $(id).replaceChildren(...items.map(([value, label]) => new Option(label, value)));
}
function status(message, error = false) {
  text("status", message);
  $("status").classList.toggle("error", error);
}
/* Chart colors come from CSS variables in style.css. They are read from the
   canvas itself, so a chart inside a light band uses the light palette and a
   chart inside a dark band uses the dark one. */
function themeFor(canvas) {
  if (typeof Chart === "undefined") throw new Error("Failed to load the chart library. Please refresh the page.");
  const style = getComputedStyle(canvas);
  const css = (name) => style.getPropertyValue(name).trim();
  Chart.defaults.color = css("--chart-tick");
  Chart.defaults.font.family = css("--font");
  Chart.defaults.borderColor = css("--chart-grid");
  return css;
}

/* ---------- Forecast playback ----------
   The chart draws itself from left to right. Axes are fixed up front so the
   lines grow into place instead of rescaling on every frame. */
function stopAnim() {
  cancelAnimationFrame(state.anim.raf);
  state.anim.playing = false;
}
function lastIndex() { return state.view.length - 1; }
function setPlayLabel() {
  const a = state.anim;
  text("play", a.playing ? "Pause" : (lastIndex() > 0 && a.progress >= lastIndex() ? "Replay" : "Play"));
}
function showFrame(progress) {
  const points = state.view;
  const last = points.length - 1;
  if (!state.chart || last < 0) return;
  const p = Math.max(0, Math.min(last, progress));
  const whole = Math.floor(p);
  const frac = p - whole;
  state.anim.progress = p;

  const actual = points.map((point, i) => (i <= whole ? point.actual : null));
  const predicted = points.map((point, i) => (i <= whole ? point.predicted : null));
  if (whole < last && frac > 0) {          // the growing tip between two points
    const from = points[whole];
    const to = points[whole + 1];
    actual[whole + 1] = from.actual + (to.actual - from.actual) * frac;
    predicted[whole + 1] = from.predicted + (to.predicted - from.predicted) * frac;
  }
  state.chart.data.datasets[0].data = actual;
  state.chart.data.datasets[1].data = predicted;
  state.chart.update("none");

  state.errorChart.data.datasets[0].data = points.map((point, i) => (i <= whole ? point.predicted - point.actual : null));
  state.errorChart.update("none");

  const label = time(points[whole].timestamp) + " UTC";
  $("scrub").value = last ? Math.round((p / last) * 1000) : 1000;
  $("scrub").setAttribute("aria-valuetext", label);
  text("playhead", label);
  setPlayLabel();
}
function play() {
  const a = state.anim;
  const last = lastIndex();
  if (last < 1) return;
  if (a.progress >= last) a.progress = 0;
  a.base = a.progress;
  a.start = performance.now();
  a.playing = true;
  a.started = true;
  setPlayLabel();
  const tick = (now) => {
    if (!a.playing) return;
    const p = a.base + ((now - a.start) / a.duration) * last;
    if (p >= last) {
      a.playing = false;
      showFrame(last);
      return;
    }
    showFrame(p);
    a.raf = requestAnimationFrame(tick);
  };
  a.raf = requestAnimationFrame(tick);
}
function pause() {
  stopAnim();
  setPlayLabel();
}
/* Start the first run when the chart scrolls into view. */
const viewObserver = "IntersectionObserver" in window
  ? new IntersectionObserver((entries) => {
      if (entries.some((entry) => entry.isIntersecting) && !state.anim.started && !reduceMotion.matches) play();
    }, { threshold: 0.4 })
  : null;

/* ---------- Loading ---------- */
function begin() {
  state.controller?.abort();
  state.controller = new AbortController();
  state.epoch += 1;
  stopAnim();
  controls.forEach((id) => { $(id).disabled = true; });
  $("retry").hidden = true;
  $("results").hidden = true;
  $("results").setAttribute("aria-busy", "true");
  status("Loading results...");
  return state.epoch;
}
function finish() {
  controls.forEach((id) => { $(id).disabled = false; });
  $("results").hidden = false;
  $("results").setAttribute("aria-busy", "false");
  status("Results loaded. Choose a model and cell to compare.");
}
function fail(error, epoch) {
  if (epoch !== state.epoch || error.name === "AbortError") return;
  stopAnim();
  $("results").hidden = true;
  $("results").setAttribute("aria-busy", "false");
  $("retry").hidden = false;
  status(error.message || "Failed to load results. Please try again later.", true);
}
async function read(relative) {
  const url = new URL(relative, dataRoot);
  if (url.origin !== dataRoot.origin || !url.pathname.startsWith(dataRoot.pathname)) {
    throw new Error("Invalid result file path.");
  }
  const response = await fetch(url, { signal: state.controller.signal, cache: "no-cache" });
  if (!response.ok) throw new Error("Failed to load the result file. Please try again.");
  const data = await response.json();
  if (data.schema_version !== "1.0") throw new Error("Unsupported result format.");
  return data;
}
function currentModel() {
  return state.run.models.find((model) => model.id === $("model").value);
}
function chooseCells() {
  const previous = $("cell").value;
  options("cell", currentModel().series.map((series) => [series.cell_id, "Cell " + series.cell_id]));
  if (currentModel().series.some((series) => series.cell_id === previous)) $("cell").value = previous;
}
async function readSeries(epoch) {
  const model = currentModel();
  const series = model.series.find((entry) => entry.cell_id === $("cell").value);
  if (!series) throw new Error("No cells available for this model.");
  const data = await read(series.path);
  if (epoch !== state.epoch) return;
  if (data.run_id !== state.run.id || data.model_id !== model.id || data.cell_id !== series.cell_id) {
    throw new Error("The selected experiment does not match the result file.");
  }
  if (!Array.isArray(data.points) || !data.points.length) throw new Error("The selected result has no time steps to display.");
  state.points = data.points;
  renderMetrics();
  renderRecord();
  renderChart();
  finish();
}
async function loadRun(epoch) {
  state.run = state.manifest.runs.find((run) => run.id === $("run").value);
  if (!state.run?.models?.length) throw new Error("No models are registered for this experiment.");
  options("model", state.run.models.map((model) => [model.id, model.label]));
  chooseCells();
  const metrics = await read(state.run.metrics_path);
  if (epoch !== state.epoch) return;
  if (metrics.run_id !== state.run.id) throw new Error("The selected experiment does not match the metrics file.");
  state.metrics = metrics;
  await readSeries(epoch);
}
async function boot() {
  const epoch = begin();
  try {
    const manifest = await read("manifest.json");
    if (epoch !== state.epoch) return;
    state.manifest = manifest;
    if (!manifest.runs?.length) throw new Error("No experiment results have been published yet.");
    text("dataset-notice", manifest.dataset.kind === "synthetic"
      ? "DEMO MODE · Results use synthetic data and do not represent actual research performance."
      : "EXPERIMENT RESULTS · Review the dataset and evaluation setup below.");
    options("run", manifest.runs.map((run) => [run.id, run.label]));
    await loadRun(epoch);
  } catch (error) { fail(error, epoch); }
}

/* ---------- Rendering ---------- */
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
  if (!row) throw new Error("No evaluation metrics found for the selected model.");
  text("mae", number.format(row.mae));
  text("rmse", number.format(row.rmse));
  text("macro-rmse", number.format(row.macro_rmse));
  text("metric-scope", model.label + " · " + row.n_cells + " cells / " + row.n_points + " samples");
  const labelOf = (item) => state.run.models.find((entry) => entry.id === item.model_id)?.label || item.model_id;
  $("metric-rows").replaceChildren(...state.metrics.rows.map((item) => {
    const tr = document.createElement("tr");
    tr.classList.toggle("selected", item.model_id === model.id);
    tr.append(...cells([labelOf(item), number.format(item.mae), number.format(item.rmse), number.format(item.macro_rmse)], true));
    return tr;
  }));
  const css = themeFor($("metric-chart"));
  const palette = [css("--series-1"), css("--series-2"), css("--series-3"), css("--series-4")];
  const grid = css("--chart-grid");
  state.metricChart?.destroy();
  state.metricChart = new Chart($("metric-chart"), {
    type: "bar",
    data: {
      labels: ["MAE", "RMSE", "Macro RMSE"],
      datasets: state.metrics.rows.map((item, index) => ({
        label: labelOf(item),
        data: [item.mae, item.rmse, item.macro_rmse],
        backgroundColor: palette[index % palette.length],
        borderRadius: 4,
      })),
    },
    options: {
      responsive: true, maintainAspectRatio: false, animation: false,
      plugins: { legend: { display: true, position: "bottom" } },
      scales: {
        x: { grid: { display: false } },
        y: { beginAtZero: true, title: { display: true, text: "Error (lower is better)" }, grid: { color: grid } },
      },
    },
  });
}
function renderRecord() {
  const run = state.run;
  const provenance = run.provenance;
  text("dataset-description", state.manifest.dataset.description);
  const entries = [
    ["Dataset", state.manifest.dataset.id],
    ["Test window", time(run.test_start) + " – " + time(run.test_end) + " UTC"],
    ["Unit", state.manifest.dataset.unit],
    ["Generated", time(run.generated_at) + " UTC"],
    ["Code version", (provenance.commit?.slice(0, 10) || "Not recorded") + (provenance.dirty ? " · includes uncommitted changes at generation time" : "")],
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
  stopAnim();
  const count = $("period").value;
  const points = count === "all" ? state.points : state.points.slice(-Number(count));
  state.view = points;
  const unit = state.manifest.dataset.unit;
  text("chart-caption", currentModel().label + " / Cell " + $("cell").value + " / " + unit);
  text("chart-range", time(points[0].timestamp) + " – " + time(points.at(-1).timestamp) + " UTC · " + points.length + " time steps");
  $("point-rows").replaceChildren(...points.map((point) => {
    const tr = document.createElement("tr");
    tr.append(...cells([time(point.timestamp), number.format(point.actual), number.format(point.predicted)]));
    return tr;
  }));

  const css = themeFor($("forecast"));
  const actual = css("--chart-actual");
  const predicted = css("--chart-predicted");
  const grid = css("--chart-grid");
  const over = css("--chart-over");
  const under = css("--chart-under");
  const hourTick = { maxRotation: 0, maxTicksLimit: 7, callback(value) { return this.getLabelForValue(value).slice(11); } };

  // Fixed axis bounds, so the lines grow into place during playback.
  const peak = Math.max(...points.flatMap((point) => [point.actual, point.predicted]));
  const errors = points.map((point) => point.predicted - point.actual);
  const bound = Math.max(...errors.map(Math.abs)) * 1.1 || 1;
  const labels = points.map((point) => time(point.timestamp));

  state.chart?.destroy();
  state.chart = new Chart($("forecast"), {
    type: "line",
    data: {
      labels,
      datasets: [
        { label: "Actual", data: [], borderColor: actual, backgroundColor: actual },
        { label: "Predicted", data: [], borderColor: predicted, backgroundColor: predicted, borderDash: [6, 4] },
      ],
    },
    options: {
      responsive: true, maintainAspectRatio: false, animation: false,
      interaction: { mode: "index", intersect: false },
      elements: { line: { borderWidth: 2 }, point: { radius: 2, hoverRadius: 4 } },
      plugins: { legend: { display: false } },
      scales: {
        x: { grid: { display: false }, ticks: hourTick },
        y: { beginAtZero: true, suggestedMax: peak * 1.08, title: { display: true, text: unit }, grid: { color: grid } },
      },
    },
  });
  state.errorChart?.destroy();
  state.errorChart = new Chart($("error-chart"), {
    type: "bar",
    data: {
      labels,
      datasets: [{
        label: "Predicted − Actual",
        data: [],
        backgroundColor: errors.map((value) => (value >= 0 ? over : under)),
        borderRadius: 3,
      }],
    },
    options: {
      responsive: true, maintainAspectRatio: false, animation: false,
      plugins: { legend: { display: false } },
      scales: {
        x: { grid: { display: false }, ticks: hourTick },
        y: { suggestedMin: -bound, suggestedMax: bound, title: { display: true, text: "Error (" + unit + ")" }, grid: { color: grid } },
      },
    },
  });

  // Playback setup: about 220 ms per time step, between 5 and 14 seconds in total.
  const a = state.anim;
  a.duration = Math.min(14000, Math.max(5000, (points.length - 1) * 220));
  a.started = false;
  a.progress = 0;
  const canAnimate = points.length > 1 && viewObserver && !reduceMotion.matches;
  showFrame(canAnimate ? 0 : points.length - 1);
  if (viewObserver) {
    const target = $("forecast");
    viewObserver.unobserve(target);
    viewObserver.observe(target);      // fires right away, so it also covers "already in view"
  }
}

/* ---------- Events ---------- */
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
$("play").addEventListener("click", () => {
  if (state.anim.playing) pause(); else play();
});
$("scrub").addEventListener("input", () => {
  pause();
  state.anim.started = true;           // the viewer is in control now; don't auto-start
  showFrame((Number($("scrub").value) / 1000) * lastIndex());
});
$("retry").addEventListener("click", boot);
boot();