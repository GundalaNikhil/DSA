class Solution {
  reduce(s, w) {
    const stack = [];
    let totalRemoved = 0;
    
    for (let i = 0; i < s.length; i++) {
      const char = s[i];
      const weight = w[i];
      
      if (stack.length > 0 && 
          stack[stack.length - 1].char === char && 
          (stack[stack.length - 1].weight + weight) % 2 === 0) {
        totalRemoved += stack[stack.length - 1].weight + weight;
        stack.pop();
      } else {
        stack.push({ char, weight });
      }
    }
    
    let resS = "";
    for (const item of stack) {
      resS += item.char;
    }
    
    return [resS, totalRemoved];
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
  let s = "";
  const w = [];
  
  for (let i = 0; i < n; i++) {
    s += data[idx++];
    w.push(parseInt(data[idx++], 10));
  }
  
  const solution = new Solution();
  const res = solution.reduce(s, w);
  
  if (res[0] === "") {
    console.log(`EMPTY ${res[1]}`);
  } else {
    console.log(`${res[0]} ${res[1]}`);
  }
});
