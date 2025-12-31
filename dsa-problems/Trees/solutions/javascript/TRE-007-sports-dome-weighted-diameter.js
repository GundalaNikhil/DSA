const readline = require("readline");

class Solution {
  weightedDiameter(n, left, right, lw, rw) {
    if (n === 0) return 0;
    
    let maxDiameter = 0n;
    
    const dfs = (u) => {
      if (u === -1) return 0n;
      
      let lPath = 0n;
      let rPath = 0n;
      
      if (left[u] !== -1) {
        lPath = BigInt(lw[u]) + dfs(left[u]);
      }
      if (right[u] !== -1) {
        rPath = BigInt(rw[u]) + dfs(right[u]);
      }
      
      const currentDiameter = lPath + rPath;
      if (currentDiameter > maxDiameter) {
        maxDiameter = currentDiameter;
      }
      
      return lPath > rPath ? lPath : rPath;
    };
    
    dfs(0);
    return maxDiameter;
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
  const left = new Array(n);
  const right = new Array(n);
  const lw = new Array(n);
  const rw = new Array(n);
  for (let i = 0; i < n; i++) {
    idx++; // value
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
    lw[i] = parseInt(data[idx++], 10);
    rw[i] = parseInt(data[idx++], 10);
  }

  const solution = new Solution();
  console.log(solution.weightedDiameter(n, left, right, lw, rw).toString());
});
