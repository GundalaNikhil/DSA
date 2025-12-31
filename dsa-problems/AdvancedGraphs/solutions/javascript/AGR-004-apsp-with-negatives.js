const readline = require("readline");

class PriorityQueue {
  constructor(comparator = (a, b) => a - b) {
    this.heap = [];
    this.comparator = comparator;
  }
  push(val) {
    this.heap.push(val);
    this.bubbleUp(this.heap.length - 1);
  }
  pop() {
    if (this.heap.length === 0) return null;
    const top = this.heap[0];
    const bottom = this.heap.pop();
    if (this.heap.length > 0) {
      this.heap[0] = bottom;
      this.bubbleDown(0);
    }
    return top;
  }
  isEmpty() { return this.heap.length === 0; }
  bubbleUp(idx) {
    while (idx > 0) {
      const pIdx = Math.floor((idx - 1) / 2);
      if (this.comparator(this.heap[idx], this.heap[pIdx]) < 0) {
        [this.heap[idx], this.heap[pIdx]] = [this.heap[pIdx], this.heap[idx]];
        idx = pIdx;
      } else break;
    }
  }
  bubbleDown(idx) {
    while (true) {
      const lIdx = 2 * idx + 1;
      const rIdx = 2 * idx + 2;
      let swapIdx = null;
      if (lIdx < this.heap.length && this.comparator(this.heap[lIdx], this.heap[idx]) < 0) swapIdx = lIdx;
      if (rIdx < this.heap.length && this.comparator(this.heap[rIdx], swapIdx === null ? this.heap[idx] : this.heap[swapIdx]) < 0) swapIdx = rIdx;
      if (swapIdx !== null) {
        [this.heap[idx], this.heap[swapIdx]] = [this.heap[swapIdx], this.heap[idx]];
        idx = swapIdx;
      } else break;
    }
  }
}

class Solution {
  allPairsShortestPaths(n, edges) {
    const INF = 1e15;
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
      adj[u].push({ to: v, w });
    }

    // 1. Bellman-Ford
    const h = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
      let changed = false;
      for (const [u, v, w] of edges) {
        if (h[u] + w < h[v]) {
          h[v] = h[u] + w;
          changed = true;
        }
      }
      if (!changed) break;
    }

    const result = Array.from({ length: n }, () => new Array(n).fill(INF));

    // 2. Dijkstra
    for (let s = 0; s < n; s++) {
      const d = new Array(n).fill(INF);
      d[s] = 0;
      const pq = new PriorityQueue((a, b) => a.dist - b.dist);
      pq.push({ dist: 0, u: s });

      while (!pq.isEmpty()) {
        const { dist: distU, u } = pq.pop();
        if (distU > d[u]) continue;

        for (const { to: v, w } of adj[u]) {
          const newW = w + h[u] - h[v];
          if (d[u] + newW < d[v]) {
            d[v] = d[u] + newW;
            pq.push({ dist: d[v], u: v });
          }
        }
      }

      for (let v = 0; v < n; v++) {
        if (d[v] !== INF) {
          result[s][v] = d[v] - h[s] + h[v];
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
  const dist = solution.allPairsShortestPaths(n, edges);
  const INF = 1e15;
  const out = dist.map((row) => row.map(x => x >= INF / 2 ? "INF" : x).join(" "));
  console.log(out.join("\n"));
});
