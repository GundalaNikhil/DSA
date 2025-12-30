class Solution {
  solve(arr, queries) {
    const results = [];
    const n = arr.length;
    
    for (const [k, b] of queries) {
      // Use BigInt for safety as k*b can exceed 2^53
      const m = BigInt(k) * BigInt(b);
      
      let low = 0;
      let high = n - 1;
      let idx = -1;
      
      while (low <= high) {
        const mid = Math.floor((low + high) / 2);
        const missingCount = BigInt(arr[mid]) - BigInt(mid + 1);
        if (missingCount < m) {
          idx = mid;
          low = mid + 1;
        } else {
          high = mid - 1;
        }
      }
      
      // Result is m + idx + 1
      // idx is number, m is BigInt. 
      // idx + 1 is the count of numbers in arr that are <= result
      results.push(Number(m + BigInt(idx + 1)));
    }
    return results;
  }
}
