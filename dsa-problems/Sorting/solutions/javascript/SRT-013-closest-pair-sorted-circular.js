class Solution {
  closestPairCircular(arr, target) {
    const n = arr.length;
    if (n === 0) {
      return [];
    }
    if (n === 1) {
      return [0, 0];
    }

    let minIdx = 0;
    let minDiff = Math.abs(arr[0] - arr[1]);
    for (let i = 0; i < n; i++) {
      const next = (i + 1) % n;
      const diff = Math.abs(arr[i] - arr[next]);
      if (diff < minDiff) {
        minDiff = diff;
        minIdx = i;
      }
    }

    let a = minIdx;
    let b = (minIdx + 1) % n;
    if (a > b) {
      const tmp = a;
      a = b;
      b = tmp;
    }
    return [a, b];
  }
}

const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim();
if (!input) process.exit(0);
const data = input.split(/\s+/);
let idx = 0;
const n = parseInt(data[idx++], 10);
const arr = [];
for (let i = 0; i < n; i++) {
  arr.push(parseInt(data[idx++], 10));
}
const solution = new Solution();
const result = solution.closestPairCircular(arr, 0);
console.log(result[0] + " " + result[1]);
