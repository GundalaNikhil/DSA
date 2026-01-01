const readline = require("readline");

class Solution {
  lcpArray(s, sa) {
    const n = s.length;
    const rank = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
      rank[sa[i]] = i;
    }
    
    const lcp = new Array(n - 1).fill(0);
    let k = 0;
    
    for (let i = 0; i < n; i++) {
      if (rank[i] === n - 1) {
        k = 0;
        continue;
      }
      
      const j = sa[rank[i] + 1];
      while (i + k < n && j + k < n && s[i + k] === s[j + k]) {
        k++;
      }
      
      lcp[rank[i]] = k;
      if (k > 0) k--;
    }
    return lcp;
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
  let idx = 0;
  const s = data[idx++];
  const n = parseInt(data[idx++], 10);
  if (isNaN(n) || idx + n > data.length) return;
  const sa = [];
  for (let i = 0; i < n; i++) sa.push(parseInt(data[idx++], 10));

  const solution = new Solution();
  const lcp = solution.lcpArray(s, sa);
  console.log(lcp.join(" "));
});
