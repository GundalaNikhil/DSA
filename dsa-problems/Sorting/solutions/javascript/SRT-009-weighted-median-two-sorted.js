class Solution {
  weightedMedian(A, B, wA, wB) {
    // Use BigInt for counts as they can exceed 2^53
    const n = BigInt(A.length);
    const m = BigInt(B.length);
    const bigWA = BigInt(wA);
    const bigWB = BigInt(wB);
    const total = n * bigWA + m * bigWB;
    
    const upperBound = (arr, val) => {
      let l = 0, r = arr.length - 1;
      let res = 0;
      while (l <= r) {
        const mid = Math.floor((l + r) / 2);
        if (arr[mid] <= val) {
          res = mid + 1;
          l = mid + 1;
        } else {
          r = mid - 1;
        }
      }
      return BigInt(res);
    };
    
    const countLessEqual = (val) => {
      let count = 0n;
      count += upperBound(A, val) * bigWA;
      count += upperBound(B, val) * bigWB;
      return count;
    };
    
    const findKth = (k) => {
      let low = -2000000000;
      let high = 2000000000;
      let ans = high;
      
      while (low <= high) {
        const mid = Math.floor((low + high) / 2); // JS bitwise ops are 32-bit, use Math.floor
        if (countLessEqual(mid) > k) {
          ans = mid;
          high = mid - 1;
        } else {
          low = mid + 1;
        }
      }
      return BigInt(ans);
    };
    
    if (total % 2n === 1n) {
      return findKth(total / 2n).toString();
    } else {
      const val1 = findKth(total / 2n - 1n);
      const val2 = findKth(total / 2n);
      const sum = val1 + val2;
      if (sum % 2n === 0n) {
        return (sum / 2n).toString();
      } else {
        return (sum / 2n).toString() + ".5";
      }
    }
  }
}
