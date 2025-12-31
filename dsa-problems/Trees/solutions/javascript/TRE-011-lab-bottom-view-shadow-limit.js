const readline = require("readline");

class Solution {
  bottomViewWithLimit(n, values, left, right, D) {
    if (n === 0) return [];

    const viewMap = new Map();
    const q = [{ u: 0, c: 0, d: 0 }];
    let minCol = 0;
    let maxCol = 0;

    while (q.length > 0) {
      const { u, c, d } = q.shift();

      viewMap.set(c, values[u]);
      
      if (c < minCol) minCol = c;
      if (c > maxCol) maxCol = c;

      if (d < D) {
        if (left[u] !== -1) q.push({ u: left[u], c: c - 1, d: d + 1 });
        if (right[u] !== -1) q.push({ u: right[u], c: c + 1, d: d + 1 });
      }
    }

    const result = [];
    for (let c = minCol; c <= maxCol; c++) {
      if (viewMap.has(c)) {
        result.push(viewMap.get(c));
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
  const D = idx < data.length ? parseInt(data[idx], 10) : 0;

  const solution = new Solution();
  const ans = solution.bottomViewWithLimit(n, values, left, right, D);
  console.log(ans.join(" "));
});
