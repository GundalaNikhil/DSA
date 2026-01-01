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
  processOperations(T, operations) {
    const left = new PriorityQueue((a, b) => b - a); // Max heap
    const right = new PriorityQueue((a, b) => a - b); // Min heap
    const leftDebt = new Map();
    const rightDebt = new Map();
    const globalCounts = new Map();
    let validLeft = 0;
    let validRight = 0;
    
    const cleanLeft = () => {
      while (!left.isEmpty()) {
        const val = left.peek();
        if ((leftDebt.get(val) || 0) > 0) {
          left.pop();
          leftDebt.set(val, leftDebt.get(val) - 1);
        } else {
          break;
        }
      }
    };

    const cleanRight = () => {
      while (!right.isEmpty()) {
        const val = right.peek();
        if ((rightDebt.get(val) || 0) > 0) {
          right.pop();
          rightDebt.set(val, rightDebt.get(val) - 1);
        } else {
          break;
        }
      }
    };
    
    const rebalance = () => {
      cleanLeft();
      cleanRight();
      
      while (validLeft > validRight + 1) {
        cleanLeft();
        if (left.isEmpty()) break;
        const val = left.pop();
        validLeft--;
        right.push(val);
        validRight++;
        cleanLeft();
      }
      
      cleanRight();
      while (validRight > validLeft) {
        cleanRight();
        if (right.isEmpty()) break;
        const val = right.pop();
        validRight--;
        left.push(val);
        validLeft++;
        cleanRight();
      }
    };
    
    const results = [];
    
    for (const opData of operations) {
      const op = opData[0];
      if (op === "ADD") {
        const x = parseInt(opData[1]);
        globalCounts.set(x, (globalCounts.get(x) || 0) + 1);
        
        cleanLeft();
        if (left.isEmpty() || x <= left.peek()) {
          left.push(x);
          validLeft++;
        } else {
          right.push(x);
          validRight++;
        }
        rebalance();
      } else if (op === "DEL") {
        const x = parseInt(opData[1]);
        if ((globalCounts.get(x) || 0) > 0) {
          globalCounts.set(x, globalCounts.get(x) - 1);
          
          cleanLeft();
          cleanRight();
          
          let inLeft = false;
          if (!left.isEmpty() && x <= left.peek()) inLeft = true;
          else inLeft = false;
          
          if (inLeft) {
            leftDebt.set(x, (leftDebt.get(x) || 0) + 1);
            validLeft--;
          } else {
            rightDebt.set(x, (rightDebt.get(x) || 0) + 1);
            validRight--;
          }
          
          rebalance();
        }
      } else {
        cleanLeft();
        const total = validLeft + validRight;
        if (total === 0) results.push("EMPTY");
        else if (total < T) results.push("NA");
        else results.push(left.peek().toString());
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
  const T = parseInt(data[idx++]);
  const operations = [];
  for (let i = 0; i < q; i++) {
    const op = data[idx++];
    if (op === "ADD" || op === "DEL") {
      const x = data[idx++];
      operations.push([op, x]);
    } else {
      operations.push([op]);
    }
  }
  
  const solution = new Solution();
  const result = solution.processOperations(T, operations);
  console.log(result.join("\n"));
});
