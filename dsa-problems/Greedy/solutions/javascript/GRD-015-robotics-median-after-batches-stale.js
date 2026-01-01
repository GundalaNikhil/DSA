const readline = require("readline");

class MinHeap {
  constructor() { this.heap = []; }
  push(val) { this.heap.push(val); this._siftUp(); }
  pop() {
    if (this.size() === 0) return null;
    if (this.size() === 1) return this.heap.pop();
    const top = this.heap[0];
    this.heap[0] = this.heap.pop();
    this._siftDown();
    return top;
  }
  peek() { return this.size() === 0 ? null : this.heap[0]; }
  size() { return this.heap.length; }
  _siftUp() {
    let idx = this.heap.length - 1;
    while (idx > 0) {
      const p = Math.floor((idx - 1) / 2);
      if (this.heap[idx] >= this.heap[p]) break;
      [this.heap[idx], this.heap[p]] = [this.heap[p], this.heap[idx]];
      idx = p;
    }
  }
  _siftDown() {
    let idx = 0;
    while (idx < this.heap.length) {
      let min = idx;
      const l = 2*idx+1, r = 2*idx+2;
      if (l < this.heap.length && this.heap[l] < this.heap[min]) min = l;
      if (r < this.heap.length && this.heap[r] < this.heap[min]) min = r;
      if (min === idx) break;
      [this.heap[idx], this.heap[min]] = [this.heap[min], this.heap[idx]];
      idx = min;
    }
  }
}

class MaxHeap {
  constructor() { this.heap = []; }
  push(val) { this.heap.push(val); this._siftUp(); }
  pop() {
    if (this.size() === 0) return null;
    if (this.size() === 1) return this.heap.pop();
    const top = this.heap[0];
    this.heap[0] = this.heap.pop();
    this._siftDown();
    return top;
  }
  peek() { return this.size() === 0 ? null : this.heap[0]; }
  size() { return this.heap.length; }
  _siftUp() {
    let idx = this.heap.length - 1;
    while (idx > 0) {
      const p = Math.floor((idx - 1) / 2);
      if (this.heap[idx] <= this.heap[p]) break;
      [this.heap[idx], this.heap[p]] = [this.heap[p], this.heap[idx]];
      idx = p;
    }
  }
  _siftDown() {
    let idx = 0;
    while (idx < this.heap.length) {
      let max = idx;
      const l = 2*idx+1, r = 2*idx+2;
      if (l < this.heap.length && this.heap[l] > this.heap[max]) max = l;
      if (r < this.heap.length && this.heap[r] > this.heap[max]) max = r;
      if (max === idx) break;
      [this.heap[idx], this.heap[max]] = [this.heap[max], this.heap[idx]];
      idx = max;
    }
  }
}

class Solution {
  medianAfterBatches(k, t, batches) {
    const lower = new MaxHeap();
    const upper = new MinHeap();
    const freq = new Map();
    const location = new Map(); // val -> [lowerCnt, upperCnt]
    
    let validLower = 0;
    let validUpper = 0;
    const results = [];
    
    for (const batch of batches) {
      for (const x of batch) {
        freq.set(x, (freq.get(x) || 0) + 1);
        const f = freq.get(x);
        
        if (f > t + 1) continue;
        
        if (f === t + 1) {
          const loc = location.get(x);
          if (loc) {
            validLower -= loc[0];
            validUpper -= loc[1];
          }
          continue;
        }
        
        if (lower.size() === 0 || x <= lower.peek()) {
          lower.push(x);
          if (!location.has(x)) location.set(x, [0, 0]);
          location.get(x)[0]++;
          validLower++;
        } else {
          upper.push(x);
          if (!location.has(x)) location.set(x, [0, 0]);
          location.get(x)[1]++;
          validUpper++;
        }
      }
      
      while (true) {
        while (lower.size() > 0 && (freq.get(lower.peek()) || 0) > t) lower.pop();
        while (upper.size() > 0 && (freq.get(upper.peek()) || 0) > t) upper.pop();
        
        if (validLower > validUpper + 1) {
          const val = lower.pop();
          location.get(val)[0]--;
          location.get(val)[1]++;
          upper.push(val);
          validLower--;
          validUpper++;
        } else if (validUpper > validLower) {
          const val = upper.pop();
          location.get(val)[1]--;
          location.get(val)[0]++;
          lower.push(val);
          validUpper--;
          validLower++;
        } else {
          break;
        }
      }
      
      if (validLower + validUpper === 0) {
        results.push("NA");
      } else {
        const median =
          (validLower + validUpper) % 2 === 1
            ? lower.peek()
            : Math.floor((lower.peek() + upper.peek()) / 2);
        results.push(median.toString());
      }
    }
    
    return results;
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

  // Flatten all input like Python does
  const allNumbers = [];
  for (const line of data) {
    allNumbers.push(...line.split(" ").map(Number));
  }

  let ptr = 0;
  const k = allNumbers[ptr++];
  const t = allNumbers[ptr++];

  const batches = [];
  for (let i = 0; i < k; i++) {
    const m = allNumbers[ptr++];
    const batch = [];
    for (let j = 0; j < m; j++) {
      batch.push(allNumbers[ptr++]);
    }
    batches.push(batch);
  }

  const solution = new Solution();
  const result = solution.medianAfterBatches(k, t, batches);
  console.log(result.join(" "));
});
