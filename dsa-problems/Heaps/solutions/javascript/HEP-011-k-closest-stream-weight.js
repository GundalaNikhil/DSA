const readline = require("readline");

class PriorityQueue {
  constructor(compare) {
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
  processOperations(k, operations) {
    // Max-Heap: Compare(a, b) < 0 means a should be above b.
    // We want "Worse" (Larger) at top.
    // So if a > b, a should be above.
    // compare(a, b) should return -1 if a > b.
    const pq = new PriorityQueue((a, b) => {
      // Compare a vs b.
      // valA = a.num * b.den
      // valB = b.num * a.den
      const valA = a.num * b.den;
      const valB = b.num * a.den;
      
      if (valA > valB) return -1; // a is larger (worse), so a up
      if (valA < valB) return 1;
      if (a.id > b.id) return -1; // a is larger id (worse), so a up
      if (a.id < b.id) return 1;
      return 0;
    });
    
    const results = [];
    let currentId = 1;
    
    for (const op of operations) {
      if (op[0] === "ADD") {
        const x = BigInt(op[1]);
        const y = BigInt(op[2]);
        const w = BigInt(op[3]);
        const p = { num: x * x + y * y, den: w, id: currentId++ };
        
        if (pq.size() < k) {
          pq.push(p);
        } else {
          const top = pq.peek();
          // Check if p is better than top
          // p < top
          const valP = p.num * top.den;
          const valTop = top.num * p.den;
          
          let isBetter = false;
          if (valP < valTop) isBetter = true;
          else if (valP === valTop && p.id < top.id) isBetter = true;
          
          if (isBetter) {
            pq.pop();
            pq.push(p);
          }
        }
      } else {
        if (pq.isEmpty()) {
          results.push("EMPTY");
        } else {
          const list = [];
          // Copy heap
          const tempPQ = new PriorityQueue(pq.compare);
          pq.heap.forEach(item => tempPQ.push(item));
          while (!tempPQ.isEmpty()) list.push(tempPQ.pop());
          
          // List comes out Worst to Best (because pop removes top)
          // So we get Worst, 2nd Worst...
          // We want Best to Worst (Ascending).
          // So reverse the list.
          list.reverse();
          
          results.push(list.map(item => item.id).join(" "));
        }
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
  const k = parseInt(data[idx++]);
  const operations = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++];
    if (type === "ADD") {
      const x = data[idx++];
      const y = data[idx++];
      const w = data[idx++];
      operations.push([type, x, y, w]);
    } else {
      operations.push([type]);
    }
  }
  
  const solution = new Solution();
  const result = solution.processOperations(k, operations);
  console.log(result.join("\n"));
});
