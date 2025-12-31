class Solution {
  process(arr, forbidden, ops) {
    const n = arr.length;
    const vals = [...arr];
    const active = forbidden.map(f => !f);
    const tree = new Int32Array(4 * n);

    const gcd = (a, b) => {
      a = Math.abs(a);
      b = Math.abs(b);
      while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
      }
      return a;
    };

    const build = (node, start, end) => {
      if (start === end) {
        tree[node] = active[start] ? vals[start] : 0;
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        tree[node] = gcd(tree[2 * node + 1], tree[2 * node + 2]);
      }
    };

    const update = (node, start, end, idx, val) => {
      if (start === end) {
        tree[node] = val;
      } else {
        const mid = Math.floor((start + end) / 2);
        if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
        else update(2 * node + 2, mid + 1, end, idx, val);
        tree[node] = gcd(tree[2 * node + 1], tree[2 * node + 2]);
      }
    };

    const query = (node, start, end, l, r) => {
      if (l > end || r < start) return 0;
      if (l <= start && end <= r) return tree[node];
      
      const mid = Math.floor((start + end) / 2);
      const p1 = query(2 * node + 1, start, mid, l, r);
      const p2 = query(2 * node + 2, mid + 1, end, l, r);
      return gcd(p1, p2);
    };

    build(0, 0, n - 1);
    const results = [];

    for (const op of ops) {
      const type = op[0];
      if (type === "TOGGLE") {
        const idx = parseInt(op[1], 10);
        active[idx] = !active[idx];
        const effVal = active[idx] ? vals[idx] : 0;
        update(0, 0, n - 1, idx, effVal);
      } else if (type === "SET") {
        const idx = parseInt(op[1], 10);
        const val = parseInt(op[2], 10);
        vals[idx] = val;
        const effVal = active[idx] ? vals[idx] : 0;
        update(0, 0, n - 1, idx, effVal);
      } else {
        const l = parseInt(op[1], 10);
        const r = parseInt(op[2], 10);
        results.push(query(0, 0, n - 1, l, r));
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
  const f = parseInt(data[idx++], 10);
  const forbidden = Array(n).fill(false);
  for (let i = 0; i < f; i++) forbidden[parseInt(data[idx++], 10)] = true;
  const ops = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++];
    if (type === "TOGGLE") {
      ops.push([type, data[idx++]]);
    } else {
      ops.push([type, data[idx++], data[idx++]]);
    }
  }
  const solution = new Solution();
  const out = solution.process(arr, forbidden, ops);
  console.log(out.join("\n"));
});
