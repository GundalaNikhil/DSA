class Solution {
  process(arr, ops) {
    const n = arr.length;
    
    // Parallel arrays
    const treeMin = new Float64Array(4 * n);
    const treeMax = new Float64Array(4 * n);
    const treeAdd = new Float64Array(4 * n);
    const treeFlip = new Int8Array(4 * n); // 0 or 1

    const applyFlip = (node) => {
      const temp = treeMin[node];
      treeMin[node] = -treeMax[node];
      treeMax[node] = -temp;
      treeAdd[node] = -treeAdd[node];
      treeFlip[node] = 1 - treeFlip[node];
    };

    const applyAdd = (node, val) => {
      treeMin[node] += val;
      treeMax[node] += val;
      treeAdd[node] += val;
    };

    const push = (node, start, end) => {
      if (treeFlip[node]) {
        applyFlip(2 * node + 1);
        applyFlip(2 * node + 2);
        treeFlip[node] = 0;
      }
      if (treeAdd[node] !== 0) {
        applyAdd(2 * node + 1, treeAdd[node]);
        applyAdd(2 * node + 2, treeAdd[node]);
        treeAdd[node] = 0;
      }
    };

    const merge = (node) => {
      treeMin[node] = Math.min(treeMin[2 * node + 1], treeMin[2 * node + 2]);
      treeMax[node] = Math.max(treeMax[2 * node + 1], treeMax[2 * node + 2]);
    };

    const build = (node, start, end) => {
      if (start === end) {
        treeMin[node] = arr[start];
        treeMax[node] = arr[start];
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        merge(node);
      }
    };

    const updateAdd = (node, start, end, l, r, val) => {
      if (l > end || r < start) return;
      if (l <= start && end <= r) {
        applyAdd(node, val);
        return;
      }
      push(node, start, end);
      const mid = Math.floor((start + end) / 2);
      updateAdd(2 * node + 1, start, mid, l, r, val);
      updateAdd(2 * node + 2, mid + 1, end, l, r, val);
      merge(node);
    };

    const updateFlip = (node, start, end, l, r) => {
      if (l > end || r < start) return;
      if (l <= start && end <= r) {
        applyFlip(node);
        return;
      }
      push(node, start, end);
      const mid = Math.floor((start + end) / 2);
      updateFlip(2 * node + 1, start, mid, l, r);
      updateFlip(2 * node + 2, mid + 1, end, l, r);
      merge(node);
    };

    const query = (node, start, end, l, r) => {
      if (l > end || r < start) return Infinity;
      if (l <= start && end <= r) return treeMin[node];
      
      push(node, start, end);
      const mid = Math.floor((start + end) / 2);
      return Math.min(query(2 * node + 1, start, mid, l, r),
                      query(2 * node + 2, mid + 1, end, l, r));
    };

    build(0, 0, n - 1);
    const results = [];

    for (const op of ops) {
      if (op[0] === "ADD") {
        updateAdd(0, 0, n - 1, parseInt(op[1]), parseInt(op[2]), parseInt(op[3]));
      } else if (op[0] === "FLIP") {
        updateFlip(0, 0, n - 1, parseInt(op[1]), parseInt(op[2]));
      } else {
        results.push(query(0, 0, n - 1, parseInt(op[1]), parseInt(op[2])));
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
    if (type === "ADD") {
      ops.push([type, data[idx++], data[idx++], data[idx++]]);
    } else {
      ops.push([type, data[idx++], data[idx++]]);
    }
  }
  const solution = new Solution();
  const out = solution.process(arr, ops);
  console.log(out.join("\n"));
});
