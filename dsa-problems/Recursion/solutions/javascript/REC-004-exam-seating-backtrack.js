class Solution {
  countArrangements(n, k, d) {
    const memo = new Map();

    const solve = (idx, remainingK) => {
      if (remainingK === 0) return 1;
      if (idx >= n) return 0;

      const key = ``idx,`{remainingK}`;
      if (memo.has(key)) return memo.get(key);

      // Option 1: Place student here
      // Next valid position is idx + 1 + d
      let count = solve(idx + 1 + d, remainingK - 1);

      // Option 2: Skip this seat
      count += solve(idx + 1, remainingK);

      memo.set(key, count);
      return count;
    };

    return solve(0, k);
  }
}
