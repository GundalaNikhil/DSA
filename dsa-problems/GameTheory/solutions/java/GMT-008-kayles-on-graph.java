import java.util.*;

class Solution {
    int[] adjMask;
    int[] memo; // -1: unknown, 0: Losing, 1: Winning

    public String kaylesOnGraph(int n, int[][] edges) {
        adjMask = new int[n];
        for (int[] e : edges) {
            adjMask[e[0]] |= (1 << e[1]);
            adjMask[e[1]] |= (1 << e[0]);
        }

        memo = new int[1 << n];
        Arrays.fill(memo, -1);

        return canWin((1 << n) - 1, n) ? "First" : "Second";
    }

    private boolean canWin(int mask, int n) {
        if (mask == 0) return false;
        if (memo[mask] != -1) return memo[mask] == 1;

        boolean canReachLosing = false;
        for (int u = 0; u < n; u++) {
            if ((mask & (1 << u)) != 0) {
                int removeMask = (1 << u) | adjMask[u];
                int nextMask = mask & ~removeMask;
                if (!canWin(nextMask, n)) {
                    canReachLosing = true;
                    break;
                }
            }
        }

        memo[mask] = canReachLosing ? 1 : 0;
        return canReachLosing;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[][] edges = new int[m][2];
            for (int i = 0; i < m; i++) {
                edges[i][0] = sc.nextInt();
                edges[i][1] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.kaylesOnGraph(n, edges));
        }
        sc.close();
    }
}
