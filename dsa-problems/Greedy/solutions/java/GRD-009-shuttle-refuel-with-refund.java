import java.util.*;

class Solution {
    public int findStart(int n, int[] gain, int[] cost) {
        long totalGain = 0;
        long totalCost = 0;
        int maxCostIndex = -1;
        int maxCostVal = -1;
        
        for (int i = 0; i < n; i++) {
            totalGain += gain[i];
            totalCost += cost[i];
            if (cost[i] > maxCostVal) {
                maxCostVal = cost[i];
                maxCostIndex = i;
            }
        }
        
        // Check if possible with coupon
        if (totalGain < totalCost - maxCostVal) {
            return -1;
        }
        
        // Standard Gas Station Greedy Logic with modified cost
        // We treat cost[maxCostIndex] as 0
        
        long currentTank = 0;
        int start = 0;
        
        for (int i = 0; i < n; i++) {
            long currentCost = (i == maxCostIndex) ? 0 : cost[i];
            currentTank += gain[i] - currentCost;
            
            if (currentTank < 0) {
                // Cannot reach i+1 from current start
                // Reset start to i+1
                start = i + 1;
                currentTank = 0;
            }
        }
        
        return start;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int[] gain = new int[n];
        for (int i = 0; i < n; i++) gain[i] = sc.nextInt();
        
        int[] cost = new int[n];
        for (int i = 0; i < n; i++) cost[i] = sc.nextInt();
        
        Solution solution = new Solution();
        System.out.println(solution.findStart(n, gain, cost));
        sc.close();
    }
}
