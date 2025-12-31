class Solution {
  countEvenIndices(arr, x) {
    const n = arr.length;
    
    const findPivot = (low, high) => {
      while (low < high) {
        const mid = Math.floor((low + high) / 2);
        if (arr[mid] > arr[high]) {
          low = mid + 1;
        } else if (arr[mid] < arr[high]) {
          high = mid;
        } else {
          high--;
        }
      }
      return low;
    };
    
    const searchRange = (low, high, target) => {
      let start = -1, end = -1;
      
      let l = low, r = high;
      while (l <= r) {
        const mid = Math.floor((l + r) / 2);
        if (arr[mid] >= target) {
          if (arr[mid] === target) start = mid;
          r = mid - 1;
        } else {
          l = mid + 1;
        }
      }
      
      if (start === -1) return [-1, -1];
      
      l = low; r = high;
      while (l <= r) {
        const mid = Math.floor((l + r) / 2);
        if (arr[mid] <= target) {
          if (arr[mid] === target) end = mid;
          l = mid + 1;
        } else {
          r = mid - 1;
        }
      }
      return [start, end];
    };
    
    const countEvens = (L, R) => {
      if (L > R) return 0;
      const len = R - L + 1;
      if (len % 2 === 0) return len / 2;
      return (L % 2 === 0) ? (len + 1) / 2 : (len - 1) / 2;
    };
    
    const pivot = findPivot(0, n - 1);
    let count = 0;
    
    if (pivot > 0) {
      const [s, e] = searchRange(0, pivot - 1, x);
      if (s !== -1) count += countEvens(s, e);
    }
    
    const [s, e] = searchRange(pivot, n - 1, x);
    if (s !== -1) count += countEvens(s, e);
    
    return count;
  }
}
