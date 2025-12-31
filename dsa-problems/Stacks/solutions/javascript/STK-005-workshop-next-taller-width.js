class Solution {
  nextTallerWithin(h, w) {
    const n = h.length;
    const result = new Int32Array(n).fill(-1);
    const stack = []; // Stores indices
    
    for (let i = n - 1; i >= 0; i--) {
      while (stack.length > 0 && h[stack[stack.length - 1]] <= h[i]) {
        stack.pop();
      }
      
      if (stack.length > 0) {
        const j = stack[stack.length - 1];
        if (j - i <= w) {
          result[i] = h[j];
        } else {
          result[i] = -1;
        }
      }
      
      stack.push(i);
    }
    
    return Array.from(result);
  }
}
