// Example: Simple animation for KPI cards
document.addEventListener("DOMContentLoaded", () => {
  const kpis = document.querySelectorAll(".kpi-value");
  kpis.forEach(el => {
    let target = parseFloat(el.textContent);
    let count = 0;
    let step = target / 50;
    let interval = setInterval(() => {
      count += step;
      if (count >= target) {
        count = target;
        clearInterval(interval);
      }
      el.textContent = count.toFixed(2);
    }, 30);
  });
});
