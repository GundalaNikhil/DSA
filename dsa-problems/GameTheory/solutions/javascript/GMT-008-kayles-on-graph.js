const readline = require("readline");

class Solution {
  kaylesOnGraph(n, edges) {
    const adjMask = new Int32Array(n);
    for (const [u, v] of edges) {
      adjMask[u] |= (1 << v);
      adjMask[v] |= (1 << u);
    }

    const memo = new Int8Array(1 << n).fill(-1); // -1: unknown, 0: Losing, 1: Winning

    const canWin = (mask) => {
      if (mask === 0) return false;
      if (memo[mask] !== -1) return memo[mask] === 1;

      let canReachLosing = false;
      for (let u = 0; u < n; u++) {
        if ((mask & (1 << u)) !== 0) {
          const removeMask = (1 << u) | adjMask[u];
          const nextMask = mask & ~removeMask;
          if (!canWin(nextMask)) {
            canReachLosing = true;
            break;
          }
        }
      }

      memo[mask] = canReachLosing ? 1 : 0;
      return canReachLosing;
    };

    return canWin((1 << n) - 1) ? "First" : "Second";
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
  
  const flatData = [];
  data.forEach(line => {
      line.trim().split(/\s+/).forEach(part => {
          if (part) flatData.push(part);
      });
  });
  
  if (flatData.length === 0) return;
  
  let idx = 0;
  const n = parseInt(flatData[idx++]);
  const m = parseInt(flatData[idx++]);
  
  const edges = [];
  for (let i = 0; i < m; i++) {
      const u = parseInt(flatData[idx++]);
      const v = parseInt(flatData[idx++]);
      edges.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.kaylesOnGraph(n, edges));
});
