const readline = require("readline");

class Solution {
  findOccurrences(p, t) {
    const s = p + "#" + t;
    const n = s.length;
    const z = new Array(n).fill(0);
    let l = 0, r = 0;
    
    // Compute Z-array
    for (let i = 1; i < n; i++) {
      if (i <= r) {
        z[i] = Math.min(r - i + 1, z[i - l]);
      }
      while (i + z[i] < n && s[z[i]] === s[i + z[i]]) {
        z[i]++;
      }
      if (i + z[i] - 1 > r) {
        l = i;
        r = i + z[i] - 1;
      }
    }
    
    // Collect matches
    const matches = [];
    const pLen = p.length;
    for (let i = pLen + 1; i < n; i++) {
      if (z[i] === pLen) {
        matches.push(i - (pLen + 1));
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
  const t = data[0];
  const p = data[1];
  const solution = new Solution();
  const result = solution.findOccurrences(p, t);
  if (result.length === 0) {
    console.log("-1");
  } else {
    console.log(result.join(" "));
  }
});
