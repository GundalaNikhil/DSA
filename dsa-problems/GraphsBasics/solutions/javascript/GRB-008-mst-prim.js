const readline = require("readline");

class MinPriorityQueue {
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
      this.sinkDown(0);
    }
    return min;
  }
  isEmpty() { return this.heap.length === 0; }
  bubbleUp(idx) {
    const element = this.heap[idx];
    while (idx > 0) {
      let parentIdx = Math.floor((idx - 1) / 2);
      let parent = this.heap[parentIdx];
      if (element.w >= parent.w) break;
      this.heap[parentIdx] = element;
      this.heap[idx] = parent;
      idx = parentIdx;
    }
  }
  sinkDown(idx) {
    const length = this.heap.length;
    const element = this.heap[idx];
    while (true) {
      let leftChildIdx = 2 * idx + 1;
      let rightChildIdx = 2 * idx + 2;
      let swap = null;
      if (leftChildIdx < length) {
        let leftChild = this.heap[leftChildIdx];
        if (leftChild.w < element.w) swap = leftChildIdx;
      }
      if (rightChildIdx < length) {
        let rightChild = this.heap[rightChildIdx];
        if ((swap === null && rightChild.w < element.w) || (swap !== null && rightChild.w < this.heap[swap].w)) {
          swap = rightChildIdx;
        }
      }
      if (swap === null) break;
      this.heap[idx] = this.heap[swap];
      this.heap[swap] = element;
      idx = swap;
    }
  }
}

class Solution {
  mstPrim(n, adj) {
    let mstWeight = 0n;
    const visited = new Int8Array(n).fill(0);
    const pq = new MinPriorityQueue();
    
    pq.push({ w: 0, u: 0 });
    let nodesCount = 0;
    
    while (!pq.isEmpty()) {
      const { w, u } = pq.pop();
      
      if (visited[u]) continue;
      
      visited[u] = 1;
      mstWeight += BigInt(w);
      nodesCount++;
      
      if (nodesCount === n) break;
      
      for (const [v, weight] of adj[u]) {
        if (!visited[v]) {
          pq.push({ w: weight, u: v });
        }
      }
    }
    
    return mstWeight.toString();
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
    const w = parseInt(data[idx++], 10);
    adj[u].push([v, w]);
    adj[v].push([u, w]);
  }

  const solution = new Solution();
  console.log(solution.mstPrim(n, adj));
});
