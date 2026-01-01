import java.util.*;

class Solution {
    int[] memo; // 0: unknown, 1: First, 2: Second

    public String divisorGame(int n) {
        memo = new int[n + 1];
        return canWin(n) ? "First" : "Second";
    }

    private boolean canWin(int n) {
        if (memo[n] != 0) return memo[n] == 1;

        boolean canReachLosing = false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                int d1 = i;
                if (!canWin(d1)) {
                    canReachLosing = true;
                    break;
                }
                int d2 = n / i;
                if (d2 < n && !canWin(d2)) {
                    canReachLosing = true;
                    break;
                }
            }
        }

        memo[n] = canReachLosing ? 1 : 2;
        return canReachLosing;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            Solution solution = new Solution();
            System.out.println(solution.divisorGame(n));
        }
        sc.close();
    }
}
