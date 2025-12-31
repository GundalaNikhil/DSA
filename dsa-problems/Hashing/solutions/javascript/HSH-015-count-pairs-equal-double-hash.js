const readline = require("readline");

class Solution {
  countPairs(s, L) {
    const n = s.length;
    if (L > n) return 0;
    
    const MOD1 = 1000000007n;
    const BASE1 = 313n;
    const MOD2 = 1000000009n;
    const BASE2 = 317n;
    
    const counts = new Map();
    
    let h1 = 0n, h2 = 0n;
    let p1 = 1n, p2 = 1n;
    
    for (let i = 0; i < L - 1; i++) {
      p1 = (p1 * BASE1) % MOD1;
      p2 = (p2 * BASE2) % MOD2;
    }
    
    for (let i = 0; i < L; i++) {
      const val = BigInt(s.charCodeAt(i));
      h1 = (h1 * BASE1 + val) % MOD1;
      h2 = (h2 * BASE2 + val) % MOD2;
    }
    
    const getKey = (a, b) => a.toString() + "," + b.toString();
    
    let key = getKey(h1, h2);
    counts.set(key, 1);
    
    for (let i = 1; i <= n - L; i++) {
      const valRemove = BigInt(s.charCodeAt(i - 1));
      const valAdd = BigInt(s.charCodeAt(i + L - 1));
      
      let remove1 = (valRemove * p1) % MOD1;
      h1 = (h1 - remove1 + MOD1) % MOD1;
      h1 = (h1 * BASE1 + valAdd) % MOD1;
      
      let remove2 = (valRemove * p2) % MOD2;
      h2 = (h2 - remove2 + MOD2) % MOD2;
      h2 = (h2 * BASE2 + valAdd) % MOD2;
      
      key = getKey(h1, h2);
      counts.set(key, (counts.get(key) || 0) + 1);
    }
    
    let ans = 0n;
    for (const count of counts.values()) {
      const c = BigInt(count);
      ans += (c * (c - 1n)) / 2n;
    }
    
    return ans.toString();
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length < 2) return;
  const s = data[0];
  const L = parseInt(data[1]);

  const solution = new Solution();
  console.log(solution.countPairs(s, L));
});
