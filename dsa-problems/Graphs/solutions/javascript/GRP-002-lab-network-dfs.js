const readline = require("readline");

class Solution {
  dfsTraversal(n, adj) {
    const result = [];
    const visited = new Array(n).fill(false);
    
    const dfs = (node) => {
      // Mark as visited and add to result (preorder)
      visited[node] = true;
      result.push(node);
      
      // Recursively visit all unvisited neighbors
      for (const neighbor of adj[node]) {
        if (!visited[neighbor]) {
          dfs(neighbor);
        }
      }
    };
    
    // Start DFS from node 0
    dfs(0);
    
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
  let ptr = 0;
  const n = parseInt(data[ptr++]);
  const m = parseInt(data[ptr++]);
  
  const adj = Array.from({ length: n }, () => []);

  for (let i = 0; i < m; i++) {
    const [u, v] = data[ptr++].split(" ").map(Number);
    adj[u].push(v);
    adj[v].push(u);
  }

  // Sort neighbors for deterministic traversal
  for (let i = 0; i < n; i++) {
    adj[i].sort((a, b) => a - b);
  }

  const solution = new Solution();
  const result = solution.dfsTraversal(n, adj);
  console.log(result.join(" "));
});
