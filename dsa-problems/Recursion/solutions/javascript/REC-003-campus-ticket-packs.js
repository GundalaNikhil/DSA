class Solution {
  packCombinations(values, packs, target) {
    const results = [];
    const n = values.length;

    const backtrack = (idx, currentSum, currentItems) => {
      if (currentSum === target) {
        // Create a copy and sort it
        results.push([...currentItems].sort((a, b) => a - b));
        return;
      }
      if (idx === n || currentSum > target) {
        return;
      }

      // Option 1: Include
      const packVal = values[idx];
      const packSize = packs[idx];
      const totalVal = packVal * packSize;

      if (currentSum + totalVal <= target) {
        const nextItems = [...currentItems];
        for (let k = 0; k < packSize; k++) nextItems.push(packVal);
        backtrack(idx + 1, currentSum + totalVal, nextItems);
      }

      // Option 2: Exclude
      backtrack(idx + 1, currentSum, currentItems);
    };

    backtrack(0, 0, []);

    // Deduplicate
    const uniqueSet = new Set();
    const uniqueResults = [];
    
    for (const res of results) {
      const key = res.join(",");
      if (!uniqueSet.has(key)) {
        uniqueSet.add(key);
        uniqueResults.push(res);
      }
    }

    // Sort results lexicographically
    uniqueResults.sort((a, b) => {
      for (let i = 0; i < Math.min(a.length, b.length); i++) {
        if (a[i] !== b[i]) return a[i] - b[i];
      }
      return a.length - b.length;
    });

    return uniqueResults;
  }
}
