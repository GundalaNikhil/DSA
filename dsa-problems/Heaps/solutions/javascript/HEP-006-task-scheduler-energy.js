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
  maxTasks(E, duration, gain) {
    const positive = [];
    const negative = [];
    
    for (let i = 0; i < duration.length; i++) {
      if (gain[i] >= duration[i]) {
        positive.push({ d: duration[i], g: gain[i] });
      } else {
        negative.push({ d: duration[i], g: gain[i] });
      }
    }
    
    positive.sort((a, b) => a.d - b.d);
    
    let count = 0;
    let currentE = BigInt(E);
    
    for (const t of positive) {
      if (currentE >= BigInt(t.d)) {
        currentE += BigInt(t.g - t.d);
        count++;
      } else {
        break;
      }
    }
    
    const peakE = currentE;

    negative.sort((a, b) => b.g - a.g);
    
    // Max heap for losses
    const pq = new PriorityQueue((a, b) => b - a);
    let currentLossSum = 0n;
    
    for (const t of negative) {
      const loss = BigInt(t.d - t.g);
      currentLossSum += loss;
      pq.push(Number(loss));
      if (currentLossSum + BigInt(t.g) > peakE) {
        currentLossSum -= BigInt(pq.pop());
      }
    }
    
    return count + pq.size();
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
  const E = parseInt(data[idx++]);
  const duration = [];
  const gain = [];
  for (let i = 0; i < n; i++) {
    duration.push(parseInt(data[idx++]));
    gain.push(parseInt(data[idx++]));
  }
  
  const solution = new Solution();
  console.log(solution.maxTasks(E, duration, gain));
});
