const readline = require("readline");

class Solution {
  matrixGame(n, m, matrix) {
    const memo = new Map();

    const solve = (r1, r2, c1, c2) => {
      const key = `${r1},${r2},${c1},${c2}`;
      if (memo.has(key)) return memo.get(key);

      if (r1 === r2 && c1 === c2) return matrix[r1][c1];

      const movesMade = (n - (r2 - r1 + 1)) + (m - (c2 - c1 + 1));
      const isMax = (movesMade % 2 === 0);

      let res;
      if (isMax) {
        res = -Infinity;
        if (r1 < r2) {
          res = Math.max(res, solve(r1 + 1, r2, c1, c2));
          res = Math.max(res, solve(r1, r2 - 1, c1, c2));
        }
        if (c1 < c2) {
          res = Math.max(res, solve(r1, r2, c1 + 1, c2));
          res = Math.max(res, solve(r1, r2, c1, c2 - 1));
        }
      } else {
        res = Infinity;
        if (r1 < r2) {
          res = Math.min(res, solve(r1 + 1, r2, c1, c2));
          res = Math.min(res, solve(r1, r2 - 1, c1, c2));
        }
        if (c1 < c2) {
          res = Math.min(res, solve(r1, r2, c1 + 1, c2));
          res = Math.min(res, solve(r1, r2, c1, c2 - 1));
        }
      }

      memo.set(key, res);
      return res;
    };

    return solve(0, n - 1, 0, m - 1);
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
  
  const flatData = [];
  data.forEach(line => {
      line.trim().split(/\s+/).forEach(part => {
          if (part) flatData.push(part);
      });
  });
  
  if (flatData.length === 0) return;
  
  let idx = 0;
  const n = parseInt(flatData[idx++]);
  const m = parseInt(flatData[idx++]);
  
  const matrix = [];
  for (let i = 0; i < n; i++) {
      const row = [];
      for (let j = 0; j < m; j++) {
          row.push(parseInt(flatData[idx++]));
      }
      matrix.push(row);
  }

  const solution = new Solution();
  console.log(solution.matrixGame(n, m, matrix));
});
