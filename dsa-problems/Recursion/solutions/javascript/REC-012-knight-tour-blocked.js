class Solution {
  knightTour(n, blocked) {
    let totalUnblocked = 0;
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (!blocked[i][j]) totalUnblocked++;
      }
    }

    const visited = Array.from({ length: n }, () => Array(n).fill(false));
    const path = [[0, 0]];
    visited[0][0] = true;

    const moves = [
      [-2, -1], [-2, 1], [-1, -2], [-1, 2],
      [1, -2], [1, 2], [2, -1], [2, 1]
    ];

    const dfs = (r, c, count) => {
      if (count === totalUnblocked) return true;

      for (const [dr, dc] of moves) {
        const nr = r + dr;
        const nc = c + dc;

        if (nr >= 0 && nr < n && nc >= 0 && nc < n && !blocked[nr][nc] && !visited[nr][nc]) {
          visited[nr][nc] = true;
          path.push([nr, nc]);
          if (dfs(nr, nc, count + 1)) return true;
          path.pop();
          visited[nr][nc] = false;
        }
      }
      return false;
    };

    if (dfs(0, 0, 1)) return path;
    return [];
  }
}
