const readline = require("readline");

class Solution {
  criticalEdges(n, edges, T) {
    const adj = Array.from({ length: n }, () => []);
    for (let i = 0; i < edges.length; i++) {
      const [u, v, c] = edges[i];
      adj[u].push({ v, c, idx: i });
      adj[v].push({ u, c, idx: i });
    }

    const disc = new Int32Array(n).fill(-1);
    const low = new Int32Array(n).fill(-1);
    const criticalIndices = [];
    let timer = 0;

    // Use explicit stack for iterative DFS to avoid recursion limit
    // However, Tarjan's is tricky to implement iteratively because of the post-order update low[u] = min(low[u], low[v])
    // We'll use recursion but note the limit. For competitive JS, recursion is usually fine up to 10^4-10^5 depending on engine.
    // If stack overflow occurs, we need a manual stack simulation.
    
    const dfs = (u, parentEdgeIdx) => {
      disc[u] = low[u] = ++timer;
      
      for (const { v, c, idx } of adj[u]) {
        if (idx === parentEdgeIdx) continue;
        
        if (disc[v] !== -1) {
          low[u] = Math.min(low[u], disc[v]);
        } else {
          dfs(v, idx);
          low[u] = Math.min(low[u], low[v]);
          
          if (low[v] > disc[u]) {
            if (c < T) {
              criticalIndices.push(idx);
            }
          }
        }
      }
    };

    for (let i = 0; i < n; i++) {
      if (disc[i] === -1) {
        dfs(i, -1);
      }
    }

    criticalIndices.sort((a, b) => a - b);
    return criticalIndices.map((idx) => [edges[idx][0], edges[idx][1]]);
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
  const T = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const c = parseInt(data[idx++], 10);
    edges.push([u, v, c]);
  }

  const solution = new Solution();
  const ans = solution.criticalEdges(n, edges, T);
  const out = [ans.length.toString(), ...ans.map((e) => ``e[0]`{e[1]}`)];
  console.log(out.join("\n"));
});
