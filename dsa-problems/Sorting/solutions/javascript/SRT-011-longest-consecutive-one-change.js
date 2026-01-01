class Solution {
  longestAfterChange(arr) {
    const n = arr.length;
    if (n <= 1) return n;
    
    const L = new Int32Array(n).fill(1);
    for (let i = 1; i < n; i++) {
      if (arr[i] > arr[i-1]) L[i] = L[i-1] + 1;
    }
    
    const R = new Int32Array(n).fill(1);
    for (let i = n - 2; i >= 0; i--) {
      if (arr[i] < arr[i+1]) R[i] = R[i+1] + 1;
    }
    
    let maxLen = 1;
    for (let i = 0; i < n; i++) maxLen = Math.max(maxLen, L[i]);
    
    for (let i = 0; i < n; i++) {
      if (i > 0) maxLen = Math.max(maxLen, L[i-1] + 1);
      if (i < n - 1) maxLen = Math.max(maxLen, R[i+1] + 1);
      
      if (i > 0 && i < n - 1 && arr[i+1] - arr[i-1] >= 2) {
        maxLen = Math.max(maxLen, L[i-1] + 1 + R[i+1]);
      }
    }
    
    return maxLen;
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
console.log(solution.longestAfterChange(arr).toString());
