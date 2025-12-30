import java.util.*;

class Solution {
    private int[][] dirs = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    
    public int shortestPathWithWalls(int[][] grid, int k) {
        int rows = grid.length;
        int cols = grid[0].length;
        
        if (rows == 1 && cols == 1) return 0;
        
        Queue<int[]> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        
        queue.offer(new int[]{0, 0, k, 0});
        visited.add("0,0," + k);
        
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0], c = curr[1], walls = curr[2], steps = curr[3];
            
            for (int[] dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
                
                int newWalls = walls - grid[nr][nc];
                String key = nr + "," + nc + "," + newWalls;
                
                if (newWalls >= 0 && !visited.contains(key)) {
                    if (nr == rows - 1 && nc == cols - 1) {
                        return steps + 1;
                    }
                    
                    visited.add(key);
                    queue.offer(new int[]{nr, nc, newWalls, steps + 1});
                }
            }
        }
        
        return -1;
    }
}
