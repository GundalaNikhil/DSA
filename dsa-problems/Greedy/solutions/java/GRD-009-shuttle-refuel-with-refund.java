import java.util.*;

class Solution {
    private boolean checkStart(int n, int[] gain, int[] cost, int startIdx) {
        long fuel = 0;
        long maxC = 0;
        boolean used = false;

        for (int i = 0; i < n; i++) {
            int idx = (startIdx + i) % n;
            fuel += gain[idx];
            maxC = Math.max(maxC, cost[idx]);
            fuel -= cost[idx];

            if (fuel < 0) {
                if (!used) {
                    fuel += maxC;
                    used = true;
                    if (fuel < 0) return false;
                } else {
                    return false;
                }
            }
        }

        return true;
    }

    public int findStart(int n, int[] gain, int[] cost) {
        long totalGain = 0;
        long totalCost = 0;
        long maxCost = 0;

        for (int i = 0; i < n; i++) {
            totalGain += gain[i];
            totalCost += cost[i];
            maxCost = Math.max(maxCost, cost[i]);
        }

        // If even with refund we can't make it, return -1
        if (totalGain < totalCost - maxCost) {
            return -1;
        }

        // Total gain + max cost must be >= total cost
        if (totalGain + maxCost < totalCost) {
            return -1;
        }

        // Check classic gas station start first
        long curr = 0;
        long minSum = 0;
        int startCand = 0;

        for (int i = 0; i < n; i++) {
            curr += gain[i] - cost[i];
            if (curr < minSum) {
                minSum = curr;
                startCand = (i + 1) % n;
            }
        }

        if (checkStart(n, gain, cost, startCand)) {
            return startCand;
        }

        // If not, try all
        for (int i = 0; i < n; i++) {
            if (checkStart(n, gain, cost, i)) {
                return i;
            }
        }

        return -1;
    }
}

class Main {
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
