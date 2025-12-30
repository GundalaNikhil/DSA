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
  maximizeCapital(k, C, R, cost, profit, risk) {
    const n = cost.length;
    const projects = [];
    for (let i = 0; i < n; i++) {
      projects.push({ c: BigInt(cost[i]), p: BigInt(profit[i]), r: BigInt(risk[i]) });
    }
    
    projects.sort((a, b) => {
      if (a.c < b.c) return -1;
      if (a.c > b.c) return 1;
      return 0;
    });
    
    const pq = new PriorityQueue((a, b) => {
      if (a.p > b.p) return -1;
      if (a.p < b.p) return 1;
      return 0;
    });
    
    let ptr = 0;
    let currentC = BigInt(C);
    let remainingR = BigInt(R);
    
    for (let i = 0; i < k; i++) {
      while (ptr < n && projects[ptr].c <= currentC) {
        pq.push(projects[ptr]);
        ptr++;
      }
      
      let picked = false;
      while (!pq.isEmpty()) {
        const top = pq.peek();
        if (top.r <= remainingR) {
          pq.pop();
          currentC += top.p;
          remainingR -= top.r;
          picked = true;
          break;
        } else {
          pq.pop();
        }
      }
      
      if (!picked) break;
    }
    
    return currentC.toString();
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
  const k = parseInt(data[idx++]);
  const C = parseInt(data[idx++]);
  const R = parseInt(data[idx++]);
  const cost = [];
  const profit = [];
  const risk = [];
  for (let i = 0; i < n; i++) {
    cost.push(parseInt(data[idx++]));
    profit.push(parseInt(data[idx++]));
    risk.push(parseInt(data[idx++]));
  }
  
  const solution = new Solution();
  console.log(solution.maximizeCapital(k, C, R, cost, profit, risk));
});
