const readline = require("readline");

class Solution {
  bfsTraversal(n, adj) {
    const result = [];
    const visited = new Array(n).fill(false);
    const queue = [];
    
    // Start BFS from node 0
    queue.push(0);
    visited[0] = true;
    
    while (queue.length > 0) {
      const curr = queue.shift();
      result.push(curr);
      
      // Visit all unvisited neighbors
      for (const neighbor of adj[curr]) {
        if (!visited[neighbor]) {
          visited[neighbor] = true;
          queue.push(neighbor);
        }
      }
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
  let ptr = 0;
  const n = parseInt(data[ptr++]);
  const m = parseInt(data[ptr++]);
  
  const adj = Array.from({ length: n }, () => []);
  
  for (let i = 0; i < m; i++) {
    const [u, v] = data[ptr++].split(" ").map(Number);
    adj[u].push(v);
    adj[v].push(u);
  }
  
  const solution = new Solution();
  const result = solution.bfsTraversal(n, adj);
  console.log(result.join(" "));
});
