import java.util.*;

class Solution {
    public int minBatterySwaps(int n, long T, long[] capacities) {
        // Calculate total sum first to check feasibility
        long totalCapacity = 0;
        for (long c : capacities) {
            totalCapacity += c;
        }
        
        if (totalCapacity < T) {
            return -1;
        }
        
        // Sort array. Arrays.sort sorts primitives in ascending order.
        Arrays.sort(capacities);
        
        long currentSum = 0;
        int count = 0;
        
        // Iterate backwards for descending order
        for (int i = n - 1; i >= 0; i--) {
            currentSum += capacities[i];
            count++;
            if (currentSum >= T) {
                return count - 1;
            }
        }
        
        return -1; // Should not reach here due to initial check
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        long T = sc.nextLong();

        long[] capacities = new long[n];
        for (int i = 0; i < n; i++) {
            capacities[i] = sc.nextLong();
        }

        Solution solution = new Solution();
        System.out.println(solution.minBatterySwaps(n, T, capacities));
        sc.close();
    }
}
