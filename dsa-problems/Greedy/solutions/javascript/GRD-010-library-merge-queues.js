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
      if (this.heap[idx].val >= this.heap[parentIdx].val) break;
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
      if (right < this.heap.length && this.heap[right].val < this.heap[left].val) {
        minChildIdx = right;
      }
      if (minChildIdx === null || this.heap[idx].val <= this.heap[minChildIdx].val) break;
      [this.heap[idx], this.heap[minChildIdx]] = [this.heap[minChildIdx], this.heap[idx]];
      idx = minChildIdx;
    }
  }
}

class Solution {
  mergeQueues(queues) {
    const pq = new MinHeap();
    const indices = new Array(queues.length).fill(0);
    
    for (let i = 0; i < queues.length; i++) {
      if (queues[i].length > 0) {
        pq.push({ val: queues[i][0], qIdx: i });
      }
    }
    
    const result = [];
    let lastVal = null;
    let count = 0;
    
    while (pq.size() > 0) {
      const best = pq.pop();
      
      if (result.length > 0 && best.val === lastVal && count === 2) {
        // Blocked
        const temp = [best];
        let found = false;
        
        while (pq.size() > 0) {
          const next = pq.pop();
          if (next.val !== lastVal) {
            // Found valid
            result.push(next.val);
            lastVal = next.val;
            count = 1;
            
            indices[next.qIdx]++;
            if (indices[next.qIdx] < queues[next.qIdx].length) {
              pq.push({ val: queues[next.qIdx][indices[next.qIdx]], qIdx: next.qIdx });
            }
            found = true;
            break;
          } else {
            temp.push(next);
          }
        }
        
        // Push back temp
        for (const item of temp) {
          pq.push(item);
        }
        
        if (!found) break; // Deadlock
        
      } else {
        // Valid
        result.push(best.val);
        if (best.val === lastVal) {
          count++;
        } else {
          lastVal = best.val;
          count = 1;
        }
        
        indices[best.qIdx]++;
        if (indices[best.qIdx] < queues[best.qIdx].length) {
          pq.push({ val: queues[best.qIdx][indices[best.qIdx]], qIdx: best.qIdx });
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
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const k = parseInt(data[ptr++]);

  const queues = [];
  for (let i = 0; i < k; i++) {
    const line = data[ptr++].split(" ").map(Number);
    const len = line[0];
    const queue = line.slice(1, len + 1);
    queues.push(queue);
  }

  const solution = new Solution();
  const result = solution.mergeQueues(queues);
  console.log(result.join(" "));
});
