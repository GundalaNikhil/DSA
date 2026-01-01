const readline = require("readline");

class Solution {
  fireSpreadTime(grid, stamina) {
    const rows = grid.length;
    const cols = grid[0].length;
    const queue = [];
    const ignited = new Set();

    // Initialize with fire sources
    for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
        if (grid[i][j] === 2) {
          const s = (i < stamina.length && j < stamina[i].length) ? stamina[i][j] : 0;
          queue.push([i, j, s, 0]);
          ignited.add(`${i},${j}`);
        }
      }
    }

    let maxTime = 0;
    const dirs = [[0,1], [1,0], [0,-1], [-1,0]];

    while (queue.length > 0) {
      const [r, c, stam, time] = queue.shift();
      maxTime = Math.max(maxTime, time);

      if (stam > 0) {
        for (const [dr, dc] of dirs) {
          const nr = r + dr;
          const nc = c + dc;
          const key = `${nr},${nc}`;

          if (nr >= 0 && nr < rows && nc >= 0 && nc < cols &&
              grid[nr][nc] === 0 && !ignited.has(key)) {
            ignited.add(key);
            queue.push([nr, nc, stam - 1, time + 1]);
          }
        }
      }
    }

    // Check if all empty cells ignited
    for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
        if (grid[i][j] === 0 && !ignited.has(`${i},${j}`)) {
          return -1;
        }
      }
    }

    return maxTime;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  const tokens = data.join(" ").split(/\s+/).filter(t => t.length > 0);
  if (tokens.length === 0) return;

  let ptr = 0;
  const r = Number(tokens[ptr++]);
  const c = Number(tokens[ptr++]);

  // Check if we have enough tokens for the grid
  if (ptr + r * c > tokens.length) return; // Incomplete grid input

  const grid = [];
  for (let i = 0; i < r; i++) {
    const row = [];
    for (let j = 0; j < c; j++) {
      if (ptr < tokens.length) {
        row.push(Number(tokens[ptr++]));
      } else {
        return; // Incomplete input
      }
    }
    grid.push(row);
  }

  // Check if we have stamina grid
  if (ptr + r * c > tokens.length) return; // Incomplete stamina grid

  const stamina = [];
  for (let i = 0; i < r; i++) {
    const row = [];
    for (let j = 0; j < c; j++) {
      if (ptr < tokens.length) {
        row.push(Number(tokens[ptr++]));
      } else {
        row.push(0); // Use default stamina if missing
      }
    }
    stamina.push(row);
  }

  const solution = new Solution();
  console.log(solution.fireSpreadTime(grid, stamina));
});
