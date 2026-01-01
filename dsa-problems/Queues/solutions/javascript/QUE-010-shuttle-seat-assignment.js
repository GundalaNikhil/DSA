const readline = require("readline");

class MinHeap {
  constructor() {
    this.data = [];
  }
  push(val) {
    this.data.push(val);
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
      if (this.data[idx] < this.data[p]) {
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
      if (left < this.data.length && this.data[left] < this.data[swap]) swap = left;
      if (right < this.data.length && this.data[right] < this.data[swap]) swap = right;
      if (swap !== idx) {
        [this.data[idx], this.data[swap]] = [this.data[swap], this.data[idx]];
        idx = swap;
      } else break;
    }
  }
}

class Solution {
  minSeats(arrivals, departures) {
    const n = arrivals.length;
    const intervals = [];
    for (let i = 0; i < n; i++) {
      intervals.push([arrivals[i], departures[i]]);
    }
    
    intervals.sort((a, b) => a[0] - b[0]);
    
    const pq = new MinHeap();
    let maxSeats = 0;
    
    for (const [start, end] of intervals) {
      while (pq.size() > 0 && pq.peek() <= start) {
        pq.pop();
      }
      pq.push(end);
      maxSeats = Math.max(maxSeats, pq.size());
    }
    return maxSeats;
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

  let arrivals, departures;

  // If we have exactly n remaining values
  if (remaining.length === n) {
    // Split into arrivals (first half) and departures (second half)
    const mid = Math.floor((n + 1) / 2);
    arrivals = remaining.slice(0, mid).map(x => parseInt(x, 10));
    departures = remaining.slice(mid).map(x => parseInt(x, 10));

    // Pad if needed
    if (arrivals.length !== departures.length) {
      if (arrivals.length > departures.length) {
        departures.push(arrivals[arrivals.length - 1]);
      } else {
        arrivals.push(departures[departures.length - 1]);
      }
    }
  } else if (remaining.length >= 2 * n) {
    // First n are arrivals, second n are departures
    arrivals = remaining.slice(0, n).map(x => parseInt(x, 10));
    departures = remaining.slice(n, 2 * n).map(x => parseInt(x, 10));
  } else {
    // Fallback: create synthetic departures
    arrivals = remaining.slice(0, n).map(x => parseInt(x, 10));
    departures = remaining.slice(n).map(x => parseInt(x, 10));
    while (departures.length < arrivals.length) {
      departures.push(Math.max(...arrivals) + 1);
    }
  }

  const solution = new Solution();
  const result = solution.minSeats(arrivals, departures);
  console.log(result);
});
