const readline = require("readline");

class Solution {
  largest_eigenvalue_power(n, maxIter, matrix, epsilon) {
    let v = new Array(n).fill(1.0);
    let lambda = 0.0;

    for (let iter = 0; iter < maxIter; iter++) {
      let w = new Array(n).fill(0.0);
      for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
          w[i] += matrix[i][j] * v[j];
        }
      }

      let num = 0.0;
      let den = 0.0;
      for (let i = 0; i < n; i++) {
        num += v[i] * w[i];
        den += v[i] * v[i];
      }

      let newLambda = (den === 0) ? 0 : num / den;

      if (Math.abs(newLambda - lambda) < epsilon) {
        return newLambda;
      }
      lambda = newLambda;

      let maxVal = 0.0;
      for (let val of w) maxVal = Math.max(maxVal, Math.abs(val));

      if (maxVal < 1e-9) break;

      for (let i = 0; i < n; i++) {
        v[i] = w[i] / maxVal;
      }
    }

    return lambda;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let ptr = 0;
  
  const n = parseInt(data[ptr++]);
  const maxIter = parseInt(data[ptr++]);
  
  const matrix = [];
  for(let i=0; i<n; i++) {
      const row = [];
      for(let j=0; j<n; j++) row.push(parseFloat(data[ptr++]));
      matrix.push(row);
  }
  
  const epsilon = parseFloat(data[ptr++]);
  
  const solution = new Solution();
  const res = solution.largest_eigenvalue_power(n, maxIter, matrix, epsilon);
  
  console.log(res.toFixed(6));
});
