const readline = require("readline");

class SegTree {
  constructor(n) {
    this.n = n;
    this.t = new Array(4 * n).fill(0);
  }
  update(idx, val, node = 1, l = 0, r = this.n - 1) {
    if (l === r) {
      if (val > this.t[node]) this.t[node] = val;
      return;
    }
    const mid = (l + r) >> 1;
    if (idx <= mid) this.update(idx, val, node << 1, l, mid);
    else this.update(idx, val, node << 1 | 1, mid + 1, r);
    const left = this.t[node << 1], right = this.t[node << 1 | 1];
    this.t[node] = left > right ? left : right;
  }
  query(ql, qr, node = 1, l = 0, r = this.n - 1) {
    if (ql > qr) return 0;
    if (qr < l || r < ql) return 0;
    if (ql <= l && r <= qr) return this.t[node];
    const mid = (l + r) >> 1;
    const a = this.query(ql, qr, node << 1, l, mid);
    const b = this.query(ql, qr, node << 1 | 1, mid + 1, r);
    return a > b ? a : b;
  }
}

function lowerBound(arr, x) {
  let l = 0, r = arr.length;
  while (l < r) {
    const m = (l + r) >> 1;
    if (arr[m] >= x) r = m;
    else l = m + 1;
  }
  return l;
}

function upperBound(arr, x) {
  let l = 0, r = arr.length;
  while (l < r) {
    const m = (l + r) >> 1;
    if (arr[m] <= x) l = m + 1;
    else r = m;
  }
  return l;
}

class Solution {
  longestBoundedDiffSubsequence(a, d, g) {
    const vals = Array.from(new Set(a)).sort((x, y) => x - y);
    const st = new SegTree(vals.length);
    let ans = 1;

    for (const x of a) {
      const lo = x - g;
      const hi = x - d;
      const L = lowerBound(vals, lo);
      const R = upperBound(vals, hi) - 1;
      const best = st.query(L, R);
      const dp = best + 1;
      const idx = lowerBound(vals, x);
      st.update(idx, dp);
      if (dp > ans) ans = dp;
    }
    return ans;
  }
}

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const n = Number(lines[idx++]);
  const a = lines[idx++].split(" ").map(Number);
  const [d, g] = lines[idx++].split(" ").map(Number);
  const sol = new Solution();
  console.log(sol.longestBoundedDiffSubsequence(a, d, g));
});
