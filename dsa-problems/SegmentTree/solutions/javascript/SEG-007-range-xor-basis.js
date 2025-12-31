class Solution {
  process(arr, ops) {
    class Basis {
      constructor() {
        this.b = new Int32Array(30).fill(0);
      }
      
      insert(x) {
        for (let i = 29; i >= 0; i--) {
          if ((x >> i) & 1) {
            if (this.b[i] === 0) {
              this.b[i] = x;
              return;
            }
            x ^= this.b[i];
          }
        }
      }
      
      merge(other) {
        for (let i = 0; i < 30; i++) {
          if (other.b[i] !== 0) this.insert(other.b[i]);
        }
      }
      
      maxXor() {
        let res = 0;
        for (let i = 29; i >= 0; i--) {
          if ((res ^ this.b[i]) > res) res ^= this.b[i];
        }
        return res;
      }
    }

    const n = arr.length;
    const tree = new Array(4 * n).fill(null).map(() => new Basis());

    const build = (node, start, end) => {
      if (start === end) {
        tree[node] = new Basis();
        tree[node].insert(arr[start]);
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        
        tree[node] = new Basis();
        tree[node].merge(tree[2 * node + 1]);
        tree[node].merge(tree[2 * node + 2]);
      }
    };

    const update = (node, start, end, idx, val) => {
      if (start === end) {
        tree[node] = new Basis();
        tree[node].insert(val);
      } else {
        const mid = Math.floor((start + end) / 2);
        if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
        else update(2 * node + 2, mid + 1, end, idx, val);
        
        tree[node] = new Basis();
        tree[node].merge(tree[2 * node + 1]);
        tree[node].merge(tree[2 * node + 2]);
      }
    };

    const query = (node, start, end, l, r) => {
      if (l > end || r < start) return new Basis();
      if (l <= start && end <= r) return tree[node];
      
      const mid = Math.floor((start + end) / 2);
      const p1 = query(2 * node + 1, start, mid, l, r);
      const p2 = query(2 * node + 2, mid + 1, end, l, r);
      
      const res = new Basis();
      res.merge(p1);
      res.merge(p2);
      return res;
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
        const res = query(0, 0, n - 1, l, r);
        results.push(res.maxXor());
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
    ops.push([data[idx++], data[idx++], data[idx++]]);
  }
  const solution = new Solution();
  const out = solution.process(arr, ops);
  console.log(out.join("\n"));
});
