const readline = require("readline");

class Solution {
  maxOppositeParityGap(n, values, left, right) {
    if (n === 0) return 0;
    
    let maxDiff = 0;
    
    // Use null for uninitialized
    const dfs = (u, depth, minE, maxE, minO, maxO) => {
      if (u === -1) return;
      
      const val = values[u];
      
      let nextMinE = minE;
      let nextMaxE = maxE;
      let nextMinO = minO;
      let nextMaxO = maxO;
      
      if (depth % 2 === 0) {
        // Even
        if (minO !== null) {
          maxDiff = Math.max(maxDiff, Math.abs(val - minO));
          maxDiff = Math.max(maxDiff, Math.abs(val - maxO));
        }
        nextMinE = (minE === null) ? val : Math.min(minE, val);
        nextMaxE = (maxE === null) ? val : Math.max(maxE, val);
      } else {
        // Odd
        if (minE !== null) {
          maxDiff = Math.max(maxDiff, Math.abs(val - minE));
          maxDiff = Math.max(maxDiff, Math.abs(val - maxE));
        }
        nextMinO = (minO === null) ? val : Math.min(minO, val);
        nextMaxO = (maxO === null) ? val : Math.max(maxO, val);
      }
      
      if (left[u] !== -1) dfs(left[u], depth + 1, nextMinE, nextMaxE, nextMinO, nextMaxO);
      if (right[u] !== -1) dfs(right[u], depth + 1, nextMinE, nextMaxE, nextMinO, nextMaxO);
    };
    
    dfs(0, 0, values[0], values[0], null, null);
    return maxDiff;
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
  const values = new Array(n);
  const left = new Array(n);
  const right = new Array(n);
  for (let i = 0; i < n; i++) {
    values[i] = parseInt(data[idx++], 10);
    left[i] = parseInt(data[idx++], 10);
    right[i] = parseInt(data[idx++], 10);
  }

  const solution = new Solution();
  console.log(solution.maxOppositeParityGap(n, values, left, right).toString());
});
