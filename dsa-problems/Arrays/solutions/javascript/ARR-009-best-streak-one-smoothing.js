const readline = require("readline");

class Solution {
  bestStreakWithSmoothing(a) {
    const n = a.length;
    if (n < 3) return 0;

    const maxEndingAt = new Array(n).fill(0);
    const globalMaxPrefix = new Array(n).fill(0);

    maxEndingAt[0] = a[0];
    globalMaxPrefix[0] = a[0];
    for (let i = 1; i < n; i++) {
      maxEndingAt[i] = Math.max(a[i], maxEndingAt[i - 1] + a[i]);
      globalMaxPrefix[i] = Math.max(globalMaxPrefix[i - 1], maxEndingAt[i]);
    }

    const maxStartingAt = new Array(n).fill(0);
    const globalMaxSuffix = new Array(n).fill(0);

    maxStartingAt[n - 1] = a[n - 1];
    globalMaxSuffix[n - 1] = a[n - 1];
    for (let i = n - 2; i >= 0; i--) {
      maxStartingAt[i] = Math.max(a[i], maxStartingAt[i + 1] + a[i]);
      globalMaxSuffix[i] = Math.max(globalMaxSuffix[i + 1], maxStartingAt[i]);
    }

    let ans = Number.MIN_SAFE_INTEGER;

    for (let i = 1; i < n - 1; i++) {
      const smoothedVal = Math.floor((a[i - 1] + a[i] + a[i + 1]) / 3);

      const leftPart = Math.max(0, maxEndingAt[i - 1]);
      const rightPart = Math.max(0, maxStartingAt[i + 1]);
      const crossSum = leftPart + smoothedVal + rightPart;

      const globalLeft = globalMaxPrefix[i - 1];
      const globalRight = globalMaxSuffix[i + 1];

      const currentBest = Math.max(crossSum, globalLeft, globalRight);
      ans = Math.max(ans, currentBest);
    }
    return ans;
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
  const tokens = data.join(" ").split(/\s+/);
  if (tokens.length === 0 || tokens[0] === "") return;

  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const a = [];
  for (let i = 0; i < n; i++) a.push(Number(tokens[ptr++]));

  const solution = new Solution();
  console.log(String(solution.bestStreakWithSmoothing(a)));
});
