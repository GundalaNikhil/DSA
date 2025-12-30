class Solution {
  solveKenKen(cages) {
    const grid = Array.from({ length: 4 }, () => Array(4).fill(0));
    const cageMap = Array.from({ length: 4 }, () => Array(4).fill(null));
    
    // Process cages
    const processedCages = cages.map((data, idx) => {
      const target = data[0];
      const op = String.fromCharCode(data[1]);
      const len = data[2];
      const coords = [];
      for (let j = 0; j < len; j++) {
        const r = data[3 + 2 * j];
        const c = data[4 + 2 * j];
        coords.push([r, c]);
        cageMap[r][c] = idx;
      }
      return { target, op, coords };
    });

    const isValid = (r, c, v) => {
      for (let j = 0; j < 4; j++) if (grid[r][j] === v) return false;
      for (let i = 0; i < 4; i++) if (grid[i][c] === v) return false;
      return true;
    };

    const checkCage = (r, c) => {
      const cageIdx = cageMap[r][c];
      const { target, op, coords } = processedCages[cageIdx];
      
      const values = [];
      for (const [rr, cc] of coords) {
        if (grid[rr][cc] === 0) return true; // Not full
        values.push(grid[rr][cc]);
      }

      if (op === '+') {
        return values.reduce((a, b) => a + b, 0) === target;
      } else if (op === '*') {
        return values.reduce((a, b) => a * b, 1) === target;
      } else if (op === '-') {
        return Math.abs(values[0] - values[1]) === target;
      } else if (op === '/') {
        const [a, b] = values;
        return (a % b === 0 && a / b === target) || (b % a === 0 && b / a === target);
      } else if (op === '=') {
        return values[0] === target;
      }
      return false;
    };

    const backtrack = (r, c) => {
      if (r === 4) return true;

      const nextR = c === 3 ? r + 1 : r;
      const nextC = c === 3 ? 0 : c + 1;

      for (let v = 1; v <= 4; v++) {
        if (isValid(r, c, v)) {
          grid[r][c] = v;
          if (checkCage(r, c)) {
            if (backtrack(nextR, nextC)) return true;
          }
          grid[r][c] = 0;
        }
      }
      return false;
    };

    if (backtrack(0, 0)) return grid;
    return [];
  }
}
