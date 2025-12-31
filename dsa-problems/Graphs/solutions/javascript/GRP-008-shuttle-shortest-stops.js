class Solution {
  shortestDistances(n, adj, source) {
    const dist = new Array(n).fill(-1);
    dist[source] = 0;
    const queue = [source];
    
    while (queue.length > 0) {
      const node = queue.shift();
      
      for (const neighbor of adj[node]) {
        if (dist[neighbor] === -1) {
          dist[neighbor] = dist[node] + 1;
          queue.push(neighbor);
        }
      }
    }
    
    return dist;
  }
}
