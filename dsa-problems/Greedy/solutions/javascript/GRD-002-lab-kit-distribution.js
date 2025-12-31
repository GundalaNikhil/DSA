const readline = require("readline");

// Simple MaxHeap implementation for JS since it doesn't have a built-in one
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
  
  _siftUp() {
    let nodeIdx = this.heap.length - 1;
    while (nodeIdx > 0) {
      const parentIdx = Math.floor((nodeIdx - 1) / 2);
      if (this.heap[nodeIdx] <= this.heap[parentIdx]) break;
      [this.heap[nodeIdx], this.heap[parentIdx]] = [this.heap[parentIdx], this.heap[nodeIdx]];
      nodeIdx = parentIdx;
    }
  }
  
  _siftDown() {
    let nodeIdx = 0;
    while (nodeIdx < this.heap.length) {
      let maxChildIdx = null;
      const leftChildIdx = 2 * nodeIdx + 1;
      const rightChildIdx = 2 * nodeIdx + 2;
      
      if (leftChildIdx < this.heap.length) maxChildIdx = leftChildIdx;
      if (rightChildIdx < this.heap.length && this.heap[rightChildIdx] > this.heap[leftChildIdx]) {
        maxChildIdx = rightChildIdx;
      }
      
      if (maxChildIdx === null || this.heap[nodeIdx] >= this.heap[maxChildIdx]) break;
      
      [this.heap[nodeIdx], this.heap[maxChildIdx]] = [this.heap[maxChildIdx], this.heap[nodeIdx]];
      nodeIdx = maxChildIdx;
    }
  }
}

class Solution {
  distributeKits(k, m, quantities) {
    const pq = new MaxHeap();
    let totalKits = 0;
    
    for (const q of quantities) {
      if (q > 0) {
        pq.push(q);
        totalKits += q;
      }
    }
    
    const fulfilled = Math.min(m, totalKits);
    let toDistribute = fulfilled;
    
    while (toDistribute > 0 && pq.size() > 0) {
      let maxQ = pq.pop();
      maxQ--;
      toDistribute--;
      
      if (maxQ > 0) {
        pq.push(maxQ);
      }
    }
    
    const remainingTypes = pq.size();
    const zeroedTypes = k - remainingTypes;
    
    return [fulfilled, zeroedTypes];
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
  const [k, m] = data[ptr++].split(" ").map(Number);
  const quantities = data[ptr++].split(" ").map(Number);

  const solution = new Solution();
  const [fulfilled, zeroed] = solution.distributeKits(k, m, quantities);
  console.log(``fulfilled`{zeroed}`);
});
