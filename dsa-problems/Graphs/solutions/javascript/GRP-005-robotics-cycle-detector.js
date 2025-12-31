class Solution {
  hasCycle(n, adj) {
    const visited = new Array(n).fill(false);
    
    const dfs = (node, parent) => {
      visited[node] = true;
      
      for (const neighbor of adj[node]) {
        if (!visited[neighbor]) {
          if (dfs(neighbor, node)) {
            return true;
          }
        } else if (neighbor !== parent) {
          return true; // Cycle detected
        }
      }
      
      return false;
    };
    
    for (let i = 0; i < n; i++) {
      if (!visited[i]) {
        if (dfs(i, -1)) {
          return true;
        }
      }
    }
    
    return false;
  }
}
