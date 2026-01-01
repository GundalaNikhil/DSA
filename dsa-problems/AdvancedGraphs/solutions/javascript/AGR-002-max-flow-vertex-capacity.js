const readline = require("readline");

class Solution {
  maxFlowVertexCap(n, s, t, cap, edges) {
    const numNodes = 2 * n;
    const adj = Array.from({ length: numNodes }, () => []);
    
    // Edge structure: [to, capacity, flow, revIndex]
    const addEdge = (from, to, cap) => {
      adj[from].push([to, cap, 0, adj[to].length]);
      adj[to].push([from, 0, 0, adj[from].length - 1]);
    };

    const INF = 1e15;

    // Vertex capacities
    for (let i = 0; i < n; i++) {
      let c = (cap[i] === -1 || i === s || i === t) ? INF : cap[i];
      addEdge(2 * i, 2 * i + 1, c);
    }

    // Edges
    for (const [u, v, c] of edges) {
      addEdge(2 * u + 1, 2 * v, c);
    }

    const sNode = 2 * s;
    const tNode = 2 * t + 1;
    let level = new Int32Array(numNodes);
    let ptr = new Int32Array(numNodes);

    const bfs = () => {
      level.fill(-1);
      level[sNode] = 0;
      const q = [sNode];
      let head = 0;
      while (head < q.length) {
        const u = q[head++];
        for (const [v, cap, flow, rev] of adj[u]) {
          if (cap - flow > 0 && level[v] === -1) {
            level[v] = level[u] + 1;
            q.push(v);
          }
        }
      }
      return level[tNode] !== -1;
    };

    const dfs = (u, pushed) => {
      if (pushed === 0 || u === tNode) return pushed;
      for (let i = ptr[u]; i < adj[u].length; i++) {
        ptr[u] = i;
        const [v, cap, flow, rev] = adj[u][i];
        if (level[u] + 1 !== level[v] || cap - flow === 0) continue;
        const tr = dfs(v, Math.min(pushed, cap - flow));
        if (tr === 0) continue;
        adj[u][i][2] += tr;
        adj[v][rev][2] -= tr;
        return tr;
      }
      return 0;
    };

    let maxFlow = 0;
    while (bfs()) {
      ptr.fill(0);
      while (true) {
        const pushed = dfs(sNode, INF);
        if (pushed === 0) break;
        maxFlow += pushed;
      }
    }

    return maxFlow;
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
  const s = parseInt(data[idx++], 10);
  const t = parseInt(data[idx++], 10);
  const cap = [];
  for (let i = 0; i < n; i++) cap.push(parseInt(data[idx++], 10));
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const c = parseInt(data[idx++], 10);
    edges.push([u, v, c]);
  }

  const solution = new Solution();
  console.log(solution.maxFlowVertexCap(n, s, t, cap, edges).toString());
});
