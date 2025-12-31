class Solution {
  placeLights(n, k, d) {
    const result = [];

    const backtrack = (index, remainingK, currentPath) => {
      if (remainingK === 0) {
        result.push([...currentPath]);
        return;
      }
      if (index >= n) {
        return;
      }

      // Option 1: Place light here
      currentPath.push(index);
      backtrack(index + d, remainingK - 1, currentPath);
      currentPath.pop();

      // Option 2: Skip this spot
      backtrack(index + 1, remainingK, currentPath);
    };

    backtrack(0, k, []);
    return result;
  }
}
