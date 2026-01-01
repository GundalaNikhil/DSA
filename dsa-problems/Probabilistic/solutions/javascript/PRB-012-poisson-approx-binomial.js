const readline = require("readline");

function logFactorial(n) {
  let res = 0.0;
  for (let i = 1; i <= n; i++) res += Math.log(i);
  return res;
}

function solve(n, p, k) {
  const lambda = n * p;

  // 1. Exact Binomial
  let binomialProb = 0.0;
  if (k <= n) {
    let logBinom = logFactorial(n) - logFactorial(k) - logFactorial(n - k);
    
    if (p > 0) logBinom += k * Math.log(p);
    else if (k > 0) logBinom = -Infinity;

    if (p < 1) logBinom += (n - k) * Math.log(1.0 - p);
    else if (n - k > 0) logBinom = -Infinity;

    if (logBinom > -1e14) binomialProb = Math.exp(logBinom);
  }

  // 2. Poisson Approx
  let approxProb = 0.0;
  if (lambda === 0) {
    approxProb = (k === 0) ? 1.0 : 0.0;
  } else {
    let logP = -lambda + k * Math.log(lambda) - logFactorial(k);
    if (logP > -1e14) approxProb = Math.exp(logP);
  }

  const error = Math.abs(binomialProb - approxProb);
  return { binomial: binomialProb, approx: approxProb, error };
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part !== "") data.push(part);
  }
});

rl.on("close", () => {
  if (data.length === 0) return;
  const n = parseInt(data[0], 10);
  const p = parseFloat(data[1]);
  const k = parseInt(data[2], 10);
  const res = solve(n, p, k);
  // Output order: Approx Exact Error
  console.log(res.approx.toFixed(9) + " " + res.binomial.toFixed(9) + " " + res.error.toFixed(9));
});
