const readline = require("readline");

class Solution {
  longestWildcardPalindrome(s) {
    if (!s) return "";
    
    let T = "^";
    for (const c of s) {
      T += "#" + c;
    }
    T += "#$";
    
    const n = T.length;
    const P = new Array(n).fill(0);
    let C = 0, R = 0;
    
    for (let i = 1; i < n - 1; i++) {
      P[i] = (R > i) ? Math.min(R - i, P[2 * C - i]) : 0;
      
      while (true) {
        const c1 = T[i + 1 + P[i]];
        const c2 = T[i - 1 - P[i]];
        
        let match = false;
        if (c1 === '#' || c2 === '#') match = (c1 === c2);
        else if (c1 === '^' || c2 === '^' || c1 === '`' || c2 === '`') match = (c1 === c2);
        else match = (c1 === c2 || c1 === '?' || c2 === '?');
        
        if (match) P[i]++;
        else break;
      }
      
      if (i + P[i] > R) {
        C = i;
        R = i + P[i];
      }
    }
    
    let maxLen = 0;
    let centerIndex = 0;
    for (let i = 1; i < n - 1; i++) {
      if (P[i] > maxLen) {
        maxLen = P[i];
        centerIndex = i;
      }
    }
    
    const start = Math.floor((centerIndex - maxLen) / 2);
    return s.substring(start, start + maxLen);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part) data.push(part);
  }
});

rl.on("close", () => {
  if (data.length === 0) return;
  const s = data[0];
  const solution = new Solution();
  console.log(solution.longestWildcardPalindrome(s));
});
