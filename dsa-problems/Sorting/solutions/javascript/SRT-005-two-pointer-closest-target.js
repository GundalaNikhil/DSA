class Solution {
  closestPair(arr, target) {
    let n = arr.length;
    let left = 0;
    let right = n - 1;
    
    let minDiff = Infinity;
    let resLeft = -1;
    let resRight = -1;
    
    while (left < right) {
      const sum = arr[left] + arr[right];
      const diff = Math.abs(sum - target);
      
      if (diff < minDiff) {
        minDiff = diff;
        resLeft = arr[left];
        resRight = arr[right];
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
