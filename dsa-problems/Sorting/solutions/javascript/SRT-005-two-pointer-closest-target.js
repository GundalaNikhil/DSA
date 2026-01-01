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
