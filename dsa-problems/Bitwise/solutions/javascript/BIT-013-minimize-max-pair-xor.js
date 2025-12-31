const readline = require("readline");

class Solution {
  minimizeMaxPairXor(a) {
    const n = a.length;
    const memo = new Int32Array(1 << n).fill(-1);
    
    const solve = (mask) => {
      if (mask === (1 << n) - 1) return 0;
      if (memo[mask] !== -1) return memo[mask];
      
      let res = 2000000000; // Infinity
      
      let i = 0;
      while ((mask >> i) & 1) i++;
      
      for (let j = i + 1; j < n; j++) {
        if (!((mask >> j) & 1)) {
          const val = a[i] ^ a[j];
          const sub = solve(mask | (1 << i) | (1 << j));
          res = Math.min(res, Math.max(val, sub));
        }
      }
      
      memo[mask] = res;
      return res;
    };
    
    return solve(0);
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
    if (data.length === 0) return;
    const tokens = data.join(" ").split(/\s+/);
    if (tokens.length === 0 || tokens[0] === "") return;
    
    let ptr = 0;
    const n = Number(tokens[ptr++]);
    const a = [];
    for (let i = 0; i < n; i++) a.push(Number(tokens[ptr++]));
    
    const solution = new Solution();
    console.log(solution.minimizeMaxPairXor(a));
});
