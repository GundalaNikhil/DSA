import java.util.*;

class Solution {
    private int rows, cols;
    private int[][] moves = {
        {-2, -1}, {-2, 1}, {-1, -2}, {-1, 2},
        {1, -2}, {1, 2}, {2, -1}, {2, 1}
    };

    public List<int[]> knightTour(int n, boolean[][] blocked) {
        rows = n;
        cols = n;
        int totalUnblocked = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!blocked[i][j]) totalUnblocked++;
            }
        }

        boolean[][] visited = new boolean[n][n];
        List<int[]> path = new ArrayList<>();
        
        // Start at 0,0
        visited[0][0] = true;
        path.add(new int[]{0, 0});
        
        if (dfs(0, 0, 1, totalUnblocked, blocked, visited, path)) {
            return path;
        }
        
        return new ArrayList<>();
    }

    private boolean dfs(int r, int c, int count, int target, boolean[][] blocked, 
                       boolean[][] visited, List<int[]> path) {
        if (count == target) {
            return true;
        }

        for (int[] m : moves) {
            int nr = r + m[0];
            int nc = c + m[1];

            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !blocked[nr][nc] && !visited[nr][nc]) {
                visited[nr][nc] = true;
                path.add(new int[]{nr, nc});
                if (dfs(nr, nc, count + 1, target, blocked, visited, path)) {
                    return true;
                }
                path.remove(path.size() - 1);
                visited[nr][nc] = false;
            }
        }
        return false;
    }
}
