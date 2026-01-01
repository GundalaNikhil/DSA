class Solution {
  validate(push, pushT, pop, popT, windows, priority) {
    const stack = [];
    const timeStack = [];
    const minPriorityStack = [];
    
    let j = 0;
    const n = push.length;
    
    for (let i = 0; i < n; i++) {
      const val = push[i];
      const t = pushT[i];
      
      stack.push(val);
      timeStack.push(t);
      
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
        
        // Check Time Window
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

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let lines = [];
rl.on("line", (line) => {
  lines.push(line);
});

rl.on("close", () => {
  if (lines.length === 0) return;
  
  let lineIdx = 0;
  const numPush = parseInt(lines[lineIdx++].trim(), 10);
  
  const push = [];
  const pushT = [];
  
  for (let i = 0; i < numPush; i++) {
    const parts = lines[lineIdx++].trim().split(/\s+/);
    push.push(parseInt(parts[0], 10));
    pushT.push(parseInt(parts[1], 10));
  }
  
  const numPop = parseInt(lines[lineIdx++].trim(), 10);
  const pop = [];
  const popT = [];
  
  for (let i = 0; i < numPop; i++) {
    const parts = lines[lineIdx++].trim().split(/\s+/);
    pop.push(parseInt(parts[0], 10));
    popT.push(parseInt(parts[1], 10));
  }
  
  const numWindows = parseInt(lines[lineIdx++].trim(), 10);
  const windows = new Map();
  
  for (let i = 0; i < numWindows; i++) {
    const parts = lines[lineIdx++].trim().split(/\s+/);
    windows.set(parseInt(parts[0], 10), parseInt(parts[1], 10));
  }
  
  const numPriority = parseInt(lines[lineIdx++].trim(), 10);
  const priority = new Set();
  
  for (let i = 0; i < numPriority; i++) {
    if (lineIdx < lines.length) {
       const l = lines[lineIdx++].trim();
       if (l) priority.add(parseInt(l, 10));
    }
  }
  
  const solution = new Solution();
  const res = solution.validate(push, pushT, pop, popT, windows, priority);
  console.log(res ? "YES" : "NO");
});
