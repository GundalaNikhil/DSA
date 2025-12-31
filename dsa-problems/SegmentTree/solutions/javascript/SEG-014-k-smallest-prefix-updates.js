class Solution {
  process(arr, ops) {
    const n = arr.length;
    
    // Parallel arrays for performance
    const treeSum = new Float64Array(4 * n);
    const treeLazy = new Float64Array(4 * n);
    const treeHasLazy = new Int8Array(4 * n); // 0 or 1

    const build = (node, start, end) => {
      if (start === end) {
        treeSum[node] = arr[start];
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        treeSum[node] = treeSum[2 * node + 1] + treeSum[2 * node + 2];
      }
    };

    const push = (node, start, end) => {
      if (treeHasLazy[node]) {
        const mid = Math.floor((start + end) / 2);
        const val = treeLazy[node];
        
        // Left
        treeLazy[2 * node + 1] = val;
        treeHasLazy[2 * node + 1] = 1;
        treeSum[2 * node + 1] = val * (mid - start + 1);
        
        // Right
        treeLazy[2 * node + 2] = val;
        treeHasLazy[2 * node + 2] = 1;
        treeSum[2 * node + 2] = val * (end - mid);
        
        treeHasLazy[node] = 0;
      }
    };

    const update = (node, start, end, l, r, val) => {
      if (l > end || r < start) return;
      if (l <= start && end <= r) {
        treeLazy[node] = val;
        treeHasLazy[node] = 1;
        treeSum[node] = val * (end - start + 1);
        return;
      }
      
      push(node, start, end);
      const mid = Math.floor((start + end) / 2);
      update(2 * node + 1, start, mid, l, r, val);
      update(2 * node + 2, mid + 1, end, l, r, val);
      treeSum[node] = treeSum[2 * node + 1] + treeSum[2 * node + 2];
    };

    const query = (node, start, end, l, r) => {
      if (l > end || r < start) return 0;
      if (l <= start && end <= r) return treeSum[node];
      
      push(node, start, end);
      const mid = Math.floor((start + end) / 2);
      return query(2 * node + 1, start, mid, l, r) + 
             query(2 * node + 2, mid + 1, end, l, r);
    };

    build(0, 0, n - 1);
    const results = [];

    for (const op of ops) {
      if (op[0] === "SETPREFIX") {
        const k = parseInt(op[1], 10);
        const x = parseInt(op[2], 10);
        if (k > 0) update(0, 0, n - 1, 0, k - 1, x);
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
    const type = data[idx++];
    ops.push([type, data[idx++], data[idx++]]);
  }
  const solution = new Solution();
  const out = solution.process(arr, ops);
  console.log(out.join("\n"));
});
