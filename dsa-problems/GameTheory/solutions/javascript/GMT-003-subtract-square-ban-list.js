const readline = require("readline");

class Solution {
  subtractSquareGame(n, banned) {
    const bannedSet = new Set(banned);
    const dp = new Uint8Array(n + 1); // 0: False, 1: True
    
    for (let i = 1; i <= n; i++) {
      for (let j = 1; j * j <= i; j++) {
        const s = j * j;
        if (!bannedSet.has(s)) {
          if (dp[i - s] === 0) {
            dp[i] = 1;
            break;
          }
        }
      }
    }
    
    return dp[n] === 1 ? "First" : "Second";
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
  
  const flatData = [];
  data.forEach(line => {
      line.trim().split(/\s+/).forEach(part => {
          if (part) flatData.push(part);
      });
  });
  
  if (flatData.length === 0) return;
  
  let idx = 0;
  const n = parseInt(flatData[idx++]);
  const k = parseInt(flatData[idx++]);
  
  const banned = [];
  for (let i = 0; i < k; i++) {
      banned.push(parseInt(flatData[idx++]));
  }

  const solution = new Solution();
  console.log(solution.subtractSquareGame(n, banned));
});
