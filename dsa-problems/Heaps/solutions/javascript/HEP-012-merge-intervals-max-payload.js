const readline = require("readline");

class Solution {
  mergeIntervals(intervals) {
    if (intervals.length === 0) return [];
    
    // Sort by start time
    intervals.sort((a, b) => a[0] - b[0]);
    
    const merged = [];
    let current = intervals[0];
    
    for (let i = 1; i < intervals.length; i++) {
      const next = intervals[i];
      
      if (next[0] <= current[1]) {
        current[1] = Math.max(current[1], next[1]);
        current[2] = Math.max(current[2], next[2]);
      } else {
        merged.push(current);
        current = next;
      }
    }
    merged.push(current);
    
    return merged;
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
  const intervals = [];
  for (let i = 0; i < n; i++) {
    const start = parseInt(data[idx++]);
    const end = parseInt(data[idx++]);
    const payload = parseInt(data[idx++]);
    intervals.push([start, end, payload]);
  }
  
  const solution = new Solution();
  const result = solution.mergeIntervals(intervals);
  console.log(result.length);
  for (const row of result) {
    console.log(row[0] + " " + row[1] + " " + row[2]);
  }
});
