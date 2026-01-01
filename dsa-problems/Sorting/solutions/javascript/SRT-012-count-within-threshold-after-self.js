class Solution {
  countWithinThreshold(arr, T) {
    const n = arr.length;
    const counts = new Array(n).fill(0);

    for (let i = 0; i < n; i++) {
      for (let j = i + 1; j < n; j++) {
        if (arr[j] - arr[i] <= T) {
          counts[i]++;
        }
      }
    }

    return counts;
  }
}

const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const t = parseInt(data[idx++], 10);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(parseInt(data[idx++], 10));
}
const solution = new Solution();
const result = solution.countWithinThreshold(arr, t);
console.log(result.join(" "));
