class Solution {
  process(arr, ops) {
    const n = arr.length;
    const MOD = 1000000007n;
    
    // Using BigInt for safety with powers and modulo
    const tree = new Array(4 * n);

    const makeNode = (val) => {
      let v = BigInt(val) % MOD;
      if (v < 0n) v += MOD;
      const v2 = (v * v) % MOD;
      const v3 = (v2 * v) % MOD;
      return { sum1: v, sum2: v2, sum3: v3 };
    };

    const merge = (n1, n2) => {
      return {
        sum1: (n1.sum1 + n2.sum1) % MOD,
        sum2: (n1.sum2 + n2.sum2) % MOD,
        sum3: (n1.sum3 + n2.sum3) % MOD
      };
    };

    const build = (node, start, end) => {
      if (start === end) {
        tree[node] = makeNode(arr[start]);
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
      }
    };

    const update = (node, start, end, idx, val) => {
      if (start === end) {
        tree[node] = makeNode(val);
      } else {
        const mid = Math.floor((start + end) / 2);
        if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
        else update(2 * node + 2, mid + 1, end, idx, val);
        tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
      }
    };

    const query = (node, start, end, l, r) => {
      if (l > end || r < start) return { sum1: 0n, sum2: 0n, sum3: 0n };
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
        const val = parseInt(op[2], 10);
        update(0, 0, n - 1, idx, val);
      } else {
        const l = parseInt(op[1], 10);
        const r = parseInt(op[2], 10);
        const p = parseInt(op[3], 10);
        const res = query(0, 0, n - 1, l, r);
        if (p === 1) results.push(Number(res.sum1));
        else if (p === 2) results.push(Number(res.sum2));
        else results.push(Number(res.sum3));
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
    const type = data[idx++];
    if (type === "SET") {
      ops.push([type, data[idx++], data[idx++]]);
    } else {
      ops.push([type, data[idx++], data[idx++], data[idx++]]);
    }
  }
  const solution = new Solution();
  const out = solution.process(arr, ops);
  console.log(out.join("\n"));
});
