const readline = require("readline");

class Solution {
  lcaBlocked(n, values, blocked, left, right, u, v) {
    const parent = new Int32Array(n).fill(-1);
    
    // 1. Build Parent Map
    const q = [0];
    let head = 0;
    while (head < q.length) {
      const curr = q[head++];
      if (left[curr] !== -1) {
        parent[left[curr]] = curr;
        q.push(left[curr]);
      }
      if (right[curr] !== -1) {
        parent[right[curr]] = curr;
        q.push(right[curr]);
      }
    }
    
    // 2. Find Standard LCA
    const ancestors = new Set();
    let curr = u;
    while (curr !== -1) {
      ancestors.add(curr);
      curr = parent[curr];
    }
    
    let lca = -1;
    curr = v;
    while (curr !== -1) {
      if (ancestors.has(curr)) {
        lca = curr;
        break;
      }
      curr = parent[curr];
    }
    
    if (lca === -1) return -1;
    
    // 3. Climb up
    while (lca !== -1 && blocked[lca] === 1) {
      lca = parent[lca];
    }
    
    return lca !== -1 ? values[lca] : -1;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const values = new Array(n);
  const blocked = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    blocked[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }
  const u = parseInt(data[idx++], 10);
  const v = parseInt(data[idx++], 10);

  const solution = new Solution();
  console.log(solution.lcaBlocked(n, values, blocked, left, right, u, v).toString());
});
