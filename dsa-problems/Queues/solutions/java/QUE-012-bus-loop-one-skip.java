import java.util.*;

class Solution {
    public int findStart(int[] gain, int[] cost) {
        int n = gain.length;
        
        // 1. Find index of minimum gain
        int minGainIndex = -1;
        int minGain = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (gain[i] < minGain) {
                minGain = gain[i];
                minGainIndex = i;
            }
        }
        
        // 2. Temporarily remove that gain (simulate skip)
        int originalGain = gain[minGainIndex];
        gain[minGainIndex] = 0;
        
        // 3. Run standard Gas Station algorithm
        long totalTank = 0;
        long currTank = 0;
        int start = 0;
        
        for (int i = 0; i < n; i++) {
            long net = (long)gain[i] - (long)cost[i];
            totalTank += net;
            currTank += net;
            if (currTank < 0) {
                start = i + 1;
                currTank = 0;
            }
        }
        
        // Restore gain (good practice)
        gain[minGainIndex] = originalGain;
        
        return totalTank >= 0 ? start % n : -1;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] gain = new int[n];
            int[] cost = new int[n];
            for (int i = 0; i < n; i++) {
                gain[i] = sc.nextInt();
            }
            for (int i = 0; i < n; i++) {
                cost[i] = sc.nextInt();
            }
    
            Solution solution = new Solution();
            System.out.println(solution.findStart(gain, cost));
        }
        sc.close();
    }
}
