class Solution {
  countUnsafe(d) {
    let unsafeCount = 0;
    for (let i = 0; i < d.length - 1; i++) {
      if (d[i] < d[i+1]) {
        unsafeCount++;
      }
    }
    return unsafeCount;
  }
}
