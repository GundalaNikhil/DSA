const readline = require("readline");

class Solution {
  minOvertimeCost(n, H, shifts) {
    let totalStandard = 0;
    let minRate = Infinity;
    
    for (const [l, p] of shifts) {
      totalStandard += l;
      if (p < minRate) {
        minRate = p;
      }
    }
    
    if (totalStandard >= H) {
      return 0;
    }
    
    const needed = H - totalStandard;
    return needed * minRate;
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
  const [n, H] = data[ptr++].split(" ").map(Number);

  const shifts = [];
  for (let i = 0; i < n; i++) {
    const [l, p] = data[ptr++].split(" ").map(Number);
    shifts.push([l, p]);
  }

  const solution = new Solution();
  console.log(solution.minOvertimeCost(n, H, shifts));
});
