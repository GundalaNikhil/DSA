const readline = require("readline");

class Solution {
  coinSplit(n, A) {
    const prefixSum = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) prefixSum[i + 1] = prefixSum[i] + A[i];

    const getSum = (i, j) => prefixSum[j + 1] - prefixSum[i];
    const memo = new Map();

    const solve = (i, j) => {
      if (i === j) return 0;
      const key = `${i},${j}`;
      if (memo.has(key)) return memo.get(key);

      let maxDiff = -Infinity;

      for (let k = i; k < j; k++) {
        const sumLeft = getSum(i, k);
        const sumRight = getSum(k + 1, j);

        const valTakeLeft = -sumLeft - solve(k + 1, j);
        const valTakeRight = -sumRight - solve(i, k);

        const outcome = Math.min(valTakeLeft, valTakeRight);
        maxDiff = Math.max(maxDiff, outcome);
      }

      memo.set(key, maxDiff);
      return maxDiff;
    };

    return solve(0, n - 1);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  
  const flatData = [];
  data.forEach(line => {
      line.trim().split(/\s+/).forEach(part => {
          if (part) flatData.push(part);
      });
  });
  
  if (flatData.length === 0) return;
  
  let idx = 0;
  const n = parseInt(flatData[idx++]);
  
  const A = [];
  for (let i = 0; i < n; i++) {
      A.push(parseInt(flatData[idx++]));
  }

  const solution = new Solution();
  console.log(solution.coinSplit(n, A));
});
