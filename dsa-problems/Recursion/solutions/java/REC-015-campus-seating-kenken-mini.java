import java.util.*;

class Solution {
    private int[][] grid;
    private int[][] cageMap; // cell (r*4+c) -> cage index
    private List<int[]> cagesList;
    
    public int[][] solveKenKen(List<int[]> cages) {
        grid = new int[4][4];
        cageMap = new int[4][4];
        cagesList = cages;
        
        // Map each cell to its cage index
        for (int i = 0; i < cages.size(); i++) {
            int[] data = cages.get(i);
            int len = data[2];
            for (int j = 0; j < len; j++) {
                int r = data[3 + 2 * j];
                int c = data[4 + 2 * j];
                cageMap[r][c] = i;
            }
        }
        
        if (backtrack(0, 0)) {
            return grid;
        }
        return new int[0][0];
    }

    private boolean backtrack(int r, int c) {
        if (r == 4) return true;
        
        int nextR = (c == 3) ? r + 1 : r;
        int nextC = (c == 3) ? 0 : c + 1;
        
        for (int v = 1; v <= 4; v++) {
            if (isValid(r, c, v)) {
                grid[r][c] = v;
                // Check cage constraint if this is the last cell in the cage
                if (checkCage(r, c)) {
                    if (backtrack(nextR, nextC)) return true;
                }
                grid[r][c] = 0;
            }
        }
        return false;
    }

    private boolean isValid(int r, int c, int v) {
        // Check if value v exists in row r
        for (int j = 0; j < 4; j++) if (grid[r][j] == v) return false;
        // Check if value v exists in column c
        for (int i = 0; i < 4; i++) if (grid[i][c] == v) return false;
        return true;
    }

    private boolean checkCage(int r, int c) {
        int cageIdx = cageMap[r][c];
        int[] data = cagesList.get(cageIdx);
        int target = data[0];
        char op = (char) data[1];
        int len = data[2];
        
        List<Integer> values = new ArrayList<>();
        boolean full = true;
        
        for (int j = 0; j < len; j++) {
            int rr = data[3 + 2 * j];
            int cc = data[4 + 2 * j];
            if (grid[rr][cc] == 0) {
                full = false;
                break;
            }
            values.add(grid[rr][cc]);
        }
        
        if (!full) return true; // Not full yet, assume valid (or implement partial checks)

        // Full cage check
        if (op == '+') {
            int sum = 0;
            for (int x : values) sum += x;
            return sum == target;
        } else if (op == '*') {
            int prod = 1;
            for (int x : values) prod *= x;
            return prod == target;
        } else if (op == '-') {
            // len is 2
            return Math.abs(values.get(0) - values.get(1)) == target;
        } else if (op == '/') {
            // len is 2
            int a = values.get(0), b = values.get(1);
            return (a % b == 0 && a / b == target) || (b % a == 0 && b / a == target);
        } else if (op == '=') {
            return values.get(0) == target;
        }
        return false;
    }
}
