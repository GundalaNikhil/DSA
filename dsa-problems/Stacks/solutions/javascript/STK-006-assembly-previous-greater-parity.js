class Solution {
  findNearestGreater(stack, val, arr) {
    if (stack.length === 0) return -1;
    
    let l = 0;
    let r = stack.length - 1;
    let ansIdx = -1;
    
    while (l <= r) {
      const mid = Math.floor((l + r) / 2);
      const idx = stack[mid];
      if (arr[idx] > val) {
        ansIdx = idx;
        l = mid + 1;
      } else {
        r = mid - 1;
      }
    }
    return ansIdx;
  }

  prevGreaterOppositeParity(arr) {
    const n = arr.length;
    const result = new Array(n).fill(-1);
    
    const evenStack = [];
    const oddStack = [];
    
    for (let i = 0; i < n; i++) {
      const val = arr[i];
      
      if (val % 2 === 0) {
        // Look in Odd
        const idx = this.findNearestGreater(oddStack, val, arr);
        if (idx !== -1) result[i] = arr[idx];
        
        // Update Even
        while (evenStack.length > 0 && arr[evenStack[evenStack.length - 1]] <= val) {
          evenStack.pop();
        }
        evenStack.push(i);
      } else {
        // Look in Even
        const idx = this.findNearestGreater(evenStack, val, arr);
        if (idx !== -1) result[i] = arr[idx];
        
        // Update Odd
        while (oddStack.length > 0 && arr[oddStack[oddStack.length - 1]] <= val) {
          oddStack.pop();
        }
        oddStack.push(i);
      }
    }
    return result;
  }
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/).filter(x => x !== "");
  for (const p of parts) data.push(p);
});

rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const arr = [];
  for (let i = 0; i < n; i++) {
    arr.push(parseInt(data[idx++], 10));
  }
  
  const solution = new Solution();
  const res = solution.prevGreaterOppositeParity(arr);
  console.log(res.join("\n"));
});
