const readline = require("readline");

class Solution {
  rightViewWithSkips(n, values, left, right) {
    if (n === 0) return [];

    const view = new Map();
    let maxDepth = -1;

    const dfs = (u, depth) => {
      if (u === -1) return;

      if (depth > maxDepth) maxDepth = depth;

      if (values[u] >= 0 && !view.has(depth)) {
        view.set(depth, values[u]);
      }

      dfs(right[u], depth + 1);
      dfs(left[u], depth + 1);
    };

    dfs(0, 0);

    const result = [];
    for (let d = 0; d <= maxDepth; d++) {
      if (view.has(d)) {
        result.push(view.get(d));
      }
    }
    return result;
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
  const values = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }

  const solution = new Solution();
  const ans = solution.rightViewWithSkips(n, values, left, right);
  console.log(ans.join(" "));
});
