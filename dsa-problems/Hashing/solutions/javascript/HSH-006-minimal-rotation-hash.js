const readline = require("readline");

class Solution {
  minimalRotation(s) {
    const n = s.length;
    const doubled = s + s;
    const m = doubled.length;
    
    const MOD = 1000000007n;
    const BASE = 313n;
    
    const h = new BigInt64Array(m + 1);
    const p = new BigInt64Array(m + 1);
    p[0] = 1n;
    
    for (let i = 0; i < m; i++) {
      const code = BigInt(doubled.charCodeAt(i));
      h[i + 1] = (h[i] * BASE + code) % MOD;
      p[i + 1] = (p[i] * BASE) % MOD;
    }
    
    const getHash = (l, r) => {
      const len = r - l + 1;
      let val = (h[r + 1] - (h[l] * p[len]) % MOD) % MOD;
      if (val < 0n) val += MOD;
      return val;
    };
    
    const getLCP = (i, j) => {
      let low = 0, high = n;
      let ans = 0;
      while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        if (mid === 0) {
          low = mid + 1;
          continue;
        }
        
        const h1 = getHash(i, i + mid - 1);
        const h2 = getHash(j, j + mid - 1);
        
        if (h1 === h2) {
          ans = mid;
          low = mid + 1;
        } else {
          high = mid - 1;
        }
      }
      return ans;
    };
    
    let best = 0;
    for (let curr = 1; curr < n; curr++) {
      const lcp = getLCP(best, curr);
      if (lcp < n) {
        if (doubled.charCodeAt(curr + lcp) < doubled.charCodeAt(best + lcp)) {
          best = curr;
        }
      }
    }
    
    return doubled.substring(best, best + n);
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
  const s = data[0];

  const solution = new Solution();
  console.log(solution.minimalRotation(s));
});
