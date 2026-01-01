const readline = require("readline");

class Solution {
  checkStart(n, gain, cost, startIdx) {
    let fuel = 0;
    let maxC = 0;
    let used = false;

    for (let i = 0; i < n; i++) {
      const idx = (startIdx + i) % n;
      fuel += gain[idx];
      maxC = Math.max(maxC, cost[idx]);
      fuel -= cost[idx];

      if (fuel < 0) {
        if (!used) {
          fuel += maxC;
          used = true;
          if (fuel < 0) return false;
        } else {
          return false;
        }
      }
    }

    return true;
  }

  findStart(n, gain, cost) {
    let totalGain = 0;
    let totalCost = 0;
    let maxCost = 0;

    for (let i = 0; i < n; i++) {
      totalGain += gain[i];
      totalCost += cost[i];
      maxCost = Math.max(maxCost, cost[i]);
    }

    // If even with refund we can't make it, return -1
    if (totalGain < totalCost - maxCost) {
      return -1;
    }

    // Total gain + max cost must be >= total cost
    if (totalGain + maxCost < totalCost) {
      return -1;
    }

    // Check classic gas station start first
    const diff = [];
    for (let i = 0; i < n; i++) {
      diff[i] = gain[i] - cost[i];
    }

    let curr = 0;
    let minSum = 0;
    let startCand = 0;

    for (let i = 0; i < n; i++) {
      curr += diff[i];
      if (curr < minSum) {
        minSum = curr;
        startCand = (i + 1) % n;
      }
    }

    if (this.checkStart(n, gain, cost, startCand)) {
      return startCand;
    }

    // If not, try all
    for (let i = 0; i < n; i++) {
      if (this.checkStart(n, gain, cost, i)) {
        return i;
      }
    }

    return -1;
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

  // Parse all numbers from all lines
  const allNumbers = [];
  for (const line of data) {
    allNumbers.push(...line.split(" ").map(Number));
  }

  let ptr = 0;
  const n = allNumbers[ptr++];
  const gain = [];
  for (let i = 0; i < n; i++) {
    gain.push(allNumbers[ptr++]);
  }
  const cost = [];
  for (let i = 0; i < n; i++) {
    cost.push(allNumbers[ptr++]);
  }

  const solution = new Solution();
  console.log(solution.findStart(n, gain, cost));
});
