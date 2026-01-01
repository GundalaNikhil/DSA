import java.util.*;

class Solution {
    private int[][] dirs = {{0,1}, {1,0}, {0,-1}, {-1,0}};

    public int shortestPath(List<String> grid) {
        if (grid == null || grid.isEmpty()) return -1;

        int rows = grid.size();
        int cols = grid.get(0).length();

        if (rows == 0 || cols == 0) return -1;
        if (rows == 1 && cols == 1) return 0;

        // Find start and end
        int startR = -1, startC = -1, endR = -1, endC = -1;
        int foodR = -1, foodC = -1;
        boolean hasFood = false;

        for (int i = 0; i < rows; i++) {
            String row = grid.get(i);
            for (int j = 0; j < Math.min(row.length(), cols); j++) {
                char cell = row.charAt(j);
                if (cell == 'S') {
                    startR = i;
                    startC = j;
                } else if (cell == 'E') {
                    endR = i;
                    endC = j;
                } else if (cell == 'F') {
                    foodR = i;
                    foodC = j;
                    hasFood = true;
                }
            }
        }

        if (startR == -1 || endR == -1) return -1;

        // BFS with state (r, c, has_visited_food)
        Queue<int[]> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        queue.offer(new int[]{startR, startC, 0, 0}); // r, c, has_food, dist
        visited.add(startR + "," + startC + ",0");

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0], c = curr[1], foodState = curr[2], dist = curr[3];

            // Check if at end with food
            if (r == endR && c == endC && foodState == 1) {
                return dist;
            }

            for (int[] dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];

                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;

                String cell = grid.get(nr);
                if (nc >= cell.length()) continue;

                char cellChar = cell.charAt(nc);
                if (cellChar == '#') continue;

                int newFoodState = foodState;
                if (cellChar == 'F') {
                    newFoodState = 1;
                }

                String key = nr + "," + nc + "," + newFoodState;
                if (!visited.contains(key)) {
                    visited.add(key);
                    queue.offer(new int[]{nr, nc, newFoodState, dist + 1});
                }
            }
        }

        return -1;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            int r = sc.nextInt();
            int c = sc.nextInt();
            sc.nextLine(); // consume newline

            List<String> grid = new ArrayList<>();
            for (int i = 0; i < r; i++) {
                if (sc.hasNextLine()) {
                    String line = sc.nextLine();
                    grid.add(line);
                } else {
                    grid.add("");
                }
            }

            Solution solution = new Solution();
            int result = solution.shortestPath(grid);
            System.out.println(result);
        } finally {
            sc.close();
        }
    }
}
