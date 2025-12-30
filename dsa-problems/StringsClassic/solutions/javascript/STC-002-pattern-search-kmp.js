const readline = require("readline");

class Solution {
  findOccurrences(p, t) {
    const m = p.length;
    const n = t.length;
    if (m === 0) return [];
    
    // Compute prefix function
    const pi = new Array(m).fill(0);
    let j = 0;
    for (let i = 1; i < m; i++) {
      while (j > 0 && p[i] !== p[j]) {
        j = pi[j - 1];
      }
      if (p[i] === p[j]) {
        j++;
      }
      pi[i] = j;
    }
    
    // Search
    const matches = [];
    j = 0;
    for (let i = 0; i < n; i++) {
      while (j > 0 && t[i] !== p[j]) {
        j = pi[j - 1];
      }
      if (t[i] === p[j]) {
        j++;
      }
      if (j === m) {
        matches.push(i - m + 1);
        j = pi[j - 1];
      }
    }
    return matches;
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
  if (data.length < 2) return;
  const p = data[0];
  const t = data[1];
  const solution = new Solution();
  const result = solution.findOccurrences(p, t);
  console.log(result.join(" "));
});
