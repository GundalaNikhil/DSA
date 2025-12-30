import java.util.*;

class Solution {
    private int rows, cols;
    private int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // U, D, L, R

    public List<int[]> findPath(int[][] grid, int T) {
        rows = grid.length;
        cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];
        List<int[]> path = new ArrayList<>();
        
        path.add(new int[]{0, 0});
        visited[0][0] = true;
        
        // Start DFS. Initial direction is -1 (none)
        if (dfs(0, 0, -1, 0, T, grid, visited, path)) {
            return path;
        }
        
        return new ArrayList<>();
    }

    private boolean dfs(int r, int c, int lastDir, int turns, int maxTurns, 
                       int[][] grid, boolean[][] visited, List<int[]> path) {
        if (r == rows - 1 && c == cols - 1) {
            return true;
        }

        for (int i = 0; i < 4; i++) {
            int nr = r + directions[i][0];
            int nc = c + directions[i][1];

            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !visited[nr][nc] && grid[nr][nc] == 0) {
                int newTurns = turns;
                if (lastDir != -1 && i != lastDir) {
                    newTurns++;
                }

                if (newTurns <= maxTurns) {
                    visited[nr][nc] = true;
                    path.add(new int[]{nr, nc});
                    if (dfs(nr, nc, i, newTurns, maxTurns, grid, visited, path)) {
                        return true;
                    }
                    path.remove(path.size() - 1);
                    visited[nr][nc] = false;
                }
            }
        }
        return false;
    }
}
