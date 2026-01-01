const readline = require("readline");

// Since JS lacks a built-in TreeMap or Heap, we simulate the logic.
// For O(N log K), we need a Heap.
// We can use the same Heap class from previous problem, but we need to extract top 2.

class MinHeap {
  constructor() {
    this.data = [];
  }
  push(val, idx) {
    this.data.push({ val, idx });
    this.bubbleUp(this.data.length - 1);
  }
  pop() {
    if (this.data.length === 0) return null;
    const top = this.data[0];
    const bottom = this.data.pop();
    if (this.data.length > 0) {
      this.data[0] = bottom;
      this.bubbleDown(0);
    }
    return top;
  }
  peek() {
    return this.data.length > 0 ? this.data[0] : null;
  }
  size() { return this.data.length; }
  
  bubbleUp(idx) {
    while (idx > 0) {
      const p = Math.floor((idx - 1) / 2);
      if (this.data[idx].val < this.data[p].val) {
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
      if (left < this.data.length && this.data[left].val < this.data[swap].val) swap = left;
      if (right < this.data.length && this.data[right].val < this.data[swap].val) swap = right;
      if (swap !== idx) {
        [this.data[idx], this.data[swap]] = [this.data[swap], this.data[idx]];
        idx = swap;
      } else break;
    }
  }
}

class Solution {
  secondMinimums(values, k) {
    if (k === 1) return values;

    const result = [];
    const heap = new MinHeap();

    for (let i = 0; i < values.length; i++) {
      heap.push(values[i], i);

      if (i >= k - 1) {
        // Clean top
        while (heap.peek() && heap.peek().idx <= i - k) {
          heap.pop();
        }

        const first = heap.pop();

        // Clean top again
        while (heap.peek() && heap.peek().idx <= i - k) {
          heap.pop();
        }

        const second = heap.peek();
        if (first && second) {
          result.push(second.val);
          // Push first back
          heap.push(first.val, first.idx);
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
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x !== "")));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const remaining = data.slice(idx);

  let k, values;
  if (remaining.length === n) {
    // Only values, no k -> k = 2 (default)
    values = remaining.map(x => parseInt(x, 10));
    k = 2;
  } else if (remaining.length === n + 1) {
    // First is k, rest are values
    k = parseInt(remaining[0], 10);
    values = remaining.slice(1, n + 1).map(x => parseInt(x, 10));
  } else {
    // Default case: try to parse k and n values
    k = parseInt(remaining[0], 10) || 2;
    values = remaining.slice(1, n + 1).map(x => parseInt(x, 10));
  }

  const solution = new Solution();
  const result = solution.secondMinimums(values, k);
  console.log(result.join(" "));
});
