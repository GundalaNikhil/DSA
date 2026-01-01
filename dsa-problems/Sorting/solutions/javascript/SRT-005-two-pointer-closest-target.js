class Solution {
  closestPair(arr, target) {
    const sorted = arr.slice().sort((a, b) => a - b);
    let n = sorted.length;
    let left = 0;
    let right = n - 1;
    
    let minDiff = Infinity;
    let resLeft = -1;
    let resRight = -1;
    
    while (left < right) {
      const sum = sorted[left] + sorted[right];
      const diff = Math.abs(sum - target);
      
      if (diff < minDiff) {
        minDiff = diff;
        resLeft = sorted[left];
        resRight = sorted[right];
      }
      
      if (sum < target) {
        left++;
      } else {
        right--;
      }
    }
    
    return [resLeft, resRight];
  }
}

const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const target = parseInt(data[idx++], 10);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(parseInt(data[idx++], 10));
}
const solution = new Solution();
const result = solution.closestPair(arr, target);
console.log(result[0] + " " + result[1]);
