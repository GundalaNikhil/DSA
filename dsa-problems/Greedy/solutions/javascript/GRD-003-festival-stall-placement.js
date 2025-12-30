const readline = require("readline");

class Solution {
  maxStalls(stalls, d) {
    // Sort by end time
    stalls.sort((a, b) => a[1] - b[1]);
    
    let count = 0;
    let lastEnd = -Infinity;
    
    for (const [start, end] of stalls) {
      if (start - lastEnd >= d) {
        count++;
        lastEnd = end;
      }
    }
    
    return count;
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
  const [n, d] = data[ptr++].split(" ").map(Number);

  const stalls = [];
  for (let i = 0; i < n; i++) {
    const [start, end] = data[ptr++].split(" ").map(Number);
    stalls.push([start, end]);
  }

  const solution = new Solution();
  console.log(solution.maxStalls(stalls, d));
});
