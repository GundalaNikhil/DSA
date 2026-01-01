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

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            List<Integer> remaining = new ArrayList<>();
            while (sc.hasNextInt()) {
                remaining.add(sc.nextInt());
            }

            int[][] grid;

            // If we have exactly n remaining values, treat as 1D grid (1 x n)
            if (remaining.size() == n) {
                grid = new int[1][n];
                for (int i = 0; i < n; i++) {
                    grid[0][i] = remaining.get(i);
                }
            } else if (remaining.size() > n) {
                // Check if we have r and c explicitly
                int r = n;
                int c = remaining.get(0);
                if (remaining.size() >= r * c) {
                    grid = new int[r][c];
                    int pos = 1;
                    for (int i = 0; i < r; i++) {
                        for (int j = 0; j < c; j++) {
                            grid[i][j] = remaining.get(pos++);
                        }
                    }
                } else {
                    // Fallback: treat as 1D
                    grid = new int[1][n];
                    for (int i = 0; i < n && i < remaining.size(); i++) {
                        grid[0][i] = remaining.get(i);
                    }
                }
            } else {
                // Fallback: treat as 1D
                grid = new int[1][remaining.size()];
                for (int i = 0; i < remaining.size(); i++) {
                    grid[0][i] = remaining.get(i);
                }
            }

            Solution sol = new Solution();
            System.out.println(sol.minutesToLight(grid));
        }
    }
}
