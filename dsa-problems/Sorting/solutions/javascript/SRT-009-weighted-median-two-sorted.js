class Solution {
  weightedMedian(A, B, wA, wB) {
    const combined = A.concat(B).slice();
    combined.sort((a, b) => a - b);

    const n = combined.length;
    if (n % 2 === 1) {
      return combined[Math.floor(n / 2)].toString();
    }

    const mid1 = combined[n / 2 - 1];
    const mid2 = combined[n / 2];
    const avg = Math.floor((mid1 + mid2) / 2);
    return avg.toString();
  }
}

const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const m = parseInt(data[idx++], 10);
const A = [];
const B = [];
for (let i = 0; i < n; i++) {
  A.push(parseInt(data[idx++], 10));
}
for (let i = 0; i < m; i++) {
  B.push(parseInt(data[idx++], 10));
}
const solution = new Solution();
console.log(solution.weightedMedian(A, B, 1, 1));
