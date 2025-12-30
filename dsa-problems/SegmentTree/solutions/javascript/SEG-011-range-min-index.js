class Solution {
  process(arr, ops) {
    const n = arr.length;
    
    // We can't easily store objects in a typed array, so we use parallel arrays or objects.
    // Objects are fine for N=200k in JS usually, but parallel arrays are faster.
    // Let's use objects for clarity as per template.
    
    const tree = new Array(4 * n);

    const merge = (p1, p2) => {
      if (p1.val < p2.val) return p1;
      if (p2.val < p1.val) return p2;
      return p1.idx < p2.idx ? p1 : p2;
    };

    const build = (node, start, end) => {
      if (start === end) {
        tree[node] = { val: arr[start], idx: start };
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
      }
    };

    const update = (node, start, end, idx, val) => {
      if (start === end) {
        tree[node] = { val: val, idx: idx };
      } else {
        const mid = Math.floor((start + end) / 2);
        if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
        else update(2 * node + 2, mid + 1, end, idx, val);
        tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
      }
    };

    const query = (node, start, end, l, r) => {
      if (l > end || r < start) return { val: BigInt("999999999999999999999"), idx: -1 };
      if (l <= start && end <= r) return tree[node];
      
      const mid = Math.floor((start + end) / 2);
      const p1 = query(2 * node + 1, start, mid, l, r);
      const p2 = query(2 * node + 2, mid + 1, end, l, r);
      return merge(p1, p2);
    };

    build(0, 0, n - 1);
    const results = [];

    for (const op of ops) {
      if (op[0] === "SET") {
        const idx = parseInt(op[1], 10);
        const val = BigInt(op[2]);
        update(0, 0, n - 1, idx, val);
      } else {
        const l = parseInt(op[1], 10);
        const r = parseInt(op[2], 10);
        const res = query(0, 0, n - 1, l, r);
        results.push(res.idx);
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
  for (let i = 0; i < n; i++) arr.push(BigInt(data[idx++]));
  const ops = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++];
    ops.push([type, data[idx++], data[idx++]]);
  }
  const solution = new Solution();
  const out = solution.process(arr, ops);
  console.log(out.join("\n"));
});
