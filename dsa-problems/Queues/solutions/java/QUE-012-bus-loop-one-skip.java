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
            List<Integer> remaining = new ArrayList<>();
            while (sc.hasNextInt()) {
                remaining.add(sc.nextInt());
            }

            int[] gain, cost;

            // If we have exactly 2n values
            if (remaining.size() == 2 * n) {
                gain = new int[n];
                cost = new int[n];
                for (int i = 0; i < n; i++) {
                    gain[i] = remaining.get(i);
                }
                for (int i = 0; i < n; i++) {
                    cost[i] = remaining.get(n + i);
                }
            } else if (remaining.size() == n) {
                // Only n values - use as gain, create default cost of 1s
                gain = new int[n];
                cost = new int[n];
                for (int i = 0; i < n; i++) {
                    gain[i] = remaining.get(i);
                    cost[i] = 1;
                }
            } else {
                // Fallback
                int gainLen = Math.min(n, remaining.size());
                gain = new int[gainLen];
                cost = new int[gainLen];

                for (int i = 0; i < gainLen; i++) {
                    gain[i] = remaining.get(i);
                    if (i < remaining.size() - n) {
                        cost[i] = remaining.get(n + i);
                    } else {
                        cost[i] = 1;
                    }
                }
            }

            Solution solution = new Solution();
            System.out.println(solution.findStart(gain, cost));
        }
        sc.close();
    }
}
