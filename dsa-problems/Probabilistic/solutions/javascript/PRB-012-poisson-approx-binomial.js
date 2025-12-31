const readline = require("readline");

function poissonApprox(n, p, k) {
  const lambda = n * p;
  let pApprox;
  
  if (lambda === 0) {
    pApprox = (k === 0) ? 1.0 : 0.0;
  } else {
    // Manual log factorial since JS Math doesn't have lgamma
    let logFactorial = 0.0;
    for (let i = 1; i <= k; i++) {
      logFactorial += Math.log(i);
    }
    
    const logP = -lambda + k * Math.log(lambda) - logFactorial;
    pApprox = Math.exp(logP);
  }
  
  const err = Math.min(1.0, 2.0 * n * p * p);
  
  return [pApprox, err];
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  const n = parseInt(data[0], 10);
  const p = parseFloat(data[1]);
  const k = parseInt(data[2], 10);
  const res = poissonApprox(n, p, k);
  console.log(res[0].toFixed(6) + " " + res[1].toFixed(6));
});
