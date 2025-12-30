const readline = require("readline");

class Solution {
  checkPalindromes(s, queries) {
    const n = s.length;
    const MOD = 1000000007n;
    const BASE = 313n;
    
    const hFwd = new BigInt64Array(n + 1);
    const hRev = new BigInt64Array(n + 1);
    const power = new BigInt64Array(n + 1);
    
    power[0] = 1n;
    const revS = s.split('').reverse().join('');
    
    for (let i = 0; i < n; i++) {
      const codeFwd = BigInt(s.charCodeAt(i));
      const codeRev = BigInt(revS.charCodeAt(i));
      
      hFwd[i + 1] = (hFwd[i] * BASE + codeFwd) % MOD;
      hRev[i + 1] = (hRev[i] * BASE + codeRev) % MOD;
      power[i + 1] = (power[i] * BASE) % MOD;
    }
    
    const getHash = (h, p, l, r) => {
      const len = r - l + 1;
      let val = (h[r + 1] - (h[l] * p[len]) % MOD) % MOD;
      if (val < 0n) val += MOD;
      return val;
    };
    
    const results = [];
    for (const [l, r] of queries) {
      const fwdHash = getHash(hFwd, power, l, r);
      
      const revL = n - 1 - r;
      const revR = n - 1 - l;
      const revHash = getHash(hRev, power, revL, revR);
      
      results.push(fwdHash === revHash);
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
    const [l, r] = data[ptr++].split(" ").map(Number);
    queries.push([l, r]);
  }
  
  const solution = new Solution();
  const result = solution.checkPalindromes(s, queries);
  
  result.forEach((ans) => console.log(ans ? "true" : "false"));
});
