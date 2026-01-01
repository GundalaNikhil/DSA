class Solution {
  sortWithSwaps(arr, S) {
    const n = arr.length;
    let count0 = 0;
    let count1 = 0;
    for (const v of arr) {
      if (v === 0) count0++;
      else if (v === 1) count1++;
    }

    let misplaced = 0;
    for (let i = 0; i < n; i++) {
      if (arr[i] === 0 && i >= count0) {
        misplaced++;
      } else if (arr[i] === 1 && (i < count0 || i >= count0 + count1)) {
        misplaced++;
      } else if (arr[i] === 2 && i < count0 + count1) {
        misplaced++;
      }
    }

    const swapsNeeded = Math.floor(misplaced / 2);
    return swapsNeeded <= S;
  }
}
