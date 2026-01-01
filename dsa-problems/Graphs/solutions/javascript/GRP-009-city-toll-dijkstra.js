class MinHeap {
  constructor() {
    this.heap = [];
  }
  
  push(val) {
    this.heap.push(val);
    this.bubbleUp(this.heap.length - 1);
  }
  
  pop() {
    if (this.heap.length === 0) return null;
    const min = this.heap[0];
    const end = this.heap.pop();
    if (this.heap.length > 0) {
      this.heap[0] = end;
      this.bubbleDown(0);
    }
    return min;
  }
  
  bubbleUp(idx) {
    while (idx > 0) {
      const parent = Math.floor((idx - 1) / 2);
      if (this.heap[parent][0] <= this.heap[idx][0]) break;
      [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
      idx = parent;
    }
  }
  
  bubbleDown(idx) {
    while (true) {
      let smallest = idx;
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      
      if (left < this.heap.length && this.heap[left][0] < this.heap[smallest][0]) {
        smallest = left;
      }
      if (right < this.heap.length && this.heap[right][0] < this.heap[smallest][0]) {
        smallest = right;
      }
      if (smallest === idx) break;
      
      [this.heap[idx], this.heap[smallest]] = [this.heap[smallest], this.heap[idx]];
      idx = smallest;
    }
  }
  
  isEmpty() {
    return this.heap.length === 0;
  }
}

class Solution {
  dijkstra(n, adj, source) {
    const dist = new Array(n).fill(Infinity);
    dist[source] = 0;
    const pq = new MinHeap();
    pq.push([0, source]);
    
    while (!pq.isEmpty()) {
      const [d, node] = pq.pop();
      
      if (d > dist[node]) continue;
      adj[node].sort((a, b) => (a[1] - b[1]) || (a[0] - b[0]));
      for (const [neighbor, weight] of adj[node]) {
        const newDist = dist[node] + weight;
        if (newDist < dist[neighbor]) {
          dist[neighbor] = newDist;
          pq.push([newDist, neighbor]);
        }
      }
    }
    
    return dist.map((d) => (d === Infinity ? -1 : d));
  }
}

const fs = require('fs');

const data = fs.readFileSync(0, 'utf8').trim().split(/\s+/);
if (data.length > 0) {
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const w = parseInt(data[idx++], 10);
    adj[u].push([v, w]);
  }
  const source = idx < data.length ? parseInt(data[idx++], 10) : 0;
  const sol = new Solution();
  const result = sol.dijkstra(n, adj, source);
  console.log(result.join(' '));
}
