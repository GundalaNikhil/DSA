class Solution {
  countWithinThreshold(arr, T) {
    const n = arr.length;
    const counts = new Array(n).fill(0);

    for (let i = 0; i < n; i++) {
      for (let j = i + 1; j < n; j++) {
        if (arr[j] - arr[i] <= T) {
          counts[i]++;
        }
      }
    }

    return counts;
  }
}
