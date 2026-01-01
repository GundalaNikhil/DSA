const readline = require("readline");

class Solution {
  criticalNodes(n, edges) {
    // Build adjacency list with colors
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v, c] of edges) {
      adj[u].push([v, c]);
      adj[v].push([u, c]);
    }
    
    const critNodes = [];
    
    // Brute force: try removing each node
    for (let removed = 0; removed < n; removed++) {
      const visited = new Array(n).fill(false);
      visited[removed] = true;
      
      const components = []; // [[hasRed, hasBlue], ...]
      
      for (let start = 0; start < n; start++) {
        if (!visited[start]) {
          let hasRed = false;
          let hasBlue = false;
          
          const compNodes = [];
          const stack = [start];
          visited[start] = true;
          
          while (stack.length > 0) {
            const u = stack.pop();
            compNodes.push(u);
            for (const [v, c] of adj[u]) {
              if (v === removed) continue;
              if (!visited[v]) {
                visited[v] = true;
                stack.push(v);
              }
            }
          }
          
          // Check edges within this component
          const compSet = new Set(compNodes);
          for (const u of compNodes) {
            for (const [v, color] of adj[u]) {
              if (v === removed) continue;
              if (compSet.has(v)) {
                if (color === 0) hasRed = true;
                else hasBlue = true;
              }
            }
          }
          
          components.push([hasRed, hasBlue]);
        }
      }
      
      // Check criticality condition
      const redComps = [];
      const blueComps = [];
      for (let i = 0; i < components.length; i++) {
        if (components[i][0]) redComps.push(i);
        if (components[i][1]) blueComps.push(i);
      }
      
      let isCritical = false;
      if (redComps.length > 0 && blueComps.length > 0) {
        if (redComps.length > 1 || blueComps.length > 1) {
          isCritical = true;
        } else if (redComps[0] !== blueComps[0]) {
          isCritical = true;
        }
      }
      
      if (isCritical) {
        critNodes.push(removed);
      }
    }
    
    return critNodes;
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
  // Output count and node IDs (as per problem statement)
  console.log(ans.length);
  console.log(ans.join(" "));
});
