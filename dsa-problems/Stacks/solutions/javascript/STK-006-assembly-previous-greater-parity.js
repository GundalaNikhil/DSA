class Solution {
  prevGreaterOppositeParity(arr) {
    const n = arr.length;
    const result = new Int32Array(n).fill(-1);
    
    const evenStack = [];
    const oddStack = [];
    
    const findNearestGreater = (stack, val) => {
      if (stack.length === 0) return -1;
      
      let l = 0;
      let r = stack.length - 1;
      let ansIdx = -1;
      
      while (l <= r) {
        const mid = Math.floor((l + r) / 2);
        if (arr[stack[mid]] > val) {
          ansIdx = stack[mid];
          l = mid + 1;
        } else {
          r = mid - 1;
        }
      }
      return ansIdx;
    };
    
    for (let i = 0; i < n; i++) {
      const val = arr[i];
      
      if (val % 2 === 0) {
        const idx = findNearestGreater(oddStack, val);
        if (idx !== -1) result[i] = arr[idx];
        
        while (evenStack.length > 0 && arr[evenStack[evenStack.length - 1]] <= val) {
          evenStack.pop();
        }
        evenStack.push(i);
      } else {
        const idx = findNearestGreater(evenStack, val);
        if (idx !== -1) result[i] = arr[idx];
        
        while (oddStack.length > 0 && arr[oddStack[oddStack.length - 1]] <= val) {
          oddStack.pop();
        }
        oddStack.push(i);
      }
    }
    
    return Array.from(result);
  }
}
