class Solution {
  hasCycle(n, adj) {
    const visited = new Array(n).fill(false);
    const recStack = new Array(n).fill(false);
    
    const dfs = (node) => {
      visited[node] = true;
      recStack[node] = true;
      
      for (const neighbor of adj[node]) {
        if (!visited[neighbor]) {
          if (dfs(neighbor)) {
            return true;
          }
        } else if (recStack[neighbor]) {
          return true; // Back edge - cycle detected
        }
      }
      
      recStack[node] = false;
      return false;
    };
    
    for (let i = 0; i < n; i++) {
      if (!visited[i]) {
        if (dfs(i)) {
          return true;
        }
      }
    }
    
    return false;
  }
}
