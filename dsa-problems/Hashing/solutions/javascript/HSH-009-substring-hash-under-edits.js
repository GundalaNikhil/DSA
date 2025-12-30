const readline = require("readline");

class Solution {
  processOperations(s, operations) {
    const n = s.length;
    const MOD = 1000000007n;
    const BASE = 313n;
    
    const chars = s.split('').map(c => BigInt(c.charCodeAt(0)));
    const tree = new BigInt64Array(4 * n);
    const power = new BigInt64Array(n + 1);
    
    power[0] = 1n;
    for (let i = 1; i <= n; i++) {
      power[i] = (power[i - 1] * BASE) % MOD;
    }
    
    const build = (node, start, end) => {
      if (start === end) {
        tree[node] = chars[start];
        return;
      }
      const mid = Math.floor((start + end) / 2);
      build(2 * node, start, mid);
      build(2 * node + 1, mid + 1, end);
      
      const rightLen = end - mid;
      tree[node] = (tree[2 * node] * power[rightLen] + tree[2 * node + 1]) % MOD;
    };
    
    const update = (node, start, end, idx, val) => {
      if (start === end) {
        chars[idx] = val;
        tree[node] = val;
        return;
      }
      const mid = Math.floor((start + end) / 2);
      if (idx <= mid) update(2 * node, start, mid, idx, val);
      else update(2 * node + 1, mid + 1, end, idx, val);
      
      const rightLen = end - mid;
      tree[node] = (tree[2 * node] * power[rightLen] + tree[2 * node + 1]) % MOD;
    };
    
    const query = (node, start, end, l, r) => {
      if (r < start || end < l) return -1n;
      if (l <= start && end <= r) return tree[node];
      
      const mid = Math.floor((start + end) / 2);
      const p1 = query(2 * node, start, mid, l, r);
      const p2 = query(2 * node + 1, mid + 1, end, l, r);
      
      if (p1 === -1n) return p2;
      if (p2 === -1n) return p1;
      
      const rightStart = Math.max(mid + 1, l);
      const rightEnd = Math.min(end, r);
      const rightLen = rightEnd - rightStart + 1;
      
      return (p1 * power[rightLen] + p2) % MOD;
    };
    
    build(1, 0, n - 1);
    
    const results = [];
    for (const op of operations) {
      if (op[0] === 'U') {
        const idx = parseInt(op[1]);
        const c = BigInt(op[2].charCodeAt(0));
        update(1, 0, n - 1, idx, c);
      } else {
        const l = parseInt(op[1]);
        const r = parseInt(op[2]);
        results.push(query(1, 0, n - 1, l, r));
      }
    }
    
    return results;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  let ptr = 0;
  const s = data[ptr++];
  const q = parseInt(data[ptr++]);
  
  const operations = [];
  for (let i = 0; i < q; i++) {
    operations.push(data[ptr++].split(" "));
  }
  
  const solution = new Solution();
  const result = solution.processOperations(s, operations);
  
  result.forEach((hash) => console.log(hash.toString()));
});
