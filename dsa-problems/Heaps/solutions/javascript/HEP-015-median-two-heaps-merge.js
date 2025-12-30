const readline = require("readline");

class Solution {
  findMedian(maxHeap, minHeap) {
    const all = maxHeap.concat(minHeap);
    all.sort((a, b) => a - b);
    
    const n = all.length;
    if (n === 0) return 0.0;
    
    if (n % 2 === 1) {
      return all[Math.floor(n / 2)];
    } else {
      const mid1 = all[n / 2 - 1];
      const mid2 = all[n / 2];
      return (mid1 + mid2) / 2.0;
    }
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part) data.push(part);
  }
});
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++]);
  const m = parseInt(data[idx++]);
  const maxHeap = [];
  const minHeap = [];
  for (let i = 0; i < n; i++) maxHeap.push(parseInt(data[idx++]));
  for (let i = 0; i < m; i++) minHeap.push(parseInt(data[idx++]));
  
  const solution = new Solution();
  console.log(solution.findMedian(maxHeap, minHeap));
});
