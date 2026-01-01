class Solution {
  countPaths(r, c) {
    const memo = Array.from({ length: r }, () => Array(c).fill(-1));

    const helper = (i, j) => {
      if (i === 0 && j === 0) return 1;
      if (i < 0 || j < 0) return 0;

      if (memo[i][j] !== -1) return memo[i][j];

      // Use BigInt if numbers might exceed 2^53 - 1, though problem says 64-bit signed int
      // Standard JS numbers are doubles, safe up to 2^53. 
      // For R, C <= 25, result is C(48, 24) which is huge (~3e13), fits in Number.
      memo[i][j] = helper(i - 1, j) + helper(i, j - 1);
      return memo[i][j];
    };

    return helper(r - 1, c - 1);
  }
}










const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const r = parseInt(tokens[ptr++]);
    const c = parseInt(tokens[ptr++]);
    const sol = new Solution();
    console.log(sol.countPaths(r, c));
});
