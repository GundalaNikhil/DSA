const readline = require("readline");

class Solution {
  countExclusiveSubstrings(a, b) {
    const s = a + "#" + b;
    const n = s.length;
    const splitIdx = a.length;
    
    // 1. Build SA
    let sa = new Array(n).fill(0).map((_, i) => i);
    let rank = new Array(n).fill(0).map((_, i) => s.charCodeAt(i));
    let newRank = new Array(n).fill(0);
    
    for (let k = 1; k < n; k *= 2) {
      sa.sort((i, j) => {
        if (rank[i] !== rank[j]) return rank[i] - rank[j];
        const ri = (i + k < n) ? rank[i + k] : -1;
        const rj = (j + k < n) ? rank[j + k] : -1;
        return ri - rj;
      });
      
      newRank[sa[0]] = 0;
      for (let i = 1; i < n; i++) {
        const prev = sa[i - 1];
        const curr = sa[i];
        const r1 = rank[prev];
        const r2 = (prev + k < n) ? rank[prev + k] : -1;
        const r3 = rank[curr];
        const r4 = (curr + k < n) ? rank[curr + k] : -1;
        
        if (r1 === r3 && r2 === r4) newRank[curr] = newRank[prev];
        else newRank[curr] = newRank[prev] + 1;
      }
      for (let i = 0; i < n; i++) rank[i] = newRank[i];
      if (rank[sa[n - 1]] === n - 1) break;
    }
    
    // 2. Build LCP
    const lcp = new Array(n).fill(0);
    let kVal = 0;
    for (let i = 0; i < n; i++) {
      if (rank[i] === 0) {
        kVal = 0;
        continue;
      }
      const j = sa[rank[i] - 1];
      while (i + kVal < n && j + kVal < n && s[i + kVal] === s[j + kVal]) {
        kVal++;
      }
      lcp[rank[i]] = kVal;
      if (kVal > 0) kVal--;
    }
    
    // 3. Max Match B
    const maxMatchB = new Array(n).fill(0);
    
    // Forward
    let currentLCP = 0;
    for (let i = 0; i < n; i++) {
      if (i > 0) currentLCP = Math.min(currentLCP, lcp[i]);
      if (sa[i] > splitIdx) {
        currentLCP = n;
      } else if (sa[i] < splitIdx) {
        maxMatchB[i] = Math.max(maxMatchB[i], currentLCP);
      }
    }
    
    // Backward
    currentLCP = 0;
    for (let i = n - 1; i >= 0; i--) {
      if (i < n - 1) currentLCP = Math.min(currentLCP, lcp[i + 1]);
      if (sa[i] > splitIdx) {
        currentLCP = n;
      } else if (sa[i] < splitIdx) {
        maxMatchB[i] = Math.max(maxMatchB[i], currentLCP);
      }
    }
    
    // 4. Count
    let count = 0n;
    let prevALCP = 0;
    
    for (let i = 0; i < n; i++) {
      if (i > 0) prevALCP = Math.min(prevALCP, lcp[i]);
      
      if (sa[i] < splitIdx) {
        const len = splitIdx - sa[i];
        const deduct = Math.max(prevALCP, maxMatchB[i]);
        if (len > deduct) {
          count += BigInt(len - deduct);
        }
        prevALCP = n;
      }
    }
    
    return count;
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
  const a = data[0];
  const b = data[1];
  const solution = new Solution();
  console.log(solution.countExclusiveSubstrings(a, b).toString());
});
