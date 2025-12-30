const readline = require("readline");

class DSU {
  constructor(n) {
    this.parent = new Int32Array(n).map((_, i) => i);
  }
  find(i) {
    if (this.parent[i] === i) return i;
    return (this.parent[i] = this.find(this.parent[i]));
  }
  unite(i, j) {
    const root_i = this.find(i);
    const root_j = this.find(j);
    if (root_i !== root_j) {
      this.parent[root_i] = root_j;
      return true;
    }
    return false;
  }
}

class Solution {
  manhattanMST(xs, ys) {
    const n = xs.length;
    let pts = [];
    for (let i = 0; i < n; i++) pts.push({ x: xs[i], y: ys[i], id: i });
    
    const edges = [];
    
    const addEdges = () => {
      pts.sort((a, b) => {
        if (a.x !== b.x) return a.x - b.x;
        return a.y - b.y;
      });
      
      const diffs = [...new Set(pts.map(p => p.y - p.x))].sort((a, b) => a - b);
      const m = diffs.length;
      const bit = new Array(m + 1).fill(null); // {val, idx}
      
      const getIdx = (val) => {
        let l = 0, r = m - 1;
        while (l <= r) {
          const mid = (l + r) >>> 1;
          if (diffs[mid] >= val) r = mid - 1;
          else l = mid + 1;
        }
        return l + 1;
      };
      
      const update = (idx, val, id) => {
        for (; idx > 0; idx -= idx & -idx) {
          if (bit[idx] === null || val > bit[idx].val) {
            bit[idx] = { val, id };
          }
        }
      };
      
      const query = (idx) => {
        let res = null;
        for (; idx <= m; idx += idx & -idx) {
          if (bit[idx] !== null) {
            if (res === null || bit[idx].val > res.val) {
              res = bit[idx];
            }
          }
        }
        return res;
      };
      
      for (let i = 0; i < n; i++) {
        const p = pts[i];
        const key = p.y - p.x;
        const idx = getIdx(key);
        const res = query(idx);
        if (res !== null) {
          const q = pts[res.id]; // res.id is index in current sorted pts
          const w = Math.abs(p.x - q.x) + Math.abs(p.y - q.y);
          edges.push({ w, u: p.id, v: q.id });
        }
        update(idx, p.x + p.y, i);
      }
    };
    
    for (let k = 0; k < 4; k++) {
      addEdges();
      // Rotate 90 degrees: (x, y) -> (y, -x)
      for (const p of pts) {
        const tmp = p.x;
        p.x = p.y;
        p.y = -tmp;
      }
    }
    
    edges.sort((a, b) => a.w - b.w);
    
    const dsu = new DSU(n);
    let mstWeight = 0n;
    let count = 0;
    
    for (const e of edges) {
      if (dsu.unite(e.u, e.v)) {
        mstWeight += BigInt(e.w);
        count++;
      }
    }
    
    return mstWeight.toString();
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
  
  let ptr = 0;
  const n = parseInt(data[ptr++], 10);
  
  const xs = [];
  for (let i = 0; i < n; i++) xs.push(parseInt(data[ptr++], 10));
  
  const ys = [];
  for (let i = 0; i < n; i++) ys.push(parseInt(data[ptr++], 10));
  
  const solution = new Solution();
  console.log(solution.manhattanMST(xs, ys));
});
