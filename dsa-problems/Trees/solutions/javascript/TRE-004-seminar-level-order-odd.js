const readline = require("readline");

class Solution {
  oddDepthLevels(n, left, right, values) {
    if (n === 0) return [];
    
    const result = [];
    const q = [0];
    let depth = 0;
    
    while (q.length > 0) {
      const size = q.length;
      const currentLevel = [];
      const isOdd = (depth % 2 !== 0);
      
      for (let i = 0; i < size; i++) {
        const u = q.shift();
        
        if (isOdd) {
          currentLevel.push(values[u]);
        }
        
        if (left[u] !== -1) q.push(left[u]);
        if (right[u] !== -1) q.push(right[u]);
      }
      
      if (isOdd) {
        result.push(currentLevel);
      }
      depth++;
    }
    return result;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  
  if (n === 0) {
      console.log("");
      return;
  }
  
  const values = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }

  const solution = new Solution();
  const levels = solution.oddDepthLevels(n, left, right, values);
  if (levels.length === 0) {
    console.log("");
  } else {
    console.log(levels.map((lvl) => lvl.join(" ")).join("\n"));
  }
});
