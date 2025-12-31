const readline = require("readline");

class Solution {
  minBatterySwaps(n, T, capacities) {
    // Use BigInt for potentially large sums, though Number is usually safe up to 2^53
    // Given constraints T <= 10^9, Number is fine.
    // But sum of capacities could exceed 2^53? 10^5 * 10^9 = 10^14 < 2^53. Safe.
    
    let totalCapacity = 0;
    for (const c of capacities) {
      totalCapacity += c;
    }
    
    if (totalCapacity < T) {
      return -1;
    }
    
    // Sort descending
    capacities.sort((a, b) => b - a);
    
    let currentSum = 0;
    let count = 0;
    
    for (const c of capacities) {
      currentSum += c;
      count++;
      if (currentSum >= T) {
        return count - 1;
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
  
  let ptr = 0;
  const [n, T] = data[ptr++].split(" ").map(Number);
  const capacities = data[ptr++].split(" ").map(Number);

  const solution = new Solution();
  console.log(solution.minBatterySwaps(n, T, capacities));
});
