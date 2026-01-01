const readline = require("readline");

class MaxHeap {
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
    const max = this.heap[0];
    this.heap[0] = this.heap.pop();
    this._siftDown();
    return max;
  }
  size() {
    return this.heap.length;
  }
  _compare(a, b) {
    // Compare by quality first (max), then by weight if tied (min)
    if (a.q !== b.q) return a.q > b.q ? 1 : -1;
    return a.w < b.w ? 1 : -1;
  }
  _siftUp() {
    let idx = this.heap.length - 1;
    while (idx > 0) {
      const parentIdx = Math.floor((idx - 1) / 2);
      if (this._compare(this.heap[idx], this.heap[parentIdx]) <= 0) break;
      [this.heap[idx], this.heap[parentIdx]] = [this.heap[parentIdx], this.heap[idx]];
      idx = parentIdx;
    }
  }
  _siftDown() {
    let idx = 0;
    while (idx < this.heap.length) {
      let maxChildIdx = null;
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      if (left < this.heap.length) maxChildIdx = left;
      if (right < this.heap.length && this._compare(this.heap[right], this.heap[left]) > 0) {
        maxChildIdx = right;
      }
      if (maxChildIdx === null || this._compare(this.heap[idx], this.heap[maxChildIdx]) >= 0) break;
      [this.heap[idx], this.heap[maxChildIdx]] = [this.heap[maxChildIdx], this.heap[idx]];
      idx = maxChildIdx;
    }
  }
}

class Solution {
  maxBundleWeight(n, T, weights, qualities) {
    const pq = new MaxHeap();
    
    for (let i = 0; i < n; i++) {
      pq.push({ w: weights[i], q: qualities[i] });
    }
    
    while (pq.size() > 1) {
      const p1 = pq.pop();
      const p2 = pq.pop();
      
      const newQ = Math.min(p1.q, p2.q) - 1;
      
      if (newQ < T) {
        return -1;
      }
      
      const minW = Math.min(p1.w, p2.w);
      const loss = Math.floor(0.1 * minW);
      const newW = p1.w + p2.w - loss;
      
      pq.push({ w: newW, q: newQ });
    }
    
    return pq.size() === 1 ? pq.pop().w : -1;
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
  const [n, T] = data[ptr++].split(" ").map(Number);
  const weights = data[ptr++].split(" ").map(Number);
  const qualities = data[ptr++].split(" ").map(Number);

  const solution = new Solution();
  console.log(solution.maxBundleWeight(n, T, weights, qualities));
});
