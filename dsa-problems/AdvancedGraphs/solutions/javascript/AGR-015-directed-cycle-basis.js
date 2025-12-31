const readline = require("readline");

class Solution {
  cycleBasis(n, edges) {
    const m = edges.length;
    const adj = Array.from({ length: n }, () => []);
    for (let i = 0; i < m; i++) {
      adj[edges[i][0]].push({ to: edges[i][1], idx: i });
    }

    // Calc basis size
    let c = 0;
    const visited = new Int8Array(n).fill(0);
    const undirAdj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
      undirAdj[u].push(v);
      undirAdj[v].push(u);
    }

    const dfs = (u) => {
      visited[u] = 1;
      for (const v of undirAdj[u]) {
        if (!visited[v]) dfs(v);
      }
    };

    for (let i = 0; i < n; i++) {
      if (!visited[i]) {
        c++;
        dfs(i);
      }
    }
    const D = m - n + c;

    // Basis using BigInt for bitsets
    const basis = new Array(m).fill(null);
    const result = [];

    for (let i = 0; i < m; i++) {
      if (result.length === D) break;

      const u = edges[i][0];
      const v = edges[i][1];

      // BFS v -> u
      const parentNode = new Int32Array(n).fill(-1);
      const parentEdge = new Int32Array(n).fill(-1);
      const q = [v];
      parentNode[v] = v;
      
      let found = false;
      let head = 0;
      while (head < q.length) {
        const curr = q[head++];
        if (curr === u) {
          found = true;
          break;
        }
        for (const edge of adj[curr]) {
          if (parentNode[edge.to] === -1) {
            parentNode[edge.to] = curr;
            parentEdge[edge.to] = edge.idx;
            q.push(edge.to);
          }
        }
      }

      if (!found) continue;

      let vec = 0n;
      vec |= (1n << BigInt(i));
      
      const path = [];
      let curr = u;
      while (curr !== v) {
        const idx = parentEdge[curr];
        vec |= (1n << BigInt(idx));
        path.push(idx);
        curr = parentNode[curr];
      }
      path.reverse();

      // Insert
      let tempVec = vec;
      let inserted = false;
      for (let j = 0; j < m; j++) {
        if ((tempVec >> BigInt(j)) & 1n) {
          if (basis[j] === null) {
            basis[j] = tempVec;
            inserted = true;
            break;
          } else {
            tempVec ^= basis[j];
          }
        }
      }

      if (inserted) {
        const cycle = [u, v];
        for (const idx of path) {
          cycle.push(edges[idx][1]);
        }
        result.push(cycle);
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
    edges.push([u, v]);
  }

  const solution = new Solution();
  const cycles = solution.cycleBasis(n, edges);
  const out = [cycles.length.toString()];
  for (const cyc of cycles) {
    out.push(`${cyc.length} ${cyc.join(" ")}`.trim());
  }
  console.log(out.join("\n").trim());
});
