const readline = require("readline");

class Task {
  constructor(name, count, priority) {
    this.name = name;
    this.count = count;
    this.priority = priority;
    this.readyTime = 0;
  }
}

class MaxHeap {
  constructor() {
    this.heap = [];
  }
  push(val) {
    this.heap.push(val);
    this._siftUp();
  }
  pop() {
    if (this.size() === 0) return null;
    if (this.size() === 1) return this.heap.pop();
    const max = this.heap[0];
    this.heap[0] = this.heap.pop();
    this._siftDown();
    return max;
  }
  size() {
    return this.heap.length;
  }
  _compare(a, b) {
    if (a.priority !== b.priority) return a.priority - b.priority;
    return a.count - b.count;
  }
  _siftUp() {
    let idx = this.heap.length - 1;
    while (idx > 0) {
      const parentIdx = Math.floor((idx - 1) / 2);
      if (this._compare(this.heap[idx], this.heap[parentIdx]) <= 0) break;
      [this.heap[idx], this.heap[parentIdx]] = [this.heap[parentIdx], this.heap[idx]];
      idx = parentIdx;
    }
  }
  _siftDown() {
    let idx = 0;
    while (idx < this.heap.length) {
      let maxChildIdx = null;
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      if (left < this.heap.length) maxChildIdx = left;
      if (right < this.heap.length && this._compare(this.heap[right], this.heap[left]) > 0) {
        maxChildIdx = right;
      }
      if (maxChildIdx === null || this._compare(this.heap[idx], this.heap[maxChildIdx]) >= 0) break;
      [this.heap[idx], this.heap[maxChildIdx]] = [this.heap[maxChildIdx], this.heap[idx]];
      idx = maxChildIdx;
    }
  }
}

class Solution {
  minSlots(tasksData, k) {
    const readyQueue = new MaxHeap();
    for (const t of tasksData) {
      readyQueue.push(new Task(t.name, t.count, t.priority));
    }
    
    let cooldownList = [];
    let time = 0;
    let tasksRemaining = tasksData.reduce((acc, t) => acc + t.count, 0);
    
    while (tasksRemaining > 0) {
      time++;
      
      const nextCooldown = [];
      for (const t of cooldownList) {
        if (t.readyTime <= time) {
          readyQueue.push(t);
        } else {
          nextCooldown.push(t);
        }
      }
      cooldownList = nextCooldown;
      
      if (readyQueue.size() === 0) {
        continue;
      }
      
      const current = readyQueue.pop();
      current.count--;
      tasksRemaining--;
      
      for (const t of cooldownList) {
        if (t.priority < current.priority) {
          t.readyTime = Math.max(t.readyTime, time + k + 1);
        }
      }
      
      if (current.count > 0) {
        current.readyTime = time + k + 1;
        cooldownList.push(current);
      }
    }
    
    return time;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;
  
  let ptr = 0;
  const [n, k] = data[ptr++].split(" ").map(Number);
  
  const tasks = [];
  for (let i = 0; i < n; i++) {
    const parts = data[ptr++].split(" ");
    const name = parts[0];
    const count = parseInt(parts[1]);
    const priority = parseInt(parts[2]);
    tasks.push({ name, count, priority });
  }

  const solution = new Solution();
  console.log(solution.minSlots(tasks, k));
});
