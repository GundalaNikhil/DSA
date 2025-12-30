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
  topKProducts(A, B, k, d) {
    const n = A.length;
    const m = B.length;
    const pq = new PriorityQueue((a, b) => {
      if (a.val > b.val) return -1;
      if (a.val < b.val) return 1;
      return 0;
    });
    const visited = new Set();
    
    const tryAdd = (r, c, dir) => {
      if (r >= 0 && r < n && c >= 0 && c < m) {
        if (Math.abs(r - c) >= d) {
          const key = ``r,`{c}`;
          if (!visited.has(key)) {
            visited.add(key);
            pq.push({ val: BigInt(A[r]) * BigInt(B[c]), r, c, dir });
          }
        }
      }
    };
    
    // TL
    if (d < n) tryAdd(d, 0, 1);
    if (d < m && d > 0) tryAdd(0, d, 1);
    else if (d === 0) tryAdd(0, 0, 1);
    
    // BR
    if (d < n) {
      const startI = n - 1;
      const startJ = Math.min(m - 1, n - 1 - d);
      if (startJ >= 0) tryAdd(startI, startJ, -1);
    }
    if (d < m && d > 0) {
      const startJ = m - 1;
      const startI = Math.min(n - 1, m - 1 - d);
      if (startI >= 0) tryAdd(startI, startJ, -1);
    }
    
    const res = [];
    while (k > 0 && !pq.isEmpty()) {
      const node = pq.pop();
      res.push(node.val.toString());
      k--;
      
      if (node.dir === 1) {
        tryAdd(node.r + 1, node.c, 1);
        tryAdd(node.r, node.c + 1, 1);
      } else {
        tryAdd(node.r - 1, node.c, -1);
        tryAdd(node.r, node.c - 1, -1);
      }
    }
    
    return res;
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
  const k = parseInt(data[idx++]);
  const d = parseInt(data[idx++]);
  const A = [];
  const B = [];
  for (let i = 0; i < n; i++) A.push(parseInt(data[idx++]));
  for (let i = 0; i < m; i++) B.push(parseInt(data[idx++]));
  
  const solution = new Solution();
  const result = solution.topKProducts(A, B, k, d);
  console.log(result.join(" "));
});
