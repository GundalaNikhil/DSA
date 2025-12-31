class Solution {
  closestPairCircular(arr, target) {
    const n = arr.length;
    if (n === 0) return [];
    
    let pivot = 0;
    for (let i = 1; i < n; i++) {
      if (arr[i] < arr[pivot]) {
        pivot = i;
      }
    }
    
    let l = 0;
    let r = n - 1;
    let minDiff = Infinity;
    let res = [];
    
    while (l < r) {
      const pL = (pivot + l) % n;
      const pR = (pivot + r) % n;
      
      const sum = arr[pL] + arr[pR];
      const diff = Math.abs(sum - target);
      
      if (diff < minDiff) {
        minDiff = diff;
        res = [arr[pL], arr[pR]];
      }
      
      if (sum < target) {
        l++;
      } else {
        r--;
      }
    }
    
    return res;
  }
}
