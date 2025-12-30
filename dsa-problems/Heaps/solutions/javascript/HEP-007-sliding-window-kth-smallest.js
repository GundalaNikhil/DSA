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
  kthSmallestInWindows(arr, w, k) {
    const n = arr.length;
    const result = [];
    
    // Max-Heap (Left)
    const left = new PriorityQueue((a, b) => b - a);
    // Min-Heap (Right)
    const right = new PriorityQueue((a, b) => a - b);
    
    const deleted = new Map();
    let leftSize = 0;
    let rightSize = 0;
    
    const clean = (pq) => {
      while (!pq.isEmpty()) {
        const val = pq.peek();
        if (deleted.has(val) && deleted.get(val) > 0) {
          pq.pop();
          deleted.set(val, deleted.get(val) - 1);
          if (deleted.get(val) === 0) deleted.delete(val);
        } else {
          break;
        }
      }
    };
    
    for (let i = 0; i < n; i++) {
      const val = arr[i];
      
      // ADD
      clean(left);
      if (left.isEmpty() || val <= left.peek()) {
        left.push(val);
        leftSize++;
      } else {
        right.push(val);
        rightSize++;
      }
      
      // REMOVE
      if (i >= w) {
        const out = arr[i - w];
        deleted.set(out, (deleted.get(out) || 0) + 1);
        
        clean(left);
        if (!left.isEmpty() && out <= left.peek()) {
          leftSize--;
        } else {
          rightSize--;
        }
      }
      
      // REBALANCE
      while (leftSize < k) {
        clean(right);
        if (right.isEmpty()) break;
        const v = right.pop();
        left.push(v);
        leftSize++;
        rightSize--;
      }
      
      while (leftSize > k) {
        clean(left);
        if (left.isEmpty()) break;
        const v = left.pop();
        right.push(v);
        leftSize--;
        rightSize++;
      }
      
      while (true) {
        clean(left);
        clean(right);
        if (left.isEmpty() || right.isEmpty()) break;
        if (left.peek() > right.peek()) {
          const l = left.pop();
          const r = right.pop();
          left.push(r);
          right.push(l);
        } else {
          break;
        }
      }
      
      if (i >= w - 1) {
        clean(left);
        result.push(left.peek());
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
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++]);
  const w = parseInt(data[idx++]);
  const k = parseInt(data[idx++]);
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(parseInt(data[idx++]));
  }
  
  const solution = new Solution();
  const result = solution.kthSmallestInWindows(arr, w, k);
  console.log(result.join(" "));
});
