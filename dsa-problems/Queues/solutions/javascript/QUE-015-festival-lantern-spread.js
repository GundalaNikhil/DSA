const readline = require("readline");

class Solution {
  minutesToLight(grid) {
    if (!grid || grid.length === 0) return 0;

    const r = grid.length;
    const c = grid[0].length;
    const queue = [];
    let freshCount = 0;

    for (let i = 0; i < r; i++) {
      for (let j = 0; j < c; j++) {
        if (grid[i][j] === 1) {
          queue.push([i, j]);
        } else {
          freshCount++;
        }
      }
    }

    if (freshCount === 0) return 0;
    if (queue.length === 0) return -1;

    let minutes = 0;
    const dirs = [
      [-1, 0],
      [1, 0],
      [0, -1],
      [0, 1],
    ];
    let head = 0;

    while (head < queue.length && freshCount > 0) {
      minutes++;
      const size = queue.length - head;
      for (let i = 0; i < size; i++) {
        const [x, y] = queue[head++];

        for (const [dx, dy] of dirs) {
          const nx = x + dx;
          const ny = y + dy;

          if (nx >= 0 && nx < r && ny >= 0 && ny < c && grid[nx][ny] === 0) {
            grid[nx][ny] = 1;
            freshCount--;
            queue.push([nx, ny]);
          }
        }
      }
    }

    return freshCount === 0 ? minutes : -1;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x !== "")));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const remaining = data.slice(idx);

  let grid;

  // If we have exactly n remaining values, treat as 1D grid (1 x n)
  if (remaining.length === n) {
    grid = [remaining.map(x => parseInt(x, 10))];
  } else if (remaining.length > n) {
    // Check if we have r and c explicitly
    const r = n;
    const c = parseInt(remaining[0], 10);
    if (remaining.length >= r * c) {
      grid = [];
      let pos = 1;
      for (let i = 0; i < r; i++) {
        const row = [];
        for (let j = 0; j < c; j++) {
          row.push(parseInt(remaining[pos++], 10));
        }
        grid.push(row);
      }
    } else {
      // Fallback: treat as 1D
      grid = [remaining.slice(0, n).map(x => parseInt(x, 10))];
    }
  } else {
    // Fallback: treat as 1D
    grid = [remaining.map(x => parseInt(x, 10))];
  }

  const solution = new Solution();
  console.log(solution.minutesToLight(grid));
});
