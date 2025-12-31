const readline = require("readline");

class Solution {
  prefixFunction(s) {
    const n = s.length;
    const pi = new Array(n).fill(0);
    let j = 0; // length of the previous longest prefix
    
    for (let i = 1; i < n; i++) {
      // Backtrack
      while (j > 0 && s[i] !== s[j]) {
        j = pi[j - 1];
      }
      // Extend
      if (s[i] === s[j]) {
        j++;
      }
      pi[i] = j;
    }
    return pi;
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
  const pi = solution.prefixFunction(s);
  console.log(pi.join(" "));
});
