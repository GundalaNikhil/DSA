import java.util.*;

class Solution {
    Map<String, String> memo = new HashMap<>();
    Set<String> visiting = new HashSet<>();

    public String circularNim(int n, int[] piles) {
        return solve(n, piles, 0);
    }

    private String solve(int n, int[] piles, int depth) {
        if (depth > 50) return "Draw";
        String key = Arrays.toString(piles);
        if (memo.containsKey(key)) return memo.get(key);
        if (visiting.contains(key)) return "Draw";

        visiting.add(key);
        boolean canReachLoss = false;
        boolean canReachDraw = false;
        boolean hasMoves = false;

        for (int i = 0; i < n; i++) {
            if (piles[i] > 0) {
                for (int k = 1; k <= piles[i]; k++) {
                    hasMoves = true;
                    piles[i] -= k;
                    piles[(i - 1 + n) % n]++;
                    piles[(i + 1) % n]++;
                    
                    String res = solve(n, piles, depth + 1);
                    
                    piles[(i + 1) % n]--;
                    piles[(i - 1 + n) % n]--;
                    piles[i] += k;

                    if (res.equals("Second")) {
                        canReachLoss = true;
                        break;
                    }
                    if (res.equals("Draw")) {
                        canReachDraw = true;
                    }
                }
                if (canReachLoss) break;
            }
        }

        visiting.remove(key);
        String result;
        if (canReachLoss) result = "First";
        else if (!hasMoves) result = "Second"; // No moves -> Loss
        else if (canReachDraw) result = "Draw";
        else result = "Second"; // All moves lead to First (Win for opponent)

        memo.put(key, result);
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] piles = new int[n];
            for (int i = 0; i < n; i++) {
                piles[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.circularNim(n, piles));
        }
        sc.close();
    }
}
