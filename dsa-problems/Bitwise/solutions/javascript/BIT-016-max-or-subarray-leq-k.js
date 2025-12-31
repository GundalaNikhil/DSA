const readline = require("readline");

class Solution {
  maxOrSubarrayLeqK(a, K) {
    const n = a.length;
    const bitCounts = new Int32Array(32);
    let currentOr = 0;
    let left = 0;
    let maxLen = 0;
    
    for (let right = 0; right < n; right++) {
      const val = a[right];
      for (let i = 0; i < 31; i++) {
        if ((val >>> i) & 1) {
          bitCounts[i]++;
          if (bitCounts[i] === 1) {
            currentOr |= (1 << i);
          }
        }
      }
      
      // Use unsigned comparison just in case but numbers are non-negative
      while (left <= right && currentOr > K) {
        const removeVal = a[left];
        for (let i = 0; i < 31; i++) {
          if ((removeVal >>> i) & 1) {
            bitCounts[i]--;
            if (bitCounts[i] === 0) {
              currentOr &= ~(1 << i);
            }
          }
        }
        left++;
      }
      
      if (currentOr <= K) {
        maxLen = Math.max(maxLen, right - left + 1);
      }
    }
    return maxLen;
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
    
    const K = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(solution.maxOrSubarrayLeqK(a, K));
});
