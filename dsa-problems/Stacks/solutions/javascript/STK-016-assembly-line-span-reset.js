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
  const counts = [];
  for (let i = 0; i < n; i++) {
    counts.push(parseInt(data[idx++], 10));
  }
  
  const solution = new Solution();
  const res = solution.spans(counts);
  console.log(res.join("\n"));
});
