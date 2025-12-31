class Solution {
  minSwapsToSort(arr) {
    const n = arr.length;
    const pairs = arr.map((val, idx) => ({ val, idx }));
    
    // Sort pairs
    pairs.sort((a, b) => a.val - b.val);
    
    const visited = new Array(n).fill(false);
    let swaps = 0;
    
    for (let i = 0; i < n; i++) {
      if (visited[i] || pairs[i].idx === i) {
        continue;
      }
      
      let cycleSize = 0;
      let j = i;
      while (!visited[j]) {
        visited[j] = true;
        j = pairs[j].idx;
        cycleSize++;
      }
      
      if (cycleSize > 0) {
        swaps += (cycleSize - 1);
      }
    }
    
    return swaps;
  }
}
