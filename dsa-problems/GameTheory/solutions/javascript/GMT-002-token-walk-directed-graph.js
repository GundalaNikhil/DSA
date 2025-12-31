const readline = require("readline");

class Solution {
  determineWinningNodes(n, edges) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
      adj[u].push(v);
    }

    const memo = new Int8Array(n).fill(-1); // -1: unknown, 0: Losing, 1: Winning

    const dfs = (u) => {
      if (memo[u] !== -1) return memo[u] === 1;

      let canReachLosing = false;
      for (const v of adj[u]) {
        if (!dfs(v)) {
          canReachLosing = true;
          break;
        }
      }

      memo[u] = canReachLosing ? 1 : 0;
      return canReachLosing;
    };

    const result = [];
    for (let i = 0; i < n; i++) {
      result.push(dfs(i) ? "Winning" : "Losing");
    }
    return result;
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
  
  // Flatten data
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
  const result = solution.determineWinningNodes(n, edges);
  console.log(result.join(" "));
});
