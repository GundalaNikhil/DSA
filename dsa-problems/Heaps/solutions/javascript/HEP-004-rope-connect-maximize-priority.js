const readline = require("readline");

class Solution {
  maxFinalStrength(strengths, priority) {
    let totalSum = 0n;
    let has1 = false;
    let has2 = false;
    let has3 = false;
    
    for (let i = 0; i < strengths.length; i++) {
      totalSum += BigInt(strengths[i]);
      if (priority[i] === 1) has1 = true;
      else if (priority[i] === 2) has2 = true;
      else if (priority[i] === 3) has3 = true;
    }
    
    let penalty = 0n;
    if (has1 && has2 && has3) penalty = 2n;
    else if (has1 && has2) penalty = 1n;
    else if (has2 && has3) penalty = 1n;
    else if (has1 && has3) penalty = 2n;
    
    return (totalSum - penalty).toString();
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++]);
  const strengths = [];
  const priority = [];
  for (let i = 0; i < n; i++) strengths.push(parseInt(data[idx++]));
  for (let i = 0; i < n; i++) priority.push(parseInt(data[idx++]));
  
  const solution = new Solution();
  console.log(solution.maxFinalStrength(strengths, priority));
});
