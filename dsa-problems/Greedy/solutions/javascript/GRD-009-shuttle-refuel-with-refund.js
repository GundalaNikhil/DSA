const readline = require("readline");

class Solution {
  findStart(n, gain, cost) {
    let totalGain = 0;
    let totalCost = 0;
    let maxCostVal = -1;
    let maxCostIdx = -1;
    
    for (let i = 0; i < n; i++) {
      totalGain += gain[i];
      totalCost += cost[i];
      if (cost[i] > maxCostVal) {
        maxCostVal = cost[i];
        maxCostIdx = i;
      }
    }
    
    if (totalGain < totalCost - maxCostVal) {
      return -1;
    }
    
    let currentTank = 0;
    let start = 0;
    
    for (let i = 0; i < n; i++) {
      const currentCost = (i === maxCostIdx) ? 0 : cost[i];
      currentTank += gain[i] - currentCost;
      
      if (currentTank < 0) {
        start = i + 1;
        currentTank = 0;
      }
    }
    
    return start;
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
  const n = parseInt(data[ptr++]);
  const gain = data[ptr++].split(" ").map(Number);
  const cost = data[ptr++].split(" ").map(Number);

  const solution = new Solution();
  console.log(solution.findStart(n, gain, cost));
});
