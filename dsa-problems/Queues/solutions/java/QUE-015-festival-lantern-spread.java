import java.util.*;

class Solution {
    public int minutesToLight(int[][] grid) {
        if (grid == null || grid.length == 0) return 0;

        int r = grid.length;
        int c = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int freshCount = 0;

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[i][j] == 1) {
                    queue.offer(new int[]{i, j});
                } else {
                    freshCount++;
                }
            }
        }

        if (freshCount == 0) return 0;
        if (queue.isEmpty()) return -1;

        int minutes = 0;
        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while (!queue.isEmpty() && freshCount > 0) {
            minutes++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] curr = queue.poll();
                for (int[] d : dirs) {
                    int ni = curr[0] + d[0];
                    int nj = curr[1] + d[1];

                    if (ni >= 0 && ni < r && nj >= 0 && nj < c && grid[ni][nj] == 0) {
                        grid[ni][nj] = 1; // Mark as lit
                        freshCount--;
                        queue.offer(new int[]{ni, nj});
                    }
                }
            }
        }

        return freshCount == 0 ? minutes : -1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int r = sc.nextInt();
            int c = sc.nextInt();
            int[][] grid = new int[r][c];
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    grid[i][j] = sc.nextInt();
                }
            }
            
            Solution sol = new Solution();
            System.out.println(sol.minutesToLight(grid));
        }
    }
}
