const readline = require("readline");

class Solution {
  detectPeriod(s) {
    const n = s.length;
    const MOD = 1000000007n;
    const BASE = 313n;
    
    const h = new BigInt64Array(n + 1);
    const p = new BigInt64Array(n + 1);
    p[0] = 1n;
    
    for (let i = 0; i < n; i++) {
      const code = BigInt(s.charCodeAt(i));
      h[i + 1] = (h[i] * BASE + code) % MOD;
      p[i + 1] = (p[i] * BASE) % MOD;
    }
    
    const getHash = (l, r) => {
      const len = r - l + 1;
      let val = (h[r + 1] - (h[l] * p[len]) % MOD) % MOD;
      if (val < 0n) val += MOD;
      return val;
    };
    
    const divisors = [];
    for (let i = 1; i * i <= n; i++) {
      if (n % i === 0) {
        divisors.push(i);
        if (i * i !== n) divisors.push(n / i);
      }
    }
    divisors.sort((a, b) => a - b);
    
    for (const len of divisors) {
      if (len === n) return n;
      
      const h1 = getHash(0, n - len - 1);
      const h2 = getHash(len, n - 1);
      
      if (h1 === h2) return len;
    }
    
    return n;
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
  console.log(solution.detectPeriod(s));
});
