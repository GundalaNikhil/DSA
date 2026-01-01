const readline = require("readline");

class Solution {
  shortestPath(grid) {
    if (!grid || grid.length === 0) return -1;

    const rows = grid.length;
    const cols = grid[0].length;

    let start = null;

    // Find starting position
    for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
        if (grid[i][j] === 'S') {
          start = [i, j];
          break;
        }
      }
      if (start) break;
    }

    if (!start) return -1;

    // State: [r, c, hasFood, dist]
    const queue = [[start[0], start[1], 0, 0]];
    const visited = new Set([`${start[0]},${start[1]},0`]);
    const dirs = [[0,1], [1,0], [0,-1], [-1,0]];

    while (queue.length > 0) {
      const [r, c, hasFood, dist] = queue.shift();

      // Check current cell
      if (r < 0 || r >= rows || c < 0 || c >= cols) continue;

      const cell = grid[r][c];
      const currentHasFood = (cell === 'F' || hasFood) ? 1 : 0;

      // Check if reached exit with food
      if (cell === 'E' && currentHasFood) {
        return dist;
      }

      // Explore neighbors
      for (const [dr, dc] of dirs) {
        const nr = r + dr;
        const nc = c + dc;

        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] !== '#') {
          const key = `${nr},${nc},${currentHasFood}`;
          if (!visited.has(key)) {
            visited.add(key);
            queue.push([nr, nc, currentHasFood, dist + 1]);
          }
        }
      }
    }

    return -1;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  // Filter out empty lines
  const validLines = data.filter(line => line.length > 0);

  if (validLines.length === 0) return;

  try {
    // Parse header (r c)
    const header = validLines[0].split(/\s+/);
    if (header.length < 2) return;
    const r = Number(header[0]);
    const c = Number(header[1]);

    // Parse grid - safely handle missing lines
    const grid = [];
    for (let i = 0; i < r; i++) {
      if (i + 1 < validLines.length) {
        grid.push(validLines[i+1].split(''));
      } else {
        grid.push([]); // Empty row filler for missing lines
      }
    }

      // Only run algorithm if we have a complete grid
    if (grid.length === r) {
      const solution = new Solution();
      console.log(solution.shortestPath(grid));
    }
  } catch (e) {
    // Silently handle parse errors
  }
});
