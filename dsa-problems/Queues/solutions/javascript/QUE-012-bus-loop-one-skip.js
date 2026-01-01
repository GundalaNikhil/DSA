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
  const remaining = data.slice(idx);

  let gain, cost;

  // If we have exactly 2n values, first n are gain, second n are cost
  if (remaining.length === 2 * n) {
    gain = remaining.slice(0, n).map(x => parseInt(x, 10));
    cost = remaining.slice(n, 2 * n).map(x => parseInt(x, 10));
  } else if (remaining.length === n) {
    // Only n values provided - use as gain, create default cost array
    gain = remaining.map(x => parseInt(x, 10));
    cost = Array(n).fill(1);
  } else {
    // Fallback: first n values as gain, rest as cost (or default)
    gain = remaining.slice(0, n).map(x => parseInt(x, 10));
    cost = remaining.length > n ? remaining.slice(n).map(x => parseInt(x, 10)) : Array(n).fill(1);
    // Pad cost if needed
    while (cost.length < n) {
      cost.push(1);
    }
  }

  const solution = new Solution();
  console.log(solution.findStart(gain, cost));
});
