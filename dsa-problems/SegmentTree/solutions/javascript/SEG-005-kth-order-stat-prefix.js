class Solution {
  kthPrefix(arr, queries) {
    // Coordinate Compression
    const unique = Array.from(new Set(arr)).sort((a, b) => a - b);
    const valMap = new Map();
    unique.forEach((val, idx) => valMap.set(val, idx));
    const m = unique.length;

    // Node class
    class Node {
      constructor(count, left, right) {
        this.count = count;
        this.left = left;
        this.right = right;
      }
    }

    const build = (l, r) => {
      if (l === r) return new Node(0, null, null);
      const mid = Math.floor((l + r) / 2);
      return new Node(0, build(l, mid), build(mid + 1, r));
    };

    const update = (node, l, r, idx) => {
      if (l === r) {
        return new Node(node.count + 1, null, null);
      }
      const mid = Math.floor((l + r) / 2);
      let left = node.left;
      let right = node.right;
      if (idx <= mid) {
        left = update(left, l, mid, idx);
      } else {
        right = update(right, mid + 1, r, idx);
      }
      return new Node(left.count + right.count, left, right);
    };

    const query = (node, l, r, k) => {
      if (l === r) return l;
      const mid = Math.floor((l + r) / 2);
      const leftCount = node.left.count;
      if (k <= leftCount) {
        return query(node.left, l, mid, k);
      } else {
        return query(node.right, mid + 1, r, k - leftCount);
      }
    };

    const nullRoot = build(0, m - 1);
    const roots = [];
    let prev = nullRoot;

    for (const x of arr) {
      const idx = valMap.get(x);
      const curr = update(prev, 0, m - 1, idx);
      roots.push(curr);
      prev = curr;
    }

    const results = [];
    for (const [r, k] of queries) {
      const idx = query(roots[r], 0, m - 1, k);
      results.push(unique[idx]);
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
  const queries = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++]; // PREFIX
    queries.push([parseInt(data[idx++], 10), parseInt(data[idx++], 10)]);
  }
  const solution = new Solution();
  const out = solution.kthPrefix(arr, queries);
  console.log(out.join("\n"));
});
