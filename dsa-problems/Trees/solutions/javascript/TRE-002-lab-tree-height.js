const readline = require("readline");

class Solution {
  treeHeight(n, left, right) {
    if (n === 0) return -1;
    
    const dfs = (u) => {
      if (u === -1) return -1;
      const lHeight = dfs(left[u]);
      const rHeight = dfs(right[u]);
      return 1 + Math.max(lHeight, rHeight);
    };
    
    return dfs(0);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => {
  const parts = line.trim().split(/\s+/);
  for (const part of parts) {
    if (part) data.push(part);
  }
});

rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  
  if (n === 0) {
      console.log("-1");
      return;
  }
  
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    idx++; // value
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }

  const solution = new Solution();
  console.log(solution.treeHeight(n, left, right).toString());
});
