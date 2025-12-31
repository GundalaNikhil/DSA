import java.util.*;

class Solution {
    public double hitProbability(int a, int b, int T) {
        // Offset to handle negative coordinates
        int offset = T;
        int size = 2 * T + 1;
        double[][] dp = new double[size][size];
        
        // Start at (0,0) -> (offset, offset)
        dp[offset][offset] = 1.0;
        
        int targetX = a + offset;
        int targetY = b + offset;
        
        // If start is target
        if (a == 0 && b == 0) return 1.0;
        
        // Directions: N, S, E, W
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        
        for (int t = 1; t <= T; t++) {
            double[][] nextDp = new double[size][size];
            
            // Optimization: Only iterate reachable area
            // At step t-1, max reach is t-1
            int minVal = offset - (t - 1);
            int maxVal = offset + (t - 1);
            
            // Carry over probability already at target (absorbing)
            nextDp[targetX][targetY] = dp[targetX][targetY];
            
            for (int x = minVal; x <= maxVal; x++) {
                for (int y = minVal; y <= maxVal; y++) {
                    if (dp[x][y] == 0) continue;
                    
                    // If we are already at target, we stayed there (handled above)
                    // But                     // We must NOT distribute from target.
                    if (x == targetX && y == targetY) continue;
                    
                    double prob = dp[x][y] * 0.25;
                    for (int i = 0; i < 4; i++) {
                        int nx = x + dx[i];
                        int ny = y + dy[i];
                        nextDp[nx][ny] += prob;
                    }
                }
            }
            dp = nextDp;
        }
        
        return dp[targetX][targetY];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int T = sc.nextInt();

            Solution solution = new Solution();
            System.out.println(solution.hitProbability(a, b, T));
        }
        sc.close();
    }
}
