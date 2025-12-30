const readline = require("readline");

class Solution {
  maxStages(n, B, bandwidths) {
    // Sort numerically!
    bandwidths.sort((a, b) => a - b);
    
    let currentSum = 0;
    let count = 0;
    
    for (const b of bandwidths) {
      if (currentSum + b <= B) {
        currentSum += b;
        count++;
      } else {
        break;
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
  const [n, B] = data[ptr++].split(" ").map(Number);
  const bandwidths = data[ptr++].split(" ").map(Number);

  const solution = new Solution();
  console.log(solution.maxStages(n, B, bandwidths));
});
