const readline = require("readline");

// Simple MinPriorityQueue / MaxPriorityQueue polyfill for JS environment
// Or use a sorted array with binary search insertion (O(K) insertion)
// Since K can be large, O(K) is bad.
// However, JS doesn't have built-in Heap or TreeMap.
// For competitive programming in JS without libraries, implementing a Heap is standard.
// Here, we'll implement a basic Heap.

class Heap {
  constructor(compare) {
    this.data = [];
    this.compare = compare; // (a, b) => boolean (true if a should be above b)
  }
  size() { return this.data.length; }
  peek() { return this.data[0]; }
  push(val) {
    this.data.push(val);
    this.bubbleUp(this.data.length - 1);
  }
  pop() {
    const top = this.data[0];
    const bottom = this.data.pop();
    if (this.data.length > 0) {
      this.data[0] = bottom;
      this.bubbleDown(0);
    }
    return top;
  }
  bubbleUp(idx) {
    while (idx > 0) {
      const p = Math.floor((idx - 1) / 2);
      if (this.compare(this.data[idx], this.data[p])) {
        [this.data[idx], this.data[p]] = [this.data[p], this.data[idx]];
        idx = p;
      } else break;
    }
  }
  bubbleDown(idx) {
    while (true) {
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      let swap = idx;
      if (left < this.data.length && this.compare(this.data[left], this.data[swap])) swap = left;
      if (right < this.data.length && this.compare(this.data[right], this.data[swap])) swap = right;
      if (swap !== idx) {
        [this.data[idx], this.data[swap]] = [this.data[swap], this.data[idx]];
        idx = swap;
      } else break;
    }
  }
}

class MedianFinder {
  constructor() {
    this.small = new Heap((a, b) => a > b); // Max Heap
    this.large = new Heap((a, b) => a < b); // Min Heap
    this.delayed = new Map();
    this.smallSize = 0;
    this.largeSize = 0;
  }
  add(val) {
    this.small.push(val);
    const maxSmall = this.small.pop();
    this.large.push(maxSmall);
    this.largeSize++;
    
    if (this.smallSize < this.largeSize) {
      this.small.push(this.large.pop());
      this.largeSize--;
      this.smallSize++;
    }
  }
  remove(val) {
    this.delayed.set(val, (this.delayed.get(val) || 0) + 1);
    const smallTop = this.small.size() > 0 ? this.small.peek() : -Infinity;
    if (val <= smallTop) this.smallSize--;
    else this.largeSize--;
    
    this.prune();
    
    if (this.smallSize < this.largeSize) {
      this.small.push(this.large.pop());
      this.largeSize--;
      this.smallSize++;
    } else if (this.smallSize > this.largeSize + 1) {
      this.large.push(this.small.pop());
      this.smallSize--;
      this.largeSize++;
    }
    this.prune();
  }
  prune() {
    while (this.small.size() > 0 && (this.delayed.get(this.small.peek()) || 0) > 0) {
      const val = this.small.pop();
      this.delayed.set(val, this.delayed.get(val) - 1);
    }
    while (this.large.size() > 0 && (this.delayed.get(this.large.peek()) || 0) > 0) {
      const val = this.large.pop();
      this.delayed.set(val, this.delayed.get(val) - 1);
    }
  }
  getMedian() {
    return this.small.peek();
  }
}

class Solution {
  windowInstability(values, k) {
    const result = [];
    const minD = []; // Indices
    const maxD = []; // Indices
    const mf = new MedianFinder();
    
    for (let i = 0; i < values.length; i++) {
      // Min Deque
      while (minD.length > 0 && minD[0] <= i - k) minD.shift();
      while (minD.length > 0 && values[minD[minD.length - 1]] >= values[i]) minD.pop();
      minD.push(i);
      
      // Max Deque
      while (maxD.length > 0 && maxD[0] <= i - k) maxD.shift();
      while (maxD.length > 0 && values[maxD[maxD.length - 1]] <= values[i]) maxD.pop();
      maxD.push(i);
      
      // Median
      mf.add(values[i]);
      if (i >= k) mf.remove(values[i - k]);
      
      if (i >= k - 1) {
        const minVal = values[minD[0]];
        const maxVal = values[maxD[0]];
        const med = mf.getMedian();
        if (med === 0) result.push(0);
        else result.push(Math.floor((maxVal - minVal) / med));
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
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x !== "")));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const remaining = data.slice(idx);

  let k, values;
  if (remaining.length === n) {
    // Only values, no k -> k = n // 2
    values = remaining.map(x => parseInt(x, 10));
    k = Math.floor(n / 2);
  } else if (remaining.length === n + 1) {
    // First is k, rest are values
    k = parseInt(remaining[0], 10);
    values = remaining.slice(1, n + 1).map(x => parseInt(x, 10));
  } else {
    // Default case: try to parse k and n values
    k = parseInt(remaining[0], 10) || Math.floor(n / 2);
    values = remaining.slice(1, n + 1).map(x => parseInt(x, 10));
  }

  if (values.length === n) {
    const solution = new Solution();
    const result = solution.windowInstability(values, k);
    if (result.length > 0) {
      console.log(result.join(" "));
    }
  }
});
