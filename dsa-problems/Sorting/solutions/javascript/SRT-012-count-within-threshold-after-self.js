class Solution {
  countWithinThreshold(arr, T) {
    const n = arr.length;
    const counts = new Array(n).fill(0); // Use regular array, counts can be large but fit in double precision usually
    // Or use BigInt if n is very large, but max count is N, fits in number.
    
    const pairs = arr.map((val, idx) => ({ val, idx }));
    
    const mergeSort = (subArr) => {
      if (subArr.length <= 1) return subArr;
      
      const mid = Math.floor(subArr.length / 2);
      const left = mergeSort(subArr.slice(0, mid));
      const right = mergeSort(subArr.slice(mid));
      
      // Count step
      let q = 0;
      for (let p = 0; p < left.length; p++) {
        const threshold = left[p].val - T;
        while (q < right.length && right[q].val < threshold) {
          q++;
        }
        counts[left[p].idx] += (right.length - q);
      }
      
      // Merge step
      const res = [];
      let i = 0, j = 0;
      while (i < left.length && j < right.length) {
        if (left[i].val <= right[j].val) {
          res.push(left[i++]);
        } else {
          res.push(right[j++]);
        }
      }
      while (i < left.length) res.push(left[i++]);
      while (j < right.length) res.push(right[j++]);
      return res;
    };
    
    mergeSort(pairs);
    return counts;
  }
}
