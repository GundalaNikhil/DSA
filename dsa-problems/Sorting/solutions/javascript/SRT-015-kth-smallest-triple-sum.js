class Solution {
  kthTripleSum(arr, k) {
    const n = arr.length;
    // Use numeric sort
    arr.sort((a, b) => a - b);
    
    // Use BigInt for sums to avoid overflow
    const bigK = BigInt(k);
    
    const countLessEqual = (target) => {
      let count = 0n;
      for (let i = 0; i < n - 2; i++) {
        const valI = BigInt(arr[i]);
        const valI1 = BigInt(arr[i+1]);
        const valI2 = BigInt(arr[i+2]);
        
        if (valI + valI1 + valI2 > target) break;
        
        const valN2 = BigInt(arr[n-2]);
        const valN1 = BigInt(arr[n-1]);
        
        if (valI + valN2 + valN1 <= target) {
          const remaining = BigInt(n - 1 - i);
          count += remaining * (remaining - 1n) / 2n;
          continue;
        }
        
        const rem = target - valI;
        let l = i + 1;
        let r = n - 1;
        while (l < r) {
          if (BigInt(arr[l]) + BigInt(arr[r]) <= rem) {
            count += BigInt(r - l);
            l++;
          } else {
            r--;
          }
        }
      }
      return count;
    };
    
    let low = BigInt(arr[0]) + BigInt(arr[1]) + BigInt(arr[2]);
    let high = BigInt(arr[n-1]) + BigInt(arr[n-2]) + BigInt(arr[n-3]);
    let ans = high;
    
    while (low <= high) {
      const mid = (low + high) / 2n;
      if (countLessEqual(mid) >= bigK) {
        ans = mid;
        high = mid - 1n;
      } else {
        low = mid + 1n;
      }
    }
    return ans.toString();
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
console.log(solution.kthTripleSum(arr, k).toString());
