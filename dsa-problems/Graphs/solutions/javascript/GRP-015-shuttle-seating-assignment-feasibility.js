class Solution {
  checkFeasibility(n, edges) {
    const indegree = Array(n).fill(0);
    const adj = Array.from({ length: n }, () => []);

    // Build graph
    for (const [u, v] of edges) {
      adj[u].push(v);
      indegree[v]++;
    }

    // Sort neighbors for deterministic behavior
    for (const neighbors of adj) {
      neighbors.sort((a, b) => a - b);
    }

    // Count initial indegree 0 nodes
    let initialZeros = 0;
    for (let i = 0; i < n; i++) {
      if (indegree[i] === 0) {
        initialZeros++;
      }
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

    if (processed === n) {
      return [1, initialZeros];
    } else {
      return [-1];
    }
  }
}

const readline = require("readline");

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

  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = Number(tokens[ptr++]);
    const v = Number(tokens[ptr++]);
    edges.push([u, v]);
  }

  const solution = new Solution();
  const result = solution.checkFeasibility(n, edges);

  if (result.length === 1) {
    console.log(result[0]);
  } else {
    console.log(`${result[0]} ${result[1]}`);
  }
});
