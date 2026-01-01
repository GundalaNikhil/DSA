class Solution {
  process(arr, ops) {
    const n = arr.length;
    // Using BigInt because values can exceed 2^53
    // But Math.min doesn't work with BigInt directly in older envs.
    // Assuming modern env or manual comparison.
    // However, problem constraints say -10^9 to 10^9, adding up to 200000 times.
    // Max value approx 2*10^14, which fits in standard JS Number (2^53 is 9*10^15).
    // So Number is safe.
    
    const tree = new Float64Array(4 * n);
    const lazy = new Float64Array(4 * n);
    const INF = Number.MAX_SAFE_INTEGER;

    const build = (node, start, end) => {
      if (start === end) {
        tree[node] = arr[start];
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        tree[node] = Math.min(tree[2 * node + 1], tree[2 * node + 2]);
      }
    };

    const push = (node) => {
      if (lazy[node] !== 0) {
        tree[2 * node + 1] += lazy[node];
        lazy[2 * node + 1] += lazy[node];
        
        tree[2 * node + 2] += lazy[node];
        lazy[2 * node + 2] += lazy[node];
        
        lazy[node] = 0;
      }
    };

    const update = (node, start, end, l, r, val) => {
      if (l > end || r < start) return;

      if (l <= start && end <= r) {
        tree[node] += val;
        lazy[node] += val;
        return;
      }

      push(node);
      const mid = Math.floor((start + end) / 2);
      update(2 * node + 1, start, mid, l, r, val);
      update(2 * node + 2, mid + 1, end, l, r, val);
      tree[node] = Math.min(tree[2 * node + 1], tree[2 * node + 2]);
    };

    const query = (node, start, end, l, r) => {
      if (l > end || r < start) return INF;

      if (l <= start && end <= r) {
        return tree[node];
      }

      push(node);
      const mid = Math.floor((start + end) / 2);
      return Math.min(query(2 * node + 1, start, mid, l, r),
                      query(2 * node + 2, mid + 1, end, l, r));
    };

    build(0, 0, n - 1);
    const results = [];

    for (const op of ops) {
      if (op[0] === "ADD") {
        const l = parseInt(op[1], 10);
        const r = parseInt(op[2], 10);
        const x = parseInt(op[3], 10);
        update(0, 0, n - 1, l, r, x);
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
  const out = solution.process(arr, ops).map(val => (val === Number.MAX_SAFE_INTEGER ? "inf" : val));
  console.log(out.join("\n"));
});
