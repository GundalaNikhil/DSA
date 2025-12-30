class Solution {
  findPeak(arr, qLimit) {
    let low = 0;
    let high = arr.length - 1;
    
    while (low < high) {
      const mid = Math.floor((low + high) / 2);
      if (arr[mid] < arr[mid + 1]) {
        low = mid + 1;
      } else {
        high = mid;
      }
    }
    return low;
  }
}
