const readline = require("readline");

class PriorityQueue {
  constructor(compare = (a, b) => a - b) {
    this.heap = [];
    this.compare = compare;
  }
  size() { return this.heap.length; }
  isEmpty() { return this.heap.length === 0; }
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
  mergeStreams(streams, r) {
    const k = streams.length;
    const indices = new Array(k).fill(0);
    const usage = new Array(k).fill(0);
    
    // Min heap: {val, idx}
    const pq = new PriorityQueue((a, b) => {
        if (a.val < b.val) return -1;
        if (a.val > b.val) return 1;
        // Break ties by index for deterministic output matching Python
        return a.idx - b.idx;
    });
    
    for (let i = 0; i < k; i++) {
      if (streams[i].length > 0) {
        pq.push({ val: streams[i][0], idx: i });
        indices[i]++;
      }
    }
    
    const result = [];
    let blocked = [];
    
    while (!pq.isEmpty()) {
      const { val, idx } = pq.pop();
      result.push(val);
      
      usage[idx]++;
      
      if (usage[idx] < r) {
        if (indices[idx] < streams[idx].length) {
          pq.push({ val: streams[idx][indices[idx]], idx: idx });
          indices[idx]++;
        }
      } else {
        blocked.push(idx);
      }
      
      if (pq.isEmpty() && blocked.length > 0) {
        for (const bIdx of blocked) {
          usage[bIdx] = 0;
          if (indices[bIdx] < streams[bIdx].length) {
            pq.push({ val: streams[bIdx][indices[bIdx]], idx: bIdx });
            indices[bIdx]++;
          }
        }
        blocked = [];
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
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part !== "") data.push(part);
  }
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const k = parseInt(data[idx++]);
  const r = parseInt(data[idx++]);
  const streams = [];
  for (let i = 0; i < k; i++) {
    const m = parseInt(data[idx++]);
    const stream = [];
    for (let j = 0; j < m; j++) {
      stream.push(BigInt(data[idx++]));
    }
    streams.push(stream);
  }
  
  const solution = new Solution();
  const result = solution.mergeStreams(streams, r);
  console.log(result.join(" "));
});
