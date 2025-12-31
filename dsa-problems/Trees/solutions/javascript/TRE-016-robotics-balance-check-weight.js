const readline = require("readline");

class Solution {
  isBalancedWeighted(n, weight, left, right, W) {
    if (n === 0) return true;

    const dfs = (u) => {
      if (u === -1) return { height: 0, weight: 0n, balanced: true };

      const l = dfs(left[u]);
      if (!l.balanced) return { height: 0, weight: 0n, balanced: false };

      const r = dfs(right[u]);
      if (!r.balanced) return { height: 0, weight: 0n, balanced: false };

      const hDiff = Math.abs(l.height - r.height);
      let wDiff = l.weight - r.weight;
      if (wDiff < 0n) wDiff = -wDiff;

      const hBal = hDiff <= 1;
      const wBal = wDiff <= BigInt(W);

      if (hBal && wBal) {
        return {
          height: Math.max(l.height, r.height) + 1,
          weight: l.weight + r.weight + BigInt(weight[u]),
          balanced: true,
        };
      } else {
        return { height: 0, weight: 0n, balanced: false };
      }
    };

    return dfs(0).balanced;
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
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const weight = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    weight[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }
  const W = idx < data.length ? parseInt(data[idx], 10) : 0;

  const solution = new Solution();
  console.log(solution.isBalancedWeighted(n, weight, left, right, W) ? "true" : "false");
});
