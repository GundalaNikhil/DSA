const readline = require("readline");

class Solution {
  topoSort(n, adj) {
    const indegree = new Int32Array(n).fill(0);
    for (let u = 0; u < n; u++) {
      for (const v of adj[u]) {
        indegree[v]++;
      }
    }

    const queue = [];
    for (let i = 0; i < n; i++) {
      if (indegree[i] === 0) {
        queue.push(i);
      }
    }

    const result = [];
    let head = 0; // Pointer for O(1) dequeue
    while (head < queue.length) {
      const u = queue[head++];
      result.push(u);

      for (const v of adj[u]) {
        indegree[v]--;
        if (indegree[v] === 0) {
          queue.push(v);
        }
      }
    }

    return result;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    adj[u].push(v);
  }

  const solution = new Solution();
  const order = solution.topoSort(n, adj);
  console.log(order.join(" "));
});
