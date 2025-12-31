const readline = require("readline");

class Solution {
  hasDeadlock(n, edges) {
    const adj = Array.from({ length: n }, () => []);
    const inDegree = new Int32Array(n).fill(0);
    
    for (const [u, v] of edges) {
      adj[u].push(v);
      inDegree[v]++;
    }
    
    const queue = [];
    for (let i = 0; i < n; i++) {
      if (inDegree[i] === 0) {
        queue.push(i);
      }
    }
    
    let head = 0;
    let processedCount = 0;
    
    while (head < queue.length) {
      const u = queue[head++];
      processedCount++;
      
      for (const v of adj[u]) {
        inDegree[v]--;
        if (inDegree[v] === 0) {
          queue.push(v);
        }
      }
    }
    
    return processedCount < n;
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
  
  let ptr = 0;
  const n = parseInt(data[ptr++], 10);
  const m = parseInt(data[ptr++], 10);
  
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[ptr++], 10);
    const v = parseInt(data[ptr++], 10);
    edges.push([u, v]);
  }
  
  const solution = new Solution();
  console.log(solution.hasDeadlock(n, edges));
});
