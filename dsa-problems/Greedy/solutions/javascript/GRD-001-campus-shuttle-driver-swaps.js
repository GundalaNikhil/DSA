const readline = require("readline");

class Solution {
  minDriverSwaps(trips, driverA, driverB) {
    const n = trips.length;
    const INF = Number.MAX_SAFE_INTEGER;
    
    let costA = INF;
    let costB = INF;
    
    const canCover = (trip, driver) => {
      return driver[0] <= trip[0] && trip[1] <= driver[1];
    };
    
    // Base case
    if (canCover(trips[0], driverA)) costA = 0;
    if (canCover(trips[0], driverB)) costB = 0;
    
    for (let i = 1; i < n; i++) {
      let nextCostA = INF;
      let nextCostB = INF;
      
      if (canCover(trips[i], driverA)) {
        nextCostA = Math.min(costA, costB + 1);
      }
      
      if (canCover(trips[i], driverB)) {
        nextCostB = Math.min(costB, costA + 1);
      }
      
      costA = nextCostA;
      costB = nextCostB;
    }
    
    let result = Math.min(costA, costB);
    return result >= INF ? -1 : result;
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
  
  const trips = [];
  for (let i = 0; i < n; i++) {
    const [start, end] = data[ptr++].split(" ").map(Number);
    trips.push([start, end]);
  }
  
  const [aStart, aEnd] = data[ptr++].split(" ").map(Number);
  const driverA = [aStart, aEnd];
  
  const [bStart, bEnd] = data[ptr++].split(" ").map(Number);
  const driverB = [bStart, bEnd];
  
  const solution = new Solution();
  console.log(solution.minDriverSwaps(trips, driverA, driverB));
});
