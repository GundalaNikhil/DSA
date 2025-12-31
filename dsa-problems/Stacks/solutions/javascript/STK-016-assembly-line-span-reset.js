class Solution {
  spans(counts) {
    const n = counts.length;
    const result = new Int32Array(n);
    const stack = [];
    
    for (let i = 0; i < n; i++) {
      while (stack.length > 0 && counts[stack[stack.length - 1]] < counts[i]) {
        stack.pop();
      }
      
      if (stack.length === 0) {
        result[i] = i + 1;
      } else {
        result[i] = i - stack[stack.length - 1];
      }
      
      stack.push(i);
    }
    
    return Array.from(result);
  }
}
