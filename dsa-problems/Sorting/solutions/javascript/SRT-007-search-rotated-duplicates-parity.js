class Solution {
  countEvenIndices(arr, x) {
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] === x) {
        return i;
      }
    }
    return -1;
  }
}

const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const x = parseInt(data[idx++], 10);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(parseInt(data[idx++], 10));
}
const solution = new Solution();
console.log(solution.countEvenIndices(arr, x).toString());
