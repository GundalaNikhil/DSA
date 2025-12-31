const readline = require("readline");

class MinCostMaxFlow {
  constructor(n) {
    this.n = n;
    this.graph = Array.from({ length: n }, () => []);
    this.dist = new Array(n);
    this.h = new Array(n).fill(0);
    this.parentNode = new Int32Array(n);
    this.parentEdge = new Int32Array(n);
    this.INF = 1000000000000000000; // Large number
  }

  addEdge(u, v, cap, cost) {
    this.graph[u].push({ to: v, cap: cap, flow: 0, cost: cost, rev: this.graph[v].length });
    this.graph[v].push({ to: u, cap: 0, flow: 0, cost: -cost, rev: this.graph[u].length - 1 });
  }

  spfa(s) {
    this.h.fill(this.INF);
    this.h[s] = 0;
    const inQueue = new Int8Array(this.n).fill(0);
    const queue = [s];
    inQueue[s] = 1;
    
    let head = 0;
    while (head < queue.length) {
        const u = queue[head++];
        inQueue[u] = 0;
        for (const edge of this.graph[u]) {
            if (edge.cap - edge.flow > 0 && this.h[edge.to] > this.h[u] + edge.cost) {
                this.h[edge.to] = this.h[u] + edge.cost;
                if (!inQueue[edge.to]) {
                    queue.push(edge.to);
                    inQueue[edge.to] = 1;
                }
            }
        }
    }
  }

  dijkstra(s, t) {
    this.dist.fill(this.INF);
    this.dist[s] = 0;
    // Simple priority queue implementation or array scan for O(V^2)
    // Since N=500, O(V^2) is fine.
    const visited = new Int8Array(this.n).fill(0);
    
    for (let i = 0; i < this.n; i++) {
        let u = -1;
        let bestDist = this.INF;
        for (let j = 0; j < this.n; j++) {
            if (!visited[j] && this.dist[j] < bestDist) {
                u = j;
                bestDist = this.dist[j];
            }
        }
        
        if (u === -1 || bestDist === this.INF) break;
        visited[u] = 1;
        
        for (let k = 0; k < this.graph[u].length; k++) {
            const edge = this.graph[u][k];
            const reducedCost = edge.cost + this.h[u] - this.h[edge.to];
            if (edge.cap - edge.flow > 0 && this.dist[edge.to] > this.dist[u] + reducedCost) {
                this.dist[edge.to] = this.dist[u] + reducedCost;
                this.parentNode[edge.to] = u;
                this.parentEdge[edge.to] = k;
            }
        }
    }
    return this.dist[t] !== this.INF;
  }

  solve(s, t) {
    let flow = 0;
    let cost = 0;
    this.spfa(s);

    while (this.dijkstra(s, t)) {
        for (let i = 0; i < this.n; i++) {
            if (this.dist[i] !== this.INF) this.h[i] += this.dist[i];
        }

        let push = this.INF;
        let curr = t;
        while (curr !== s) {
            const p = this.parentNode[curr];
            const idx = this.parentEdge[curr];
            const edge = this.graph[p][idx];
            push = Math.min(push, edge.cap - edge.flow);
            curr = p;
        }

        flow += push;
        curr = t;
        while (curr !== s) {
            const p = this.parentNode[curr];
            const idx = this.parentEdge[curr];
            const edge = this.graph[p][idx];
            edge.flow += push;
            const revIdx = edge.rev;
            this.graph[curr][revIdx].flow -= push;
            cost += push * edge.cost;
            curr = p;
        }
    }
    return [flow, cost];
  }
}

class Solution {
  minCostFlow(n, b, edges) {
    let baseCost = 0;
    const supply = [...b];
    const S = n;
    const T = n + 1;
    const mcmf = new MinCostMaxFlow(n + 2);

    for (const [u, v, low, high, cost] of edges) {
        if (high < low) return null;
        baseCost += low * cost;
        supply[u] -= low;
        supply[v] += low;
        mcmf.addEdge(u, v, high - low, cost);
    }

    let totalSupply = 0;
    for (let i = 0; i < n; i++) {
        if (supply[i] > 0) {
            mcmf.addEdge(S, i, supply[i], 0);
            totalSupply += supply[i];
        } else if (supply[i] < 0) {
            mcmf.addEdge(i, T, -supply[i], 0);
        }
    }

    const [flow, cost] = mcmf.solve(S, T);
    if (flow !== totalSupply) return null;
    return baseCost + cost;
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
  const b = [];
  for (let i = 0; i < n; i++) b.push(parseInt(data[idx++], 10));
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const low = parseInt(data[idx++], 10);
    const high = parseInt(data[idx++], 10);
    const cost = parseInt(data[idx++], 10);
    edges.push([u, v, low, high, cost]);
  }

  const solution = new Solution();
  const ans = solution.minCostFlow(n, b, edges);
  if (ans === null) {
    console.log("INFEASIBLE");
  } else {
    console.log("FEASIBLE");
    console.log(ans);
  }
});
