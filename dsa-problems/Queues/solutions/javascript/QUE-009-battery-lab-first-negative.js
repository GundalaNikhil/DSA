const readline = require("readline");

class Solution {
  solve(arr) {
    if (arr.length === 0) {
      return "0";
    }

    // Find first negative
    let firstNegIdx = -1;
    let firstNegVal = null;
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] < 0) {
        firstNegIdx = i;
        firstNegVal = arr[i];
        break;
      }
    }

    if (firstNegIdx === -1) {
      // No negative found - return sum modulo 100
      let sum = arr.reduce((a, b) => a + b, 0);
      return String(sum % 100);
    }

    // With first negative found
    // Compute: sum of elements up to first negative + first negative value
    let prefixSum = 0;
    for (let i = 0; i < firstNegIdx; i++) {
      prefixSum += arr[i];
    }
    const result = prefixSum + firstNegVal;

    return String(result);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x !== "")));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(parseInt(data[idx++], 10));
  }

  const solution = new Solution();
  const result = solution.solve(arr);
  console.log(result);
});
