const readline = require("readline");

class Solution {
  checkSubstringEquality(s, queries) {
    const n = s.length;
    const MOD1 = 1000000007n;
    const BASE1 = 313n;
    const MOD2 = 1000000009n;
    const BASE2 = 317n;
    
    const h1 = new BigInt64Array(n + 1);
    const p1 = new BigInt64Array(n + 1);
    const h2 = new BigInt64Array(n + 1);
    const p2 = new BigInt64Array(n + 1);
    
    h1[0] = 0n; p1[0] = 1n;
    h2[0] = 0n; p2[0] = 1n;
    
    for (let i = 0; i < n; i++) {
      const charCode = BigInt(s.charCodeAt(i));
      
      h1[i + 1] = (h1[i] * BASE1 + charCode) % MOD1;
      p1[i + 1] = (p1[i] * BASE1) % MOD1;
      
      h2[i + 1] = (h2[i] * BASE2 + charCode) % MOD2;
      p2[i + 1] = (p2[i] * BASE2) % MOD2;
    }
    
    const results = [];
    
    const getHash = (h, p, l, r, mod) => {
      const len = r - l + 1;
      let val = (h[r + 1] - (h[l] * p[len]) % mod) % mod;
      if (val < 0n) val += mod;
      return val;
    };
    
    for (const [l1, r1, l2, r2] of queries) {
      if (r1 - l1 !== r2 - l2) {
        results.push(false);
        continue;
      }
      
      const hash1_s1 = getHash(h1, p1, l1, r1, MOD1);
      const hash1_s2 = getHash(h1, p1, l2, r2, MOD1);
      
      if (hash1_s1 !== hash1_s2) {
        results.push(false);
        continue;
      }
      
      const hash2_s1 = getHash(h2, p2, l1, r1, MOD2);
      const hash2_s2 = getHash(h2, p2, l2, r2, MOD2);
      
      results.push(hash2_s1 === hash2_s2);
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
  
  const queries = [];
  for (let i = 0; i < q; i++) {
    const parts = data[ptr++].split(" ").map(Number);
    queries.push(parts);
  }
  
  const solution = new Solution();
  const result = solution.checkSubstringEquality(s, queries);
  
  result.forEach((ans) => console.log(ans ? "true" : "false"));
});
