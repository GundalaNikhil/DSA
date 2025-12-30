import java.util.*;

class Solution {
    private int[][] dirs = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    
    public int fireSpreadTime(int[][] grid, int[][] stamina) {
        int rows = grid.length;
        int cols = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        Set<String> ignited = new HashSet<>();
        
        // Initialize with fire sources
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 2) {
                    queue.offer(new int[]{i, j, stamina[i][j], 0});
                    ignited.add(i + "," + j);
                }
            }
        }
        
        int maxTime = 0;
        
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0], c = curr[1], stam = curr[2], time = curr[3];
            maxTime = Math.max(maxTime, time);
            
            if (stam > 0) {
                for (int[] dir : dirs) {
                    int nr = r + dir[0];
                    int nc = c + dir[1];
                    String key = nr + "," + nc;
                    
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && 
                        grid[nr][nc] == 0 && !ignited.contains(key)) {
                        ignited.add(key);
                        queue.offer(new int[]{nr, nc, stam - 1, time + 1});
                    }
                }
            }
        }
        
        // Check if all empty cells ignited
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 0 && !ignited.contains(i + "," + j)) {
                    return -1;
                }
            }
        }
        
        return maxTime;
    }
}
