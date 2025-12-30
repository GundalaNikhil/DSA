class Solution {
  isFeasible(n, edges) {
    const indegree = Array(n).fill(0);
    const adj = Array.from({ length: n }, () => []);
    
    // Build graph
    for (const [u, v] of edges) {
      adj[u].push(v);
      indegree[v]++;
    }
    
    // Initialize queue with indegree 0 nodes
    const queue = [];
    for (let i = 0; i < n; i++) {
      if (indegree[i] === 0) {
        queue.push(i);
      }
    }
    
    let processed = 0;
    
    while (queue.length > 0) {
      const u = queue.shift();
      processed++;
      
      for (const v of adj[u]) {
        indegree[v]--;
        if (indegree[v] === 0) {
          queue.push(v);
        }
      }
    }
    
    return processed === n;
  }
}
