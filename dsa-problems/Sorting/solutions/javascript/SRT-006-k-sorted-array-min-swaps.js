class Solution {
  minSwapsToSort(arr, k = 0) {
    const pairs = arr.map((val, idx) => ({ val, idx }));
    pairs.sort((a, b) => a.val - b.val);

    let violations = 0;
    for (let targetIdx = 0; targetIdx < pairs.length; targetIdx++) {
      const originalIdx = pairs[targetIdx].idx;
      if (Math.abs(targetIdx - originalIdx) > k) {
        violations++;
      }
    }

    return Math.floor(violations / 2);
  }
}

const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const k = parseInt(data[idx++], 10);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(parseInt(data[idx++], 10));
}
const solution = new Solution();
console.log(solution.minSwapsToSort(arr, k).toString());
