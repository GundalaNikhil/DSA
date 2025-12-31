const readline = require("readline");

function expectedComparisons(n, k) {
  // Initialize arrays
  const dp = Array(n + 1).fill(0).map(() => new Float64Array(n + 1));
  const colSum = Array(n + 1).fill(0).map(() => new Float64Array(n + 1));
  const diagSum = Array(n + 1).fill(0).map(() => new Float64Array(n + 1));
  
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= i; j++) {
      let total = 0.0;
      
      if (i - 1 >= j) {
        total += colSum[j][i - 1] - colSum[j][j - 1];
      }
      
      const d = i - j;
      if (j > 1) {
        total += diagSum[d][i - 1];
      }
      
      dp[i][j] = (i - 1) + total / i;
      
      colSum[j][i] = colSum[j][i - 1] + dp[i][j];
      diagSum[d][i] = diagSum[d][i - 1] + dp[i][j];
    }
  }
  
  return dp[n][k];
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
  const k = parseInt(data[1], 10);
  console.log(expectedComparisons(n, k).toFixed(6));
});
