const readline = require("readline");

class Solution {
  criticalNodes(n, edges) {
    const adj = Array.from({ length: n }, () => []);
    let totalRed = 0;
    let totalBlue = 0;

    for (const [u, v, c] of edges) {
      adj[u].push([v, c]);
      adj[v].push([u, c]);
      if (c === 0) totalRed++;
      else totalBlue++;
    }

    const disc = new Int32Array(n).fill(-1);
    const low = new Int32Array(n).fill(-1);
    const subRed = new Int32Array(n).fill(0);
    const subBlue = new Int32Array(n).fill(0);
    const critical = new Set();
    let timer = 0;

    const dfs = (u, p) => {
      disc[u] = low[u] = ++timer;
      let children = 0;

      for (const [v, color] of adj[u]) {
        if (v === p) continue;

        if (disc[v] !== -1) {
          low[u] = Math.min(low[u], disc[v]);
          if (disc[v] < disc[u]) {
            if (color === 0) subRed[u]++;
            else subBlue[u]++;
          }
        } else {
          children++;
          dfs(v, u);

          const branchRed = subRed[v] + (color === 0 ? 1 : 0);
          const branchBlue = subBlue[v] + (color === 1 ? 1 : 0);

          subRed[u] += branchRed;
          subBlue[u] += branchBlue;

          low[u] = Math.min(low[u], low[v]);

          if (low[v] >= disc[u]) {
            // When u is removed, edge (u,v) is also removed.
            // Component v has only internal edges (subRed[v], subBlue[v]).
            const vRed = subRed[v];
            const vBlue = subBlue[v];

            // Rest of graph minus v's subtree and the edge (u,v)
            const restRed = totalRed - vRed - (color === 0 ? 1 : 0);
            const restBlue = totalBlue - vBlue - (color === 1 ? 1 : 0);

            if ((vRed > 0 && restBlue > 0) || (vBlue > 0 && restRed > 0)) {
              critical.add(u);
            }
          }
        }
      }

      if (p === -1 && children < 2) {
        critical.delete(u);
      }
    };

    for (let i = 0; i < n; i++) {
      if (disc[i] === -1) {
        dfs(i, -1);
      }
    }

    return Array.from(critical).sort((a, b) => a - b);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const c = data[idx++];
    edges.push([u, v, c === "R" ? 0 : 1]);
  }

  const solution = new Solution();
  const ans = solution.criticalNodes(n, edges);
  console.log(ans.length.toString());
  console.log(ans.join(" "));
});
