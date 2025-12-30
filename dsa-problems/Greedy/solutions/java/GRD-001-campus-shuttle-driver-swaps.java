import java.util.*;

class Solution {
    public int minDriverSwaps(int[][] trips, int[] driverA, int[] driverB) {
        int n = trips.length;
        // Costs to reach current trip ending with Driver A or Driver B
        // Use a large number for infinity, but safe from overflow when adding 1
        int INF = Integer.MAX_VALUE / 2;
        int costA = INF;
        int costB = INF;

        // Base case: Trip 0
        if (canCover(trips[0], driverA)) costA = 0;
        if (canCover(trips[0], driverB)) costB = 0;

        for (int i = 1; i < n; i++) {
            int nextCostA = INF;
            int nextCostB = INF;

            // If Driver A can take current trip
            if (canCover(trips[i], driverA)) {
                // Option 1: Continued from A (0 cost)
                // Option 2: Switched from B (1 cost)
                nextCostA = Math.min(costA, costB + 1);
            }

            // If Driver B can take current trip
            if (canCover(trips[i], driverB)) {
                // Option 1: Continued from B (0 cost)
                // Option 2: Switched from A (1 cost)
                nextCostB = Math.min(costB, costA + 1);
            }

            costA = nextCostA;
            costB = nextCostB;
        }

        int result = Math.min(costA, costB);
        return result >= INF ? -1 : result;
    }

    private boolean canCover(int[] trip, int[] driver) {
        return driver[0] <= trip[0] && trip[1] <= driver[1];
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        
        int[][] trips = new int[n][2];
        for (int i = 0; i < n; i++) {
            trips[i][0] = sc.nextInt();
            trips[i][1] = sc.nextInt();
        }
        
        int[] driverA = new int[2];
        driverA[0] = sc.nextInt();
        driverA[1] = sc.nextInt();
        
        int[] driverB = new int[2];
        driverB[0] = sc.nextInt();
        driverB[1] = sc.nextInt();
        
        Solution solution = new Solution();
        System.out.println(solution.minDriverSwaps(trips, driverA, driverB));
        sc.close();
    }
}
