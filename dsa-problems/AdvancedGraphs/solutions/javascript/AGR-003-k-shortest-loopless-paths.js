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
  kShortestPaths(n, adj, s, t, k) {
    const INF = 1e15;

    const getShortestPath = (start, end, forbiddenNodes, forbiddenEdges) => {
      const dist = new Array(n).fill(INF);
      const parent = new Array(n).fill(-1);
      dist[start] = 0;
      
      const pq = new PriorityQueue((a, b) => a.d - b.d);
      pq.push({ d: 0, u: start });

      while (!pq.isEmpty()) {
        const { d, u } = pq.pop();
        if (d > dist[u]) continue;
        if (u === end) break;

        for (const [v, w] of adj[u]) {
          if (forbiddenNodes.has(v)) continue;
          if (forbiddenEdges.has(`${u},${v}`)) continue;

          if (dist[u] + w < dist[v]) {
            dist[v] = dist[u] + w;
            parent[v] = u;
            pq.push({ d: dist[v], u: v });
          }
        }
      }

      if (dist[end] === INF) return null;

      const path = [];
      let curr = end;
      while (curr !== -1) {
        path.push(curr);
        curr = parent[curr];
      }
      path.reverse();
      return { nodes: path, cost: dist[end] };
    };

    const A = [];
    const B = new PriorityQueue((a, b) => a.cost - b.cost);
    const B_set = new Set(); // To avoid duplicates in B

    const p0 = getShortestPath(s, t, new Set(), new Set());
    if (!p0) return [];
    A.push(p0);

    for (let i = 1; i < k; i++) {
      const prevPath = A[A.length - 1];

      for (let j = 0; j < prevPath.nodes.length - 1; j++) {
        const spurNode = prevPath.nodes[j];
        const rootPathNodes = prevPath.nodes.slice(0, j + 1);
        
        let rootCost = 0;
        for (let x = 0; x < j; x++) {
          const u = prevPath.nodes[x];
          const v = prevPath.nodes[x + 1];
          for (const [neighbor, w] of adj[u]) {
            if (neighbor === v) { rootCost += w; break; }
          }
        }

        const forbiddenNodes = new Set(rootPathNodes);
        forbiddenNodes.delete(spurNode);

        const forbiddenEdges = new Set();
        for (const p of A) {
          if (p.nodes.length > j && 
              p.nodes.slice(0, j + 1).every((val, idx) => val === rootPathNodes[idx])) {
forbiddenEdges.add(`${p.nodes[j]},${p.nodes[j+1]}`);
          }
        }

        const spurPath = getShortestPath(spurNode, t, forbiddenNodes, forbiddenEdges);

        if (spurPath) {
          const totalNodes = rootPathNodes.slice(0, -1).concat(spurPath.nodes);
          const totalCost = rootCost + spurPath.cost;
          const totalPathStr = JSON.stringify(totalNodes);

          if (!B_set.has(totalPathStr)) {
            B.push({ nodes: totalNodes, cost: totalCost, str: totalPathStr });
            B_set.add(totalPathStr);
          }
        }
      }

      if (B.isEmpty()) break;
      
      // Extract best unique path
      // B can contain paths already in A.
      // No, because we forbid edges used in A.
      // But we should check just in case logic is loose.
      // Standard Yen guarantees new paths.
      
      const best = B.pop();
      A.push(best);
    }

    return A.map(p => p.cost);
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
  const k = parseInt(data[idx++], 10);
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const w = parseInt(data[idx++], 10);
    if (u >= n || u < 0) { console.error(`Error: u=${u} n=${n} idx=${idx-3} len=${data.length}`); }
    if (!adj[u]) { console.error(`Error: adj[${u}] undefined. n=${n}`); }
    adj[u].push([v, w]);
  }

  const solution = new Solution();
  const paths = solution.kShortestPaths(n, adj, s, t, k);
  console.log(paths.length.toString());
  console.log(paths.join(" "));
});
