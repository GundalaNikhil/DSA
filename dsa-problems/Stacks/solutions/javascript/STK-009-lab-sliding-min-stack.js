class Solution {
  update(node, start, end, idx, val) {
    if (start === end) {
      this.tree[node] = val;
      return;
    }
    const mid = Math.floor((start + end) / 2);
    if (idx <= mid) {
      this.update(2 * node, start, mid, idx, val);
    } else {
      this.update(2 * node + 1, mid + 1, end, idx, val);
    }
    this.tree[node] = Math.min(this.tree[2 * node], this.tree[2 * node + 1]);
  }

  query(node, start, end, l, r) {
    if (r < start || end < l) {
      return Infinity;
    }
    if (l <= start && end <= r) {
      return this.tree[node];
    }
    const mid = Math.floor((start + end) / 2);
    return Math.min(this.query(2 * node, start, mid, l, r),
                    this.query(2 * node + 1, mid + 1, end, l, r));
  }

  process(ops) {
    const result = [];
    const n = 100005;
    this.tree = new Array(4 * n).fill(Infinity);
    const stackVals = [];
    let currentSize = 0;
    
    for (const op of ops) {
      const cmd = op[0];
      
      if (cmd === "PUSH") {
        const val = parseInt(op[1], 10);
        stackVals.push(val);
        this.update(1, 0, n - 1, currentSize, val);
        currentSize++;
      } else if (cmd === "POP") {
        if (currentSize === 0) {
          result.push("EMPTY");
        } else {
          const val = stackVals.pop();
          result.push(val.toString());
          currentSize--;
        }
      } else if (cmd === "MIN") {
        const k = parseInt(op[1], 10);
        if (currentSize < k) {
          result.push("NA");
        } else {
          const minVal = this.query(1, 0, n - 1, currentSize - k, currentSize - 1);
          result.push(minVal.toString());
        }
      }
    }
    return result;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
});

rl.on("close", () => {
  if (lines.length === 0) return;
  
  const m = parseInt(lines[0].trim(), 10);
  const ops = [];
  
  for (let i = 1; i <= m; i++) {
    if (i < lines.length) {
      ops.push(lines[i].trim().split(/\s+/));
    }
  }
  
  const solution = new Solution();
  const res = solution.process(ops);
  console.log(res.join("\n"));
});
