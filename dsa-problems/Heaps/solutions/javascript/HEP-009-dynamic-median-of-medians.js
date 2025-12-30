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

class Group {
  constructor() {
    this.left = new PriorityQueue((a, b) => b - a);
    this.right = new PriorityQueue((a, b) => a - b);
  }
  add(val) {
    if (this.left.isEmpty() || val <= this.left.peek()) {
      this.left.push(val);
    } else {
      this.right.push(val);
    }
    this.rebalance();
  }
  rebalance() {
    while (this.left.size() > this.right.size() + 1) {
      this.right.push(this.left.pop());
    }
    while (this.right.size() > this.left.size()) {
      this.left.push(this.right.pop());
    }
  }
  getMedian() {
    if (this.left.isEmpty()) return 0;
    return this.left.peek();
  }
  size() { return this.left.size() + this.right.size(); }
  getAll() {
    // Destructive get for merging
    const res = [];
    while (!this.left.isEmpty()) res.push(this.left.pop());
    while (!this.right.isEmpty()) res.push(this.right.pop());
    return res;
  }
}

class Solution {
  processOperations(operations) {
    const groups = new Map();
    const gLeft = new PriorityQueue((a, b) => b - a);
    const gRight = new PriorityQueue((a, b) => a - b);
    const gDeleted = new Map();
    let gLeftSize = 0;
    let gRightSize = 0;
    
    const cleanGlobal = () => {
      while (!gLeft.isEmpty() && (gDeleted.get(gLeft.peek()) || 0) > 0) {
        const val = gLeft.pop();
        gDeleted.set(val, gDeleted.get(val) - 1);
      }
      while (!gRight.isEmpty() && (gDeleted.get(gRight.peek()) || 0) > 0) {
        const val = gRight.pop();
        gDeleted.set(val, gDeleted.get(val) - 1);
      }
    };
    
    const rebalanceGlobal = () => {
      cleanGlobal();
      while (gLeftSize > gRightSize + 1) {
        gRight.push(gLeft.pop());
        gLeftSize--;
        gRightSize++;
        cleanGlobal();
      }
      while (gRightSize > gLeftSize) {
        gLeft.push(gRight.pop());
        gLeftSize++;
        gRightSize--;
        cleanGlobal();
      }
    };
    
    const addToGlobal = (val) => {
      cleanGlobal();
      if (gLeft.isEmpty() || val <= gLeft.peek()) {
        gLeft.push(val);
        gLeftSize++;
      } else {
        gRight.push(val);
        gRightSize++;
      }
      rebalanceGlobal();
    };
    
    const removeFromGlobal = (val) => {
      gDeleted.set(val, (gDeleted.get(val) || 0) + 1);
      cleanGlobal();
      if (!gLeft.isEmpty() && val <= gLeft.peek()) {
        gLeftSize--;
      } else {
        gRightSize--;
      }
      rebalanceGlobal();
    };
    
    const results = [];
    
    for (const op of operations) {
      const type = op[0];
      if (type === "NEW") {
        const gid = op[1];
        const g = new Group();
        for (let i = 2; i < op.length; i++) g.add(parseInt(op[i]));
        groups.set(gid, g);
        addToGlobal(g.getMedian());
      } else if (type === "ADD") {
        const gid = op[1];
        const x = parseInt(op[2]);
        if (groups.has(gid)) {
          const g = groups.get(gid);
          removeFromGlobal(g.getMedian());
          g.add(x);
          addToGlobal(g.getMedian());
        }
      } else if (type === "MERGE") {
        const gid1 = op[1];
        const gid2 = op[2];
        if (groups.has(gid1) && groups.has(gid2)) {
          let g1 = groups.get(gid1);
          let g2 = groups.get(gid2);
          removeFromGlobal(g1.getMedian());
          removeFromGlobal(g2.getMedian());
          
          if (g1.size() < g2.size()) {
            const elems = g1.getAll();
            for (const x of elems) g2.add(x);
            groups.set(gid1, g2);
          } else {
            const elems = g2.getAll();
            for (const x of elems) g1.add(x);
          }
          groups.delete(gid2);
          addToGlobal(groups.get(gid1).getMedian());
        }
      } else if (type === "QUERY") {
        cleanGlobal();
        if (gLeftSize === 0) results.push("EMPTY");
        else results.push(gLeft.peek().toString());
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
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const q = parseInt(data[idx++]);
  const operations = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++];
    if (type === "NEW") {
      const gid = data[idx++];
      const m = parseInt(data[idx++]);
      const vals = [];
      for (let j = 0; j < m; j++) vals.push(data[idx++]);
      operations.push([type, gid, ...vals]);
    } else if (type === "ADD") {
      const gid = data[idx++];
      const x = data[idx++];
      operations.push([type, gid, x]);
    } else if (type === "MERGE") {
      const gid1 = data[idx++];
      const gid2 = data[idx++];
      operations.push([type, gid1, gid2]);
    } else {
      operations.push([type]);
    }
  }
  
  const solution = new Solution();
  const result = solution.processOperations(operations);
  console.log(result.join("\n"));
});
