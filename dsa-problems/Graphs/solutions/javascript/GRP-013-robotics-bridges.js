class Solution {
  findBridges(n, adj) {
    const disc = Array(n).fill(-1);
    const low = Array(n).fill(-1);
    const parent = Array(n).fill(-1);
    const bridges = [];
    let time = 0;
    
    const dfs = (u) => {
      disc[u] = low[u] = time++;
      
      for (const v of adj[u]) {
        if (disc[v] === -1) {
          parent[v] = u;
          dfs(v);
          
          low[u] = Math.min(low[u], low[v]);
          
          if (low[v] > disc[u]) {
            bridges.push([u, v]);
          }
        } else if (v !== parent[u]) {
          low[u] = Math.min(low[u], disc[v]);
        }
      }
    };
    
    for (let i = 0; i < n; i++) {
      if (disc[i] === -1) {
        dfs(i);
      }
    }
    
    return bridges;
  }
}
