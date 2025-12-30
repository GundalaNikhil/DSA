class Solution {
  countAssignments(nums, K, target) {
    const n = nums.length;

    const backtrack = (index, currentSum, negations) => {
      if (index === n) {
        return currentSum === target ? 1 : 0;
      }

      let count = 0;

      // Option 1: +
      count += backtrack(index + 1, currentSum + nums[index], negations);

      // Option 2: -
      if (negations < K) {
        count += backtrack(index + 1, currentSum - nums[index], negations + 1);
      }

      return count;
    };

    return backtrack(0, 0, 0);
  }
}
