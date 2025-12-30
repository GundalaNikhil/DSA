const readline = require("readline");

class Dinic {
  constructor(n) {
    this.n = n;
    this.graph = Array.from({ length: n }, () => []);
    this.level = new Int32Array(n);
  }

  addEdge(u, v, cap) {
    this.graph[u].push({ to: v, cap: BigInt(cap), flow: 0n, rev: this.graph[v].length });
    this.graph[v].push({ to: u, cap: 0n, flow: 0n, rev: this.graph[u].length - 1 });
  }

  bfs(s, t) {
    this.level.fill(-1);
    this.level[s] = 0;
    const queue = [s];
    let head = 0;
    while (head < queue.length) {
      const u = queue[head++];
      for (const edge of this.graph[u]) {
        if (edge.cap - edge.flow > 0n && this.level[edge.to] === -1) {
          this.level[edge.to] = this.level[u] + 1;
          queue.push(edge.to);
        }
      }
    }
    return this.level[t] !== -1;
  }

  dfs(u, t, pushed, ptr) {
    if (pushed === 0n || u === t) return pushed;
    for (let i = ptr[u]; i < this.graph[u].length; i++) {
      ptr[u] = i;
      const edge = this.graph[u][i];
      if (this.level[u] + 1 !== this.level[edge.to] || edge.cap - edge.flow === 0n) continue;
      
      let tr = pushed < (edge.cap - edge.flow) ? pushed : (edge.cap - edge.flow);
      const push = this.dfs(edge.to, t, tr, ptr);
      
      if (push === 0n) continue;
      
      edge.flow += push;
      this.graph[edge.to][edge.rev].flow -= push;
      return push;
    }
    return 0n;
  }

  maxFlow(s, t) {
    let flow = 0n;
    while (this.bfs(s, t)) {
      const ptr = new Int32Array(this.n).fill(0);
      while (true) {
        const pushed = this.dfs(s, t, 1000000000000000000n, ptr);
        if (pushed === 0n) break;
        flow += pushed;
      }
    }
    return flow;
  }
}

class Solution {
  minVertexCoverCost(nU, nV, wU, wV, edges) {
    const S = 0;
    const T = nU + nV + 1;
    const dinic = new Dinic(T + 1);
    const INF = 1000000000000000000n; // 1e18

    for (let i = 0; i < nU; i++) {
      dinic.addEdge(S, i + 1, wU[i]);
    }
    for (let i = 0; i < nV; i++) {
      dinic.addEdge(nU + 1 + i, T, wV[i]);
    }
    for (const [u, v] of edges) {
      dinic.addEdge(u + 1, nU + 1 + v, INF);
    }

    return dinic.maxFlow(S, T);
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
  const nU = parseInt(data[idx++], 10);
  const nV = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const wU = [];
  const wV = [];
  for (let i = 0; i < nU; i++) wU.push(parseInt(data[idx++], 10));
  for (let i = 0; i < nV; i++) wV.push(parseInt(data[idx++], 10));
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.minVertexCoverCost(nU, nV, wU, wV, edges).toString());
});
