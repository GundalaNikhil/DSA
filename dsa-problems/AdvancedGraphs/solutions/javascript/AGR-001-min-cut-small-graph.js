const readline = require("readline");

class Solution {
  minCut(n, edges) {
    const adj = Array.from({ length: n }, () => new Array(n).fill(0));
    for (const [u, v, w] of edges) {
      adj[u][v] += w;
      adj[v][u] += w;
    }

    let globalMinCut = Infinity;
    const merged = new Int8Array(n).fill(0);
    let nodesRemaining = n;

    while (nodesRemaining > 1) {
      const weights = new Array(n).fill(0);
      const inSet = new Int8Array(n).fill(0);
      let prev = -1;
      let curr = -1;

      for (let step = 0; step < nodesRemaining; step++) {
        prev = curr;
        curr = -1;
        let maxW = -1;

        for (let i = 0; i < n; i++) {
          if (!merged[i] && !inSet[i]) {
            if (weights[i] > maxW) {
              maxW = weights[i];
              curr = i;
            }
          }
        }

        if (curr === -1) break;
        inSet[curr] = 1;

        for (let i = 0; i < n; i++) {
          if (!merged[i] && !inSet[i]) {
            weights[i] += adj[curr][i];
          }
        }
      }

      globalMinCut = Math.min(globalMinCut, weights[curr]);

      // Merge curr into prev
      for (let i = 0; i < n; i++) {
        if (i !== curr && i !== prev && !merged[i]) {
          adj[prev][i] += adj[curr][i];
          adj[i][prev] += adj[curr][i];
        }
      }
      merged[curr] = 1;
      nodesRemaining--;
    }

    return globalMinCut === Infinity ? 0 : globalMinCut;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => { const parts = line.trim().split(/\s+/); for (const p of parts) if (p) data.push(p); });
rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const w = parseInt(data[idx++], 10);
    edges.push([u, v, w]);
  }

  const solution = new Solution();
  console.log(solution.minCut(n, edges).toString());
});
