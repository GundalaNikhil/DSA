const readline = require("readline");

class Solution {
  verticalOrderWithWeights(n, values, weights, left, right, W) {
    if (n === 0) return [];

    const cols = new Map();
    const q = [{ u: 0, c: 0, d: 0 }];
    let minCol = 0;
    let maxCol = 0;

    while (q.length > 0) {
      const { u, c, d } = q.shift();
      
      if (!cols.has(c)) cols.set(c, []);
      cols.get(c).push({ val: values[u], weight: weights[u], depth: d });
      
      if (c < minCol) minCol = c;
      if (c > maxCol) maxCol = c;

      if (left[u] !== -1) q.push({ u: left[u], c: c - 1, d: d + 1 });
      if (right[u] !== -1) q.push({ u: right[u], c: c + 1, d: d + 1 });
    }

    const result = [];
    for (let c = minCol; c <= maxCol; c++) {
      if (cols.has(c)) {
        const list = cols.get(c);
        let totalWeight = 0n;
        for (const node of list) totalWeight += BigInt(node.weight);

        if (totalWeight >= BigInt(W)) {
          list.sort((a, b) => {
            if (a.depth !== b.depth) return a.depth - b.depth;
            if (a.weight !== b.weight) return b.weight - a.weight;
            return a.val - b.val;
          });
          result.push(list.map(node => node.val));
        }
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
  const weights = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    weights[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }
  const W = idx < data.length ? parseInt(data[idx], 10) : 0;

  const solution = new Solution();
  const cols = solution.verticalOrderWithWeights(n, values, weights, left, right, W);
  if (cols.length === 0) {
    console.log("");
  } else {
    console.log(cols.map((col) => col.join(" ")).join("\n"));
  }
});
