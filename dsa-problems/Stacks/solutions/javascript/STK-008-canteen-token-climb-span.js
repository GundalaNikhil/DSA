class Solution {
  spans(demand) {
    const n = demand.length;
    const result = new Int32Array(n);
    const stack = []; // Stores indices
    
    for (let i = 0; i < n; i++) {
        while (stack.length > 0 && demand[stack[stack.length - 1]] < demand[i]) {
            stack.pop();
        }
        
        if (stack.length === 0) {
            result[i] = i;
        } else if (demand[stack[stack.length - 1]] === demand[i]) {
            result[i] = 0;
        } else {
            result[i] = i - stack[stack.length - 1] - 1;
        }
        
        stack.push(i);
    }
    
    return Array.from(result);
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
  const demand = [];
  for (let i = 0; i < n; i++) {
    demand.push(parseInt(data[idx++], 10));
  }
  
  const solution = new Solution();
  const res = solution.spans(demand);
  console.log(res.join("\n"));
});
