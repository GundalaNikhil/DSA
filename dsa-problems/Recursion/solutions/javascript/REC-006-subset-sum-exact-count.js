class Solution {
  findSubset(arr, k, target) {
    const result = [];
    const n = arr.length;

    const backtrack = (index, count, currentSum) => {
      if (count === k) {
        return currentSum === target;
      }
      if (index === n) {
        return false;
      }

      // Pruning
      if (n - index < k - count) {
        return false;
      }

      // Option 1: Include
      result.push(arr[index]);
      if (backtrack(index + 1, count + 1, currentSum + arr[index])) {
        return true;
      }
      result.pop();

      // Option 2: Exclude
      if (backtrack(index + 1, count, currentSum)) {
        return true;
      }

      return false;
    };

    if (backtrack(0, 0, 0)) {
      return result;
    }
    return [];
  }
}
