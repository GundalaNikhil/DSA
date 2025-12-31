class Solution {
  validate(push, pushT, pop, popT, windows, priority) {
    const n = push.length;
    const stack = [];
    const timeStack = [];
    const minPriorityStack = [];
    
    let j = 0;
    
    for (let i = 0; i < n; i++) {
      const val = push[i];
      const time = pushT[i];
      
      stack.push(val);
      timeStack.push(time);
      
      let currentMin = minPriorityStack.length === 0 ? Infinity : minPriorityStack[minPriorityStack.length - 1];
      if (priority.has(val)) {
        currentMin = Math.min(currentMin, val);
      }
      minPriorityStack.push(currentMin);
      
      while (stack.length > 0 && j < n && stack[stack.length - 1] === pop[j]) {
        const poppedVal = stack.pop();
        const pushedTime = timeStack.pop();
        minPriorityStack.pop();
        
        const poppedTime = popT[j];
        
        // Check Time
        if (windows.has(poppedVal)) {
          if (poppedTime - pushedTime > windows.get(poppedVal)) {
            return false;
          }
        }
        
        // Check Priority
        if (!priority.has(poppedVal)) {
          const minP = minPriorityStack.length === 0 ? Infinity : minPriorityStack[minPriorityStack.length - 1];
          if (poppedVal > minP) {
            return false;
          }
        }
        
        j++;
      }
    }
    
    return stack.length === 0;
  }
}
