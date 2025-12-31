const readline = require("readline");

class Solution {
  minimalRotationIndex(s) {
    const n = s.length;
    if (n === 0) return 0;
    const text = s + s;
    const m = text.length;
    
    let sa = new Array(m).fill(0).map((_, i) => i);
    let rank = new Array(m).fill(0).map((_, i) => text.charCodeAt(i));
    let newRank = new Array(m).fill(0);
    
    for (let k = 1; k < m; k *= 2) {
      sa.sort((i, j) => {
        if (rank[i] !== rank[j]) return rank[i] - rank[j];
        const ri = (i + k < m) ? rank[i + k] : -1;
        const rj = (j + k < m) ? rank[j + k] : -1;
        return ri - rj;
      });
      
      newRank[sa[0]] = 0;
      for (let i = 1; i < m; i++) {
        const prev = sa[i - 1];
        const curr = sa[i];
        const r1 = rank[prev];
        const r2 = (prev + k < m) ? rank[prev + k] : -1;
        const r3 = rank[curr];
        const r4 = (curr + k < m) ? rank[curr + k] : -1;
        
        if (r1 === r3 && r2 === r4) newRank[curr] = newRank[prev];
        else newRank[curr] = newRank[prev] + 1;
      }
      for (let i = 0; i < m; i++) rank[i] = newRank[i];
      if (rank[sa[m - 1]] === m - 1) break;
    }
    
    for (let i = 0; i < m; i++) {
      if (sa[i] < n) return sa[i];
    }
    return 0;
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
  console.log(solution.minimalRotationIndex(s).toString());
});
