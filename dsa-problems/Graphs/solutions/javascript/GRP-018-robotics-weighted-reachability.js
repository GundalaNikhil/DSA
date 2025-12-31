class Solution {
  reachableNodes(n, adj, source, threshold) {
    const visited = new Set();
    const queue = [source];
    visited.add(source);
    
    while (queue.length > 0) {
      const node = queue.shift();
      
      for (const [neighbor, weight] of adj[node]) {
        if (weight <= threshold && !visited.has(neighbor)) {
          visited.add(neighbor);
          queue.push(neighbor);
        }
      }
    }
    
    return Array.from(visited);
  }
}
