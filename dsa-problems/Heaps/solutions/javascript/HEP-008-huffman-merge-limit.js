const readline = require("readline");

class PriorityQueue {
  constructor(compare = (a, b) => a - b) {
    this.heap = [];
    this.compare = compare;
  }
  size() { return this.heap.length; }
  isEmpty() { return this.heap.length === 0; }
  peek() { return this.heap[0]; }
  push(val) {
    this.heap.push(val);
    this.bubbleUp(this.heap.length - 1);
  }
  pop() {
    if (this.size() === 0) return null;
    const top = this.heap[0];
    const bottom = this.heap.pop();
    if (this.size() > 0) {
      this.heap[0] = bottom;
      this.bubbleDown(0);
    }
    return top;
  }
  bubbleUp(idx) {
    while (idx > 0) {
      const pIdx = Math.floor((idx - 1) / 2);
      if (this.compare(this.heap[idx], this.heap[pIdx]) < 0) {
        [this.heap[idx], this.heap[pIdx]] = [this.heap[pIdx], this.heap[idx]];
        idx = pIdx;
      } else break;
    }
  }
  bubbleDown(idx) {
    while (true) {
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      let swap = null;
      if (left < this.size() && this.compare(this.heap[left], this.heap[idx]) < 0) swap = left;
      if (right < this.size() && this.compare(this.heap[right], swap === null ? this.heap[idx] : this.heap[swap]) < 0) swap = right;
      if (swap === null) break;
      [this.heap[idx], this.heap[swap]] = [this.heap[swap], this.heap[idx]];
      idx = swap;
    }
  }
}

class Solution {
  huffmanCost(freq, m) {
    const pq = new PriorityQueue((a, b) => {
      if (a < b) return -1;
      if (a > b) return 1;
      return 0;
    });
    
    for (const f of freq) {
      pq.push(BigInt(f));
    }
    
    while ((pq.size() - 1) % (m - 1) !== 0) {
      pq.push(0n);
    }
    
    let totalCost = 0n;
    
    while (pq.size() > 1) {
      let sum = 0n;
      for (let i = 0; i < m; i++) {
        sum += pq.pop();
      }
      totalCost += sum;
      pq.push(sum);
    }
    
    return totalCost.toString();
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
  const n = parseInt(data[idx++]);
  const m = parseInt(data[idx++]);
  const freq = [];
  for (let i = 0; i < n; i++) {
    freq.push(parseInt(data[idx++]));
  }
  
  const solution = new Solution();
  console.log(solution.huffmanCost(freq, m));
});
