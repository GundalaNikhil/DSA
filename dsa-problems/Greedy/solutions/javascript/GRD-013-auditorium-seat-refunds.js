const readline = require("readline");

class Solution {
  highestOccupiedRow(r, capacities, refunds) {
    const totalCapacity = capacities.reduce((a, b) => a + b, 0);
    let totalPeople = totalCapacity - refunds.length;
    
    if (totalPeople <= 0) return 0;
    
    for (let i = 0; i < r; i++) {
      totalPeople -= capacities[i];
      if (totalPeople <= 0) {
        return i + 1;
      }
    }
    
    return r;
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
  const [r, n] = data[ptr++].split(" ").map(Number);
  const capacities = data[ptr++].split(" ").map(Number);
  
  const refunds = [];
  for (let i = 0; i < n; i++) {
    const [row, seatId] = data[ptr++].split(" ").map(Number);
    refunds.push([row, seatId]);
  }

  const solution = new Solution();
  console.log(solution.highestOccupiedRow(r, capacities, refunds));
});
