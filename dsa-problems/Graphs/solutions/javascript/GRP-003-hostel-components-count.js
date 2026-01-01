const readline = require("readline");

class Solution {
  countComponents(n, adj) {
    const visited = new Array(n).fill(false);
    let components = 0;
    
    const bfs = (start) => {
      const queue = [start];
      visited[start] = true;
      
      while (queue.length > 0) {
        const node = queue.shift();
        
        for (const neighbor of adj[node]) {
          if (!visited[neighbor]) {
            visited[neighbor] = true;
            queue.push(neighbor);
          }
        }
      }
    };
    
    for (let i = 0; i < n; i++) {
      if (!visited[i]) {
        components++;
        bfs(i);
      }
    }
    
    return components;
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
  console.log(solution.countComponents(n, adj));
});
