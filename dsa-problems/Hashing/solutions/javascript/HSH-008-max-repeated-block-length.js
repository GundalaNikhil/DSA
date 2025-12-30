const readline = require("readline");

class Solution {
  maxRepeatedBlockLength(s) {
    const n = s.length;
    const MOD = 1000000007n;
    const BASE = 313n;
    
    const check = (len) => {
      if (len === 0) return true;
      
      const firstOccurrence = new Map();
      let currentHash = 0n;
      let power = 1n;
      
      for (let i = 0; i < len - 1; i++) {
        power = (power * BASE) % MOD;
      }
      
      for (let i = 0; i < len; i++) {
        const code = BigInt(s.charCodeAt(i));
        currentHash = (currentHash * BASE + code) % MOD;
      }
      firstOccurrence.set(currentHash, 0);
      
      for (let i = 1; i <= n - len; i++) {
        const removeCode = BigInt(s.charCodeAt(i - 1));
        const addCode = BigInt(s.charCodeAt(i + len - 1));
        
        let remove = (removeCode * power) % MOD;
        currentHash = (currentHash - remove + MOD) % MOD;
        currentHash = (currentHash * BASE + addCode) % MOD;
        
        if (firstOccurrence.has(currentHash)) {
          if (i >= firstOccurrence.get(currentHash) + len) {
            return true;
          }
        } else {
          firstOccurrence.set(currentHash, i);
        }
      }
      return false;
    };
    
    let low = 0, high = Math.floor(n / 2);
    let ans = 0;
    
    while (low <= high) {
      const mid = Math.floor((low + high) / 2);
      if (mid === 0) {
        low = mid + 1;
        continue;
      }
      
      if (check(mid)) {
        ans = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }
    return ans;
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
  console.log(solution.maxRepeatedBlockLength(s));
});
