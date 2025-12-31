class Solution {
  findArticulationPoints(n, adj) {
    const disc = Array(n).fill(-1);
    const low = Array(n).fill(-1);
    const parent = Array(n).fill(-1);
    const ap = new Set();
    let time = 0;
    
    const dfs = (u) => {
      let children = 0;
      disc[u] = low[u] = time++;
      
      for (const v of adj[u]) {
        if (disc[v] === -1) {
          children++;
          parent[v] = u;
          dfs(v);
          
          low[u] = Math.min(low[u], low[v]);
          
          if (parent[u] !== -1 && low[v] >= disc[u]) {
            ap.add(u);
          }
        } else if (v !== parent[u]) {
          low[u] = Math.min(low[u], disc[v]);
        }
      }
      
      if (parent[u] === -1 && children > 1) {
        ap.add(u);
      }
    };
    
    for (let i = 0; i < n; i++) {
      if (disc[i] === -1) {
        dfs(i);
      }
    }
    
    return Array.from(ap);
  }
}
