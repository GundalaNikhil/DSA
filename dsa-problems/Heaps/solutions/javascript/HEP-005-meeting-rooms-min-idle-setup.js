const readline = require("readline");

// Simple BST / TreeMap implementation for JS
class TreeMap {
  constructor() {
    // Sorted array + counts map for used rooms.
    this.keys = [];
    this.counts = {};
  }
  
  // Find largest key <= val
  floorKey(val) {
    if (this.keys.length === 0) return null;
    let l = 0, r = this.keys.length - 1;
    let res = null;
    while (l <= r) {
      const mid = Math.floor((l + r) / 2);
      if (this.keys[mid] <= val) {
        res = this.keys[mid];
        l = mid + 1;
      } else {
        r = mid - 1;
      }
    }
    return res;
  }
  
  removeOne(key) {
    if (this.counts[key] > 1) {
      this.counts[key]--;
    } else {
      delete this.counts[key];
      // Remove from keys array
      // Binary search to find index
      let l = 0, r = this.keys.length - 1;
      while (l <= r) {
        const mid = Math.floor((l + r) / 2);
        if (this.keys[mid] === key) {
          this.keys.splice(mid, 1);
          return;
        } else if (this.keys[mid] < key) {
          l = mid + 1;
        } else {
          r = mid - 1;
        }
      }
    }
  }
  
  addOne(key) {
    if (this.counts[key]) {
      this.counts[key]++;
    } else {
      this.counts[key] = 1;
      // Insert into keys array sorted
      // Find index
      let l = 0, r = this.keys.length - 1;
      let idx = this.keys.length;
      while (l <= r) {
        const mid = Math.floor((l + r) / 2);
        if (this.keys[mid] < key) {
          l = mid + 1;
        } else {
          idx = mid;
          r = mid - 1;
        }
      }
      this.keys.splice(idx, 0, key);
    }
  }
}

class Solution {
  minTotalSlack(meetings, k, s) {
    meetings.sort((a, b) => a[0] - b[0]);
    
    const rooms = new TreeMap();
    let unused = k;
    
    let totalSlack = 0n;
    
    for (const [start, end] of meetings) {
      const freeTime = rooms.floorKey(start);
      
      if (freeTime !== null) {
        totalSlack += BigInt(start - freeTime);
        rooms.removeOne(freeTime);
      } else {
        // Use a fresh room; first meeting in a room has 0 slack.
        unused--;
      }

      rooms.addOne(end + s);
    }
    
    return totalSlack.toString();
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
  const s = parseInt(data[idx++]);
  const meetings = [];
  for (let i = 0; i < n; i++) {
    const start = parseInt(data[idx++]);
    const end = parseInt(data[idx++]);
    meetings.push([start, end]);
  }
  
  const solution = new Solution();
  console.log(solution.minTotalSlack(meetings, k, s));
});
