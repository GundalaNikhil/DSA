const readline = require("readline");

class Solution {
  topView(n, values, left, right) {
    if (n === 0) return [];

    const viewMap = new Map(); // col -> {val, depth}
    const q = [{ u: 0, c: 0, d: 0 }];
    let minCol = 0;
    let maxCol = 0;

    while (q.length > 0) {
      const { u, c, d } = q.shift();

      if (!viewMap.has(c)) {
        viewMap.set(c, { val: values[u], depth: d });
      } else {
        const existing = viewMap.get(c);
        if (d < existing.depth) {
          viewMap.set(c, { val: values[u], depth: d });
        } else if (d === existing.depth) {
          if (values[u] > existing.val) {
            existing.val = values[u];
          }
        }
      }

      if (c < minCol) minCol = c;
      if (c > maxCol) maxCol = c;

      if (left[u] !== -1) q.push({ u: left[u], c: c - 1, d: d + 1 });
      if (right[u] !== -1) q.push({ u: right[u], c: c + 1, d: d + 1 });
    }

    const result = [];
    for (let c = minCol; c <= maxCol; c++) {
      if (viewMap.has(c)) {
        result.push(viewMap.get(c).val);
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
  const ans = solution.topView(n, values, left, right);
  console.log(ans.join(" "));
});
