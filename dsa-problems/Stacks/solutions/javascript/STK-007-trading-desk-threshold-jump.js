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

  thresholdJump(prices, t) {
    const n = prices.length;
    
    // Coordinate Compression
    // Use Set for distinct, then sort
    const distinct = Array.from(new Set(prices)).sort((a, b) => a - b);
    const m = distinct.length;
    const rankMap = new Map();
    distinct.forEach((val, i) => rankMap.set(val, i));
    
    // Segment Tree
    // Size 4*m
    this.tree = new Array(4 * m).fill(Infinity);
    
    const result = new Array(n).fill(0);
    
    for (let i = n - 1; i >= 0; i--) {
      const target = prices[i] + t;
      
      // bisect_left logic
      let l = 0, r = m;
      while (l < r) {
        const mid = Math.floor((l + r) / 2);
        if (distinct[mid] < target) {
          l = mid + 1;
        } else {
          r = mid;
        }
      }
      const rank = l;
      
      if (rank < m) {
        const nearestIdx = this.query(1, 0, m - 1, rank, m - 1);
        if (nearestIdx !== Infinity) {
          result[i] = nearestIdx - i;
        }
      }
      
      this.update(1, 0, m - 1, rankMap.get(prices[i]), i);
    }
    return result;
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
  const prices = [];
  for (let i = 0; i < n; i++) {
    prices.push(parseInt(data[idx++], 10));
  }
  const t = parseInt(data[idx++], 10);
  
  const solution = new Solution();
  const res = solution.thresholdJump(prices, t);
  console.log(res.join("\n"));
});
