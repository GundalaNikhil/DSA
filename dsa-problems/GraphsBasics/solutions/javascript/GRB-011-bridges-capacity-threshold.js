const readline = require("readline");

class Solution {
  criticalEdges(n, edges, T) {
    const adj = Array.from({ length: n }, () => []);
    const validEdgeIndices = [];
    
    // Build adjacency list with ONLY edges where c < T
    for (let i = 0; i < edges.length; i++) {
      const [u, v, c] = edges[i];
      if (c < T) {
        adj[u].push([v, c, i]);
        adj[v].push([u, c, i]);
        validEdgeIndices.push(i);
      }
    }

    const tin = new Int32Array(n).fill(-1);
    const low = new Int32Array(n).fill(-1);
    let timer = 0;
    const bridges = new Set(); // Use Set like Python
    
    const dfs = (u, pEdgeIdx) => {
        tin[u] = low[u] = timer++;
        
        for (const [v, c, idx] of adj[u]) {
            if (idx === pEdgeIdx) {
                continue;
            }
            if (tin[v] !== -1) {
                low[u] = Math.min(low[u], tin[v]);
            } else {
                dfs(v, idx);
                low[u] = Math.min(low[u], low[v]);
                if (low[v] > tin[u]) {
                    bridges.add(idx);
                }
            }
        }
    };

    // DFS from all unvisited nodes
    for (let i = 0; i < n; i++) {
        if (tin[i] === -1) {
            dfs(i, -1);
        }
    }
    
    // Maintain original order - exactly like Python
    const result = [];
    for (let i = 0; i < edges.length; i++) {
        if (validEdgeIndices.includes(i) && bridges.has(i)) {
            const [u, v, c] = edges[i];
            result.push([u, v]);
        }
    }
    
    return result;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

let data = [];
rl.on("line", (line) => {
    if (line.trim() !== '') {
        const parts = line.trim().split(/\s+/);
        for(const p of parts) data.push(p);
    }
});

rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  function nextInt() {
      return parseInt(data[idx++], 10);
  }
  
  const n = nextInt();
  const m = nextInt();
  const T = nextInt();
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = nextInt();
    const v = nextInt();
    const c = nextInt();
    edges.push([u, v, c]);
  }

  const solution = new Solution();
  const ans = solution.criticalEdges(n, edges, T);
  console.log(ans.length.toString());
  for(const e of ans) {
      console.log(`${e[0]} ${e[1]}`);
  }
});
