class Solution {
  courseSchedule(n, prerequisites, pairs) {
    const parent = Array.from({ length: n }, (_, i) => i);
    
    const find = (x) => {
      if (parent[x] !== x) {
        parent[x] = find(parent[x]);
      }
      return parent[x];
    };
    
    const union = (x, y) => {
      const px = find(x);
      const py = find(y);
      if (px !== py) {
        parent[px] = py;
      }
    };
    
    // Union pairs
    for (const [a, b] of pairs) {
      union(a, b);
    }
    
    // Build contracted graph
    const contracted = new Map();
    const inDegree = new Map();
    const roots = new Set();
    
    for (let i = 0; i < n; i++) {
      roots.add(find(i));
    }
    
    for (const root of roots) {
      contracted.set(root, []);
      inDegree.set(root, 0);
    }
    
    for (const [u, v] of prerequisites) {
      const from = find(u);
      const to = find(v);
      if (from !== to) {
        contracted.get(from).push(to);
        inDegree.set(to, inDegree.get(to) + 1);
      }
    }
    
    // Topological sort
    const queue = [];
    for (const root of roots) {
      if (inDegree.get(root) === 0) {
        queue.push(root);
      }
    }
    
    const topoOrder = [];
    while (queue.length > 0) {
      const node = queue.shift();
      topoOrder.push(node);
      
      for (const neighbor of contracted.get(node)) {
        inDegree.set(neighbor, inDegree.get(neighbor) - 1);
        if (inDegree.get(neighbor) === 0) {
          queue.push(neighbor);
        }
      }
    }
    
    if (topoOrder.length !== roots.size) {
      return []; // Cycle detected
    }
    
    // Expand super-nodes
    const result = [];
    for (const superNode of topoOrder) {
      for (let i = 0; i < n; i++) {
        if (find(i) === superNode) {
          result.push(i);
        }
      }
    }
    
    return result;
  }
}
