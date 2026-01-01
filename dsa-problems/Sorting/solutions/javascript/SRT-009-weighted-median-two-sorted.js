class Solution {
  weightedMedian(A, B, wA, wB) {
    const combined = A.concat(B).slice();
    combined.sort((a, b) => a - b);

    const n = combined.length;
    if (n % 2 === 1) {
      return combined[Math.floor(n / 2)].toString();
    }

    const mid1 = combined[n / 2 - 1];
    const mid2 = combined[n / 2];
    const avg = Math.floor((mid1 + mid2) / 2);
    return avg.toString();
  }
}
