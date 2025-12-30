class Solution {
  process(arr, updates) {
    class Node {
      constructor(val) {
        if (val !== undefined) {
          this.maxLen = 1;
          this.prefLen = 1;
          this.suffLen = 1;
          this.len = 1;
          this.leftVal = val;
          this.rightVal = val;
        } else {
          this.maxLen = 0;
          this.prefLen = 0;
          this.suffLen = 0;
          this.len = 0;
          this.leftVal = 0;
          this.rightVal = 0;
        }
      }
    }

    const n = arr.length;
    const tree = new Array(4 * n);

    const merge = (left, right) => {
      const res = new Node();
      res.len = left.len + right.len;
      res.leftVal = left.leftVal;
      res.rightVal = right.rightVal;
      
      res.maxLen = Math.max(left.maxLen, right.maxLen);
      res.prefLen = left.prefLen;
      res.suffLen = right.suffLen;
      
      if (left.rightVal < right.leftVal) {
        res.maxLen = Math.max(res.maxLen, left.suffLen + right.prefLen);
        if (left.prefLen === left.len) {
          res.prefLen = left.len + right.prefLen;
        }
        if (right.suffLen === right.len) {
          res.suffLen = right.len + left.suffLen;
        }
      }
      return res;
    };

    const build = (node, start, end) => {
      if (start === end) {
        tree[node] = new Node(arr[start]);
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
      }
    };

    const update = (node, start, end, idx, val) => {
      if (start === end) {
        tree[node] = new Node(val);
      } else {
        const mid = Math.floor((start + end) / 2);
        if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
        else update(2 * node + 2, mid + 1, end, idx, val);
        tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
      }
    };

    build(0, 0, n - 1);
    const results = [];

    for (const [idx, val] of updates) {
      update(0, 0, n - 1, idx, val);
      results.push(tree[0].maxLen);
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
  const updates = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++]; // SET
    updates.push([parseInt(data[idx++], 10), parseInt(data[idx++], 10)]);
  }
  const solution = new Solution();
  const out = solution.process(arr, updates);
  console.log(out.join("\n"));
});
