class Solution {
  spans(demand) {
    const n = demand.length;
    const result = new Int32Array(n);
    const stack = []; // Stores indices
    
    for (let i = 0; i < n; i++) {
      while (stack.length > 0 && demand[stack[stack.length - 1]] < demand[i]) {
        stack.pop();
      }
      
      const prevIdx = stack.length === 0 ? -1 : stack[stack.length - 1];
      result[i] = i - prevIdx - 1;
      
      stack.push(i);
    }
    
    return Array.from(result);
  }
}
