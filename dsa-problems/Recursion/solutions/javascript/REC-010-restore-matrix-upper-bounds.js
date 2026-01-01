class Solution {
  restoreMatrix(rowSums, colSums) {
    const R = rowSums.length;
    const C = colSums.length;
    const matrix = Array.from({ length: R }, () => Array(C).fill(0));

    // Clone sums to avoid mutation if we wanted to reuse input, 
    // but here we can mutate copies passed to recursion or just mutate input if allowed.
    // Let's use copies for safety in recursion logic.
    const rSums = [...rowSums];
    const cSums = [...colSums];

    const backtrack = (r, c) => {
      if (r === R) {
        return cSums.every((x) => x === 0);
      }

      const nextR = c === C - 1 ? r + 1 : r;
      const nextC = c === C - 1 ? 0 : c + 1;

      if (c === C - 1) {
        const val = rSums[r];
        if (val >= 0 && val <= cSums[c]) {
          matrix[r][c] = val;
          rSums[r] -= val;
          cSums[c] -= val;
          if (backtrack(nextR, nextC)) return true;
          rSums[r] += val;
          cSums[c] += val;
        }
        return false;
      }

      const maxVal = Math.min(rSums[r], cSums[c]);

      for (let val = maxVal; val >= 0; val--) {
        matrix[r][c] = val;
        rSums[r] -= val;
        cSums[c] -= val;
        if (backtrack(nextR, nextC)) return true;
        rSums[r] += val;
        cSums[c] += val;
      }
      return false;
    };

    if (backtrack(0, 0)) return matrix;
    return [];
  }
}










const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const R = parseInt(tokens[ptr++], 10);
    const C = parseInt(tokens[ptr++], 10);
    const rowSums = [];
    const colSums = [];
    for(let i=0; i<R; i++) rowSums.push(parseInt(tokens[ptr++], 10));
    for(let i=0; i<C; i++) colSums.push(parseInt(tokens[ptr++], 10));
    const sol = new Solution();
    const res = sol.restoreMatrix(rowSums, colSums);
    if (res.length === 0) {
        console.log("IMPOSSIBLE");
    } else {
        res.forEach(row => console.log(row.join(' ')));
    }
});
