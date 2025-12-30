const readline = require("readline");

class Solution {
  minPlanksForRoof(height) {
    const n = height.length;
    if (n === 0) return 0;

    const L = new BigInt64Array(n);
    const SumL = new BigInt64Array(n);

    L[0] = BigInt(height[0]);
    SumL[0] = BigInt(height[0]);
    for (let i = 1; i < n; i++) {
      const h = BigInt(height[i]);
      L[i] = h > L[i - 1] ? h : L[i - 1];
      SumL[i] = SumL[i - 1] + L[i];
    }

    const R = new BigInt64Array(n);
    const SumR = new BigInt64Array(n);

    R[n - 1] = BigInt(height[n - 1]);
    SumR[n - 1] = BigInt(height[n - 1]);
    for (let i = n - 2; i >= 0; i--) {
      const h = BigInt(height[i]);
      R[i] = h > R[i + 1] ? h : R[i + 1];
      SumR[i] = SumR[i + 1] + R[i];
    }

    let minTotalHeight = -1n;

    for (let i = 0; i < n; i++) {
      let minLR = L[i] < R[i] ? L[i] : R[i];
      let currentTotal = SumL[i] + SumR[i] - minLR;

      if (minTotalHeight === -1n || currentTotal < minTotalHeight) {
        minTotalHeight = currentTotal;
      }
    }

    let originalSum = 0n;
    for (const h of height) originalSum += BigInt(h);

    const result = minTotalHeight - originalSum;
    return result.toString();
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
  const height = [];
  for (let i = 0; i < n; i++) height.push(Number(tokens[ptr++]));

  const solution = new Solution();
  console.log(solution.minPlanksForRoof(height));
});
