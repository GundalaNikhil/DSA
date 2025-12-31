const readline = require("readline");

class Solution {
  maxSubarrayXorWithStart(a, s) {
    let currentXor = 0;
    let maxXor = 0;
    let first = true;
    
    const len = a.length;
    for (let i = s; i < len; i++) {
      currentXor ^= a[i];
      if (first) {
        maxXor = currentXor;
        first = false;
      } else {
        if (currentXor > maxXor) {
          maxXor = currentXor;
        }
      }
    }
    return maxXor;
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
    const tokens = data.join(" ").split(/\s+/);
    if (tokens.length === 0 || tokens[0] === "") return;
    
    let ptr = 0;
    const n = Number(tokens[ptr++]);
    const a = [];
    for (let i = 0; i < n; i++) a.push(Number(tokens[ptr++]));
    const s = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(String(solution.maxSubarrayXorWithStart(a, s)));
});
