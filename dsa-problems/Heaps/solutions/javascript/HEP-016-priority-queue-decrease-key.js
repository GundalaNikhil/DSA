const readline = require("readline");

class Solution {
  constructor() {
    this.heap = []; // {id, value}
    this.pos = new Map(); // id -> index
  }
  
  swap(i, j) {
    const t = this.heap[i];
    this.heap[i] = this.heap[j];
    this.heap[j] = t;
    
    this.pos.set(this.heap[i].id, i);
    this.pos.set(this.heap[j].id, j);
  }
  
  less(i, j) {
    const n1 = this.heap[i];
    const n2 = this.heap[j];
    if (n1.value !== n2.value) {
      return n1.value < n2.value;
    }
    return n1.id < n2.id;
  }
  
  bubbleUp(k) {
    while (k > 0) {
      const p = Math.floor((k - 1) / 2);
      if (this.less(k, p)) {
        this.swap(k, p);
        k = p;
      } else {
        break;
      }
    }
  }
  
  bubbleDown(k) {
    const n = this.heap.length;
    while (true) {
      const left = 2 * k + 1;
      if (left >= n) break;
      let child = left;
      const right = left + 1;
      if (right < n && this.less(right, left)) {
        child = right;
      }
      if (this.less(child, k)) {
        this.swap(k, child);
        k = child;
      } else {
        break;
      }
    }
  }
  
  processOperations(operations) {
    const results = [];
    this.heap = [];
    this.pos.clear();
    
    for (const op of operations) {
      const type = op[0];
      if (type === "INSERT") {
        const id = op[1];
        const val = BigInt(op[2]);
        this.heap.push({ id, value: val });
        this.pos.set(id, this.heap.length - 1);
        this.bubbleUp(this.heap.length - 1);
      } else if (type === "DECREASE") {
        const id = op[1];
        const delta = BigInt(op[2]);
        if (this.pos.has(id)) {
          const idx = this.pos.get(id);
          this.heap[idx].value -= delta;
          this.bubbleUp(idx);
        }
      } else if (type === "EXTRACT") {
        if (this.heap.length === 0) {
          results.push("EMPTY");
        } else {
          const min = this.heap[0];
          results.push(`${min.value} ${min.id}`);
          
          this.pos.delete(min.id);
          const last = this.heap.pop();
          
          if (this.heap.length > 0) {
            this.heap[0] = last;
            this.pos.set(last.id, 0);
            this.bubbleDown(0);
          }
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
  const operations = [];
  for (let i = 0; i < q; i++) {
    const type = data[idx++];
    if (type === "INSERT") {
      const id = data[idx++];
      const val = data[idx++];
      operations.push([type, id, val]);
    } else if (type === "DECREASE") {
      const id = data[idx++];
      const delta = data[idx++];
      operations.push([type, id, delta]);
    } else {
      operations.push([type]);
    }
  }
  
  const solution = new Solution();
  const result = solution.processOperations(operations);
  console.log(result.join("\n"));
});
