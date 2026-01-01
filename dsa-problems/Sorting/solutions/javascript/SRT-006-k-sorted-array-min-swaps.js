class Solution {
  minSwapsToSort(arr, k = 0) {
    const pairs = arr.map((val, idx) => ({ val, idx }));
    pairs.sort((a, b) => a.val - b.val);

    let violations = 0;
    for (let targetIdx = 0; targetIdx < pairs.length; targetIdx++) {
      const originalIdx = pairs[targetIdx].idx;
      if (Math.abs(targetIdx - originalIdx) > k) {
        violations++;
      }
    }

    return Math.floor(violations / 2);
  }
}
