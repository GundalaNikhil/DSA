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

class DualHeap {
  constructor(k) {
    this.k = k;
    this.small = new PriorityQueue((a, b) => b - a); // Max heap
    this.large = new PriorityQueue((a, b) => a - b); // Min heap
    this.smallCount = 0;
    this.largeCount = 0;
    this.lazy = new Map();
    this.inSmall = new Map();
    this.inLarge = new Map();
  }

  prune(heap) {
    while (!heap.isEmpty()) {
      const val = heap.peek();
      if ((this.lazy.get(val) || 0) > 0) {
        this.lazy.set(val, this.lazy.get(val) - 1);
        heap.pop();
      } else {
        break;
      }
    }
  }

  add(x) {
    if (this.smallCount < this.k) {
      this.small.push(x);
      this.smallCount++;
      this.inSmall.set(x, (this.inSmall.get(x) || 0) + 1);
    } else {
      this.prune(this.small);
      if (this.small.isEmpty()) {
        this.small.push(x);
        this.smallCount++;
        this.inSmall.set(x, (this.inSmall.get(x) || 0) + 1);
      } else {
        const smallMax = this.small.peek();
        if (x <= smallMax) {
          this.small.pop();
          this.inSmall.set(smallMax, this.inSmall.get(smallMax) - 1);
          
          this.small.push(x);
          this.inSmall.set(x, (this.inSmall.get(x) || 0) + 1);
          
          this.large.push(smallMax);
          this.inLarge.set(smallMax, (this.inLarge.get(smallMax) || 0) + 1);
          this.largeCount++;
        } else {
          this.large.push(x);
          this.inLarge.set(x, (this.inLarge.get(x) || 0) + 1);
          this.largeCount++;
        }
      }
    }
    this.balance();
  }

  remove(x) {
    this.lazy.set(x, (this.lazy.get(x) || 0) + 1);
    if ((this.inSmall.get(x) || 0) > 0) {
      this.inSmall.set(x, this.inSmall.get(x) - 1);
      this.smallCount--;
    } else {
      this.inLarge.set(x, (this.inLarge.get(x) || 0) - 1);
      this.largeCount--;
    }
    this.balance();
  }

  balance() {
    this.prune(this.small);
    this.prune(this.large);
    
    while (this.smallCount < this.k && !this.large.isEmpty()) {
      this.prune(this.large);
      if (this.large.isEmpty()) break;
      
      const val = this.large.pop();
      this.inLarge.set(val, this.inLarge.get(val) - 1);
      
      this.small.push(val);
      this.inSmall.set(val, (this.inSmall.get(val) || 0) + 1);
      this.smallCount++;
      this.largeCount--;
      this.prune(this.small);
    }
    
    while (this.smallCount > this.k) {
      this.prune(this.small);
      if (this.small.isEmpty()) break;
      
      const val = this.small.pop();
      this.inSmall.set(val, this.inSmall.get(val) - 1);
      
      this.large.push(val);
      this.inLarge.set(val, (this.inLarge.get(val) || 0) + 1);
      this.smallCount--;
      this.largeCount++;
      this.prune(this.large);
    }
  }

  getKthSmallest() {
    this.prune(this.small);
    if (this.small.isEmpty()) return null;
    return this.small.peek();
  }
}

class Solution {
  kthSmallestInWindows(arr, w, k) {
    const n = arr.length;
    if (w > n) return [];
    
    const dh = new DualHeap(k);
    const result = [];
    
    for (let i = 0; i < w; i++) {
        dh.add(arr[i]);
    }
    const val = dh.getKthSmallest();
    if(val !== null) result.push(val);
    
    for (let i = w; i < n; i++) {
        dh.remove(arr[i - w]);
        dh.add(arr[i]);
        const v = dh.getKthSmallest();
        if(v !== null) result.push(v);
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
