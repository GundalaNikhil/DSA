const readline = require("readline");

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

    // Get all roots sorted for determinism
    const rootSet = new Set();
    for (let i = 0; i < n; i++) {
      rootSet.add(find(i));
    }
    const roots = Array.from(rootSet).sort((a, b) => a - b);

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

    // Topological sort - queue initialized with sorted zero-indegree roots
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

      // Sort neighbors for deterministic processing
      const neighbors = contracted.get(node).sort((a, b) => a - b);
      for (const neighbor of neighbors) {
        inDegree.set(neighbor, inDegree.get(neighbor) - 1);
        if (inDegree.get(neighbor) === 0) {
          queue.push(neighbor);
        }
      }
    }

    if (topoOrder.length !== roots.length) {
      return []; // Cycle detected
    }

    // Expand super-nodes
    const result = [];
    for (const superNode of topoOrder) {
      const members = [];
      for (let i = 0; i < n; i++) {
        if (find(i) === superNode) {
          members.push(i);
        }
      }
      members.sort((a, b) => a - b);
      result.push(...members);
    }

    return result;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  const tokens = data.join(" ").split(/\s+/);
  let ptr = 0;
  const n = Number(tokens[ptr++]);
  const m = Number(tokens[ptr++]);

  const prerequisites = [];
  for (let i = 0; i < m; i++) {
    const u = Number(tokens[ptr++]);
    const v = Number(tokens[ptr++]);
    prerequisites.push([u, v]);
  }

  // Handle optional pairs input
  let pairs = [];
  if (ptr < tokens.length) {
    const p = Number(tokens[ptr++]);
    for (let i = 0; i < p; i++) {
      const a = Number(tokens[ptr++]);
      const b = Number(tokens[ptr++]);
      pairs.push([a, b]);
    }
  }

  const solution = new Solution();
  const result = solution.courseSchedule(n, prerequisites, pairs);

  if (result.length === 0) {
    console.log(-1);
  } else {
    console.log(result.join(" "));
  }
});
