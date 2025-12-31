const readline = require("readline");

class Solution {
  minTotalDelay(n, trips) {
    // Sort by s + d
    trips.sort((a, b) => (a[0] + a[1]) - (b[0] + b[1]));
    
    let currentTime = 0;
    let totalDelay = 0;
    
    for (const [s, d] of trips) {
      const delay = Math.max(0, currentTime - s);
      totalDelay += delay;
      currentTime += d;
    }
    
    return totalDelay;
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
    const [s, d] = data[ptr++].split(" ").map(Number);
    trips.push([s, d]);
  }
  
  const solution = new Solution();
  console.log(solution.minTotalDelay(n, trips));
});
