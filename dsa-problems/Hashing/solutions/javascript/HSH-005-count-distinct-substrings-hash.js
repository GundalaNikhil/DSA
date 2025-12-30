const readline = require("readline");

class Solution {
  countDistinctSubstrings(s) {
    const n = s.length;
    const MOD = 1000000007n;
    const BASE = 313n;
    
    const distinctHashes = new Set();
    
    for (let i = 0; i < n; i++) {
      let currentHash = 0n;
      for (let j = i; j < n; j++) {
        const code = BigInt(s.charCodeAt(j));
        currentHash = (currentHash * BASE + code) % MOD;
        distinctHashes.add(currentHash);
      }
    }
    
    return distinctHashes.size + 1;
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
  console.log(solution.countDistinctSubstrings(s));
});
