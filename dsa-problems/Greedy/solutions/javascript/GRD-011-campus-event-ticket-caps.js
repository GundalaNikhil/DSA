const readline = require("readline");

class MinHeap {
  constructor() {
    this.heap = [];
  }
  push(val) {
    this.heap.push(val);
    this._siftUp();
  }
  pop() {
    if (this.size() === 0) return null;
    if (this.size() === 1) return this.heap.pop();
    const min = this.heap[0];
    this.heap[0] = this.heap.pop();
    this._siftDown();
    return min;
  }
  size() {
    return this.heap.length;
  }
  _siftUp() {
    let idx = this.heap.length - 1;
    while (idx > 0) {
      const parentIdx = Math.floor((idx - 1) / 2);
      if (this.heap[idx] >= this.heap[parentIdx]) break;
      [this.heap[idx], this.heap[parentIdx]] = [this.heap[parentIdx], this.heap[idx]];
      idx = parentIdx;
    }
  }
  _siftDown() {
    let idx = 0;
    while (idx < this.heap.length) {
      let minChildIdx = null;
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      if (left < this.heap.length) minChildIdx = left;
      if (right < this.heap.length && this.heap[right] < this.heap[left]) {
        minChildIdx = right;
      }
      if (minChildIdx === null || this.heap[idx] <= this.heap[minChildIdx]) break;
      [this.heap[idx], this.heap[minChildIdx]] = [this.heap[minChildIdx], this.heap[idx]];
      idx = minChildIdx;
    }
  }
}

class Solution {
  maxTickets(n, requests) {
    // Sort by deadline
    requests.sort((a, b) => a[1] - b[1]);
    
    const pq = new MinHeap();
    let total = 0;
    
    for (const [q, d] of requests) {
      pq.push(q);
      total += q;
      
      if (pq.size() > d) {
        total -= pq.pop();
      }
    }
    
    return total;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const n = parseInt(data[ptr++]);
  
  const requests = [];
  for (let i = 0; i < n; i++) {
    const [q, d] = data[ptr++].split(" ").map(Number);
    requests.push([q, d]);
  }

  const solution = new Solution();
  console.log(solution.maxTickets(n, requests));
});
