import java.util.*;

class Solution {
    public String subtractSquareGame(int n, int[] banned) {
        Set<Integer> bannedSet = new HashSet<>();
        for (int b : banned) bannedSet.add(b);
        
        boolean[] dp = new boolean[n + 1];
        // dp[0] is false (Losing)
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j * j <= i; j++) {
                int s = j * j;
                if (!bannedSet.contains(s)) {
                    if (!dp[i - s]) {
                        dp[i] = true;
                        break;
                    }
                }
            }
        }
        
        return dp[n] ? "First" : "Second";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int[] banned = new int[k];
            for (int i = 0; i < k; i++) {
                banned[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.subtractSquareGame(n, banned));
        }
        sc.close();
    }
}
