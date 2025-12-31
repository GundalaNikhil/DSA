class Solution {
  process(arr, queries) {
    const K = 40;

    class Summary {
      constructor() {
        this.candidates = new Map(); // val -> count
      }

      add(val, count) {
        this.candidates.set(val, (this.candidates.get(val) || 0) + count);
        if (this.candidates.size > K) {
          let minCnt = Infinity;
          for (const c of this.candidates.values()) minCnt = Math.min(minCnt, c);
          
          const toRemove = [];
          for (const [k, v] of this.candidates.entries()) {
            const newVal = v - minCnt;
            if (newVal <= 0) toRemove.push(k);
            else this.candidates.set(k, newVal);
          }
          for (const k of toRemove) this.candidates.delete(k);
        }
      }

      merge(other) {
        for (const [val, count] of other.candidates.entries()) {
          this.add(val, count);
        }
      }
    }

    const n = arr.length;
    const positions = new Map();
    for (let i = 0; i < n; i++) {
      const x = arr[i];
      if (!positions.has(x)) positions.set(x, []);
      positions.get(x).push(i);
    }

    const tree = new Array(4 * n);

    const build = (node, start, end) => {
      if (start === end) {
        const s = new Summary();
        s.add(arr[start], 1);
        tree[node] = s;
      } else {
        const mid = Math.floor((start + end) / 2);
        build(2 * node + 1, start, mid);
        build(2 * node + 2, mid + 1, end);
        
        const s = new Summary();
        s.merge(tree[2 * node + 1]);
        s.merge(tree[2 * node + 2]);
        tree[node] = s;
      }
    };

    const queryTree = (node, start, end, l, r) => {
      if (l > end || r < start) return new Summary();
      if (l <= start && end <= r) return tree[node];
      
      const mid = Math.floor((start + end) / 2);
      const s1 = queryTree(2 * node + 1, start, mid, l, r);
      const s2 = queryTree(2 * node + 2, mid + 1, end, l, r);
      
      const res = new Summary();
      res.merge(s1);
      res.merge(s2);
      return res;
    };

    build(0, 0, n - 1);

    const results = [];
    
    const getFreq = (val, l, r) => {
      const pos = positions.get(val);
      if (!pos) return 0;
      
      // Binary search for range [l, r]
      let left = 0, right = pos.length;
      let lIdx = pos.length;
      while (left < right) {
        const mid = (left + right) >>> 1;
        if (pos[mid] >= l) {
          lIdx = mid;
          right = mid;
        } else {
          left = mid + 1;
        }
      }
      
      left = 0; right = pos.length;
      let rIdx = pos.length;
      while (left < right) {
        const mid = (left + right) >>> 1;
        if (pos[mid] > r) {
          rIdx = mid;
          right = mid;
        } else {
          left = mid + 1;
        }
      }
      
      return Math.max(0, rIdx - lIdx);
    };

    for (const [l, r, t] of queries) {
      const s = queryTree(0, 0, n - 1, l, r);
      const cands = new Set(s.candidates.keys());
      for (let i = 0; i < 40; i++) {
        cands.add(arr[l + Math.floor(Math.random() * (r - l + 1))]);
      }
      
      let bestVal = -1;
      let maxFreq = -1;
      
      for (const val of cands) {
        const freq = getFreq(val, l, r);
        if (freq >= t) {
          if (freq > maxFreq) {
            maxFreq = freq;
            bestVal = val;
          } else if (freq === maxFreq) {
            if (bestVal === -1 || val < bestVal) {
              bestVal = val;
            }
          }
        }
      }
      results.push(bestVal);
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
    const type = data[idx++]; // MAJ
    queries.push([parseInt(data[idx++], 10), parseInt(data[idx++], 10), parseInt(data[idx++], 10)]);
  }
  const solution = new Solution();
  const out = solution.process(arr, queries);
  console.log(out.join("\n"));
});
