const readline = require("readline");

class Solution {
  findStart(gain, cost) {
    const n = gain.length;
    
    // 1. Find min gain
    let minGainIdx = 0;
    for (let i = 1; i < n; i++) {
      if (gain[i] < gain[minGainIdx]) {
        minGainIdx = i;
      }
    }
    
    // 2. Skip
    const original = gain[minGainIdx];
    gain[minGainIdx] = 0;
    
    // 3. Greedy
    let totalTank = 0;
    let currTank = 0;
    let start = 0;
    
    for (let i = 0; i < n; i++) {
      const net = gain[i] - cost[i];
      totalTank += net;
      currTank += net;
      if (currTank < 0) {
        start = i + 1;
        currTank = 0;
      }
    }
    
    gain[minGainIdx] = original;
    
    return totalTank >= 0 ? start % n : -1;
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
  const gain = [];
  const cost = [];
  for (let i = 0; i < n; i++) {
    gain.push(parseInt(data[idx++], 10));
  }
  for (let i = 0; i < n; i++) {
    cost.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  console.log(solution.findStart(gain, cost));
});
