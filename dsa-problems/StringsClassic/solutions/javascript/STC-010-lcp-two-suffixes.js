const readline = require("readline");

class Solution {
  lcpQueries(s, queries) {
    const n = s.length;
    if (n === 0) return new Array(queries.length).fill(0);
    
    // Build SA
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
    
    // Build LCP
    const lcp = new Array(n - 1).fill(0);
    let kVal = 0;
    for (let i = 0; i < n; i++) {
      if (rank[i] === n - 1) {
        kVal = 0;
        continue;
      }
      const j = sa[rank[i] + 1];
      while (i + kVal < n && j + kVal < n && s[i + kVal] === s[j + kVal]) {
        kVal++;
      }
      lcp[rank[i]] = kVal;
      if (kVal > 0) kVal--;
    }
    
    // Build Sparse Table
    const m = lcp.length;
    if (m === 0) {
        return queries.map(([i, j]) => i === j ? n - i : 0);
    }
    
    const logs = new Array(m + 1).fill(0);
    for (let i = 2; i <= m; i++) logs[i] = logs[Math.floor(i / 2)] + 1;
    
    const K = logs[m];
    const st = new Array(K + 1).fill(0).map(() => new Array(m).fill(0));
    for (let i = 0; i < m; i++) st[0][i] = lcp[i];
    
    for (let k = 1; k <= K; k++) {
      for (let i = 0; i + (1 << k) <= m; i++) {
        st[k][i] = Math.min(st[k - 1][i], st[k - 1][i + (1 << (k - 1))]);
      }
    }
    
    const query = (L, R) => {
      if (L > R) return 0;
      const j = logs[R - L + 1];
      return Math.min(st[j][L], st[j][R - (1 << j) + 1]);
    };
    
    const ans = [];
    for (const [i, j] of queries) {
      if (i === j) {
        ans.push(n - i);
      } else {
        let r1 = rank[i];
        let r2 = rank[j];
        if (r1 > r2) {
          const temp = r1; r1 = r2; r2 = temp;
        }
        ans.push(query(r1, r2 - 1));
      }
    }
    return ans;
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
  const q = parseInt(data[1], 10);
  let idx = 2;
  const queries = [];
  for (let k = 0; k < q; k++) {
    const i = parseInt(data[idx++], 10);
    const j = parseInt(data[idx++], 10);
    queries.push([i, j]);
  }

  const solution = new Solution();
  const ans = solution.lcpQueries(s, queries);
  console.log(ans.join("\n"));
});
