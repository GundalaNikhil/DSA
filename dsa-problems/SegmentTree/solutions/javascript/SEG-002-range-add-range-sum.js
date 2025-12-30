class Solution {
  process(arr, ops) {
    const n = arr.length;
    const tree = new BigInt64Array(4 * n);
    const lazy = new BigInt64Array(4 * n);

    const build = (node, start, end) => {
      if (start === end) {
        tree[node] = BigInt(arr[start]);
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
      }
    };

    const push = (node, start, end) => {
      if (lazy[node] !== 0n) {
        const mid = Math.floor((start + end) / 2);
        
        tree[2 * node + 1] += lazy[node] * BigInt(mid - start + 1);
        lazy[2 * node + 1] += lazy[node];
        
        tree[2 * node + 2] += lazy[node] * BigInt(end - mid);
        lazy[2 * node + 2] += lazy[node];
        
        lazy[node] = 0n;
      }
    };

    const update = (node, start, end, l, r, val) => {
      if (l > end || r < start) return;

      if (l <= start && end <= r) {
        tree[node] += val * BigInt(end - start + 1);
        lazy[node] += val;
        return;
      }

      push(node, start, end);
      const mid = Math.floor((start + end) / 2);
      update(2 * node + 1, start, mid, l, r, val);
      update(2 * node + 2, mid + 1, end, l, r, val);
      tree[node] = tree[2 * node + 1] + tree[2 * node + 2];
    };

    const query = (node, start, end, l, r) => {
      if (l > end || r < start) return 0n;

      if (l <= start && end <= r) {
        return tree[node];
      }

      push(node, start, end);
      const mid = Math.floor((start + end) / 2);
      return query(2 * node + 1, start, mid, l, r) + 
             query(2 * node + 2, mid + 1, end, l, r);
    };

    build(0, 0, n - 1);
    const results = [];

    for (const op of ops) {
      if (op[0] === "ADD") {
        const l = parseInt(op[1], 10);
        const r = parseInt(op[2], 10);
        const x = BigInt(op[3]);
        update(0, 0, n - 1, l, r, x);
      } else {
        const l = parseInt(op[1], 10);
        const r = parseInt(op[2], 10);
        results.push(query(0, 0, n - 1, l, r).toString());
      }
    }
    return results;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/).filter(x => x !== "");
  for (const p of parts) data.push(p);
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const q = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) arr.push(parseInt(data[idx++], 10));
  const ops = [];
  for (let i = 0; i < q; i++) {
    const op = data[idx++];
    if (op === "ADD") {
      ops.push([op, data[idx++], data[idx++], data[idx++]]);
    } else {
      ops.push([op, data[idx++], data[idx++]]);
    }
  }
  const solution = new Solution();
  const out = solution.process(arr, ops);
  console.log(out.join("\n"));
});
