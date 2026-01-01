const readline = require("readline");

class MinPriorityQueue {
  constructor() {
    this.heap = [];
  }
  
  push(val) {
    this.heap.push(val);
    this._bubbleUp(this.heap.length - 1);
  }
  
  pop() {
    if (this.heap.length === 0) return null;
    const top = this.heap[0];
    const bottom = this.heap.pop();
    if (this.heap.length > 0) {
      this.heap[0] = bottom;
      this._bubbleDown(0);
    }
    return top;
  }
  
  isEmpty() {
    return this.heap.length === 0;
  }
  
  _bubbleUp(idx) {
    while (idx > 0) {
      const parentIdx = Math.floor((idx - 1) / 2);
      if (this.heap[idx][0] >= this.heap[parentIdx][0]) break;
      [this.heap[idx], this.heap[parentIdx]] = [this.heap[parentIdx], this.heap[idx]];
      idx = parentIdx;
    }
  }
  
  _bubbleDown(idx) {
    while (true) {
      let leftIdx = 2 * idx + 1;
      let rightIdx = 2 * idx + 2;
      let smallest = idx;
      
      if (leftIdx < this.heap.length && this.heap[leftIdx][0] < this.heap[smallest][0]) {
        smallest = leftIdx;
      }
      if (rightIdx < this.heap.length && this.heap[rightIdx][0] < this.heap[smallest][0]) {
        smallest = rightIdx;
      }
      if (smallest === idx) break;
      [this.heap[idx], this.heap[smallest]] = [this.heap[smallest], this.heap[idx]];
      idx = smallest;
    }
  }
}

class Solution {
  shortestPathWithBattery(n, edges, source, dest, battery) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
      adj[u].push([v, w]);
      adj[v].push([u, w]);
    }
    
    const dist = new Int32Array(n).fill(2147483647); // Max int
    dist[source] = 0;
    
    const pq = new MinPriorityQueue();
    pq.push([0, source]);
    
    while (!pq.isEmpty()) {
      const [d, u] = pq.pop();
      
      if (d > dist[u]) continue;
      if (u === dest) return d;
      
      for (const [v, w] of adj[u]) {
        if (w <= battery) {
          if (dist[u] + w < dist[v]) {
            dist[v] = dist[u] + w;
            pq.push([dist[v], v]);
          }
        }
      }
    }
    
    return dist[dest] === 2147483647 ? -1 : dist[dest];
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

  let ptr = 0;
  const n = parseInt(data[ptr++], 10);
  const m = parseInt(data[ptr++], 10);

  const edges = [];
  for (let i = 0; i < m; i++) {
    if (ptr + 2 >= data.length) return; // Not enough data
    const u = parseInt(data[ptr++], 10);
    const v = parseInt(data[ptr++], 10);
    const w = parseInt(data[ptr++], 10);
    edges.push([u, v, w]);
  }

  // Check if we have source, dest, battery parameters
  if (ptr + 2 >= data.length) return; // Incomplete input

  const source = parseInt(data[ptr++], 10);
  const dest = parseInt(data[ptr++], 10);
  const battery = parseInt(data[ptr++], 10);

  const solution = new Solution();
  console.log(solution.shortestPathWithBattery(n, edges, source, dest, battery));
});
