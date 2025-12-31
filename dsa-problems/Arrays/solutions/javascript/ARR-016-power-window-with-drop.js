const readline = require("readline");

class Solution {
  maxWindowSumWithDrop(arr, k) {
    const n = arr.length;
    if (n < k) return 0;
    
    let currentSum = 0n;
    for (let i = 0; i < k; i++) {
      currentSum += BigInt(arr[i]);
    }
    
    let maxTotal = currentSum;
    
    for (let i = k; i < n; i++) {
      currentSum += BigInt(arr[i]);
      currentSum -= BigInt(arr[i - k]);
      if (currentSum > maxTotal) {
        maxTotal = currentSum;
      }
    }
    
    return maxTotal.toString();
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
    const tokens = data.join(" ").split(/\s+/);
    if (tokens.length === 0 || tokens[0] === "") return;
    
    let ptr = 0;
    const n = Number(tokens[ptr++]);
    const arr = [];
    for (let i = 0; i < n; i++) arr.push(Number(tokens[ptr++]));
    
    const k = Number(tokens[ptr++]);
    
    const solution = new Solution();
    console.log(solution.maxWindowSumWithDrop(arr, k));
});
