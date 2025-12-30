class Solution {
  findPath(grid, T) {
    const rows = grid.length;
    const cols = grid[0].length;
    const visited = Array.from({ length: rows }, () => Array(cols).fill(false));
    const path = [[0, 0]];
    visited[0][0] = true;
    
    const dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]; // U, D, L, R

    const dfs = (r, c, lastDir, turns) => {
      if (r === rows - 1 && c === cols - 1) return true;

      for (let i = 0; i < 4; i++) {
        const [dr, dc] = dirs[i];
        const nr = r + dr;
        const nc = c + dc;

        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !visited[nr][nc] && grid[nr][nc] === 0) {
          let newTurns = turns;
          if (lastDir !== -1 && i !== lastDir) newTurns++;

          if (newTurns <= T) {
            visited[nr][nc] = true;
            path.push([nr, nc]);
            if (dfs(nr, nc, i, newTurns)) return true;
            path.pop();
            visited[nr][nc] = false;
          }
        }
      }
      return false;
    };

    if (dfs(0, 0, -1, 0)) return path;
    return [];
  }
}
