import java.util.*;

class Solution {
    public int highestOccupiedRow(int r, int[] capacities, int[][] refunds) {
        long totalCapacity = 0;
        for (int cap : capacities) {
            totalCapacity += cap;
        }
        
        long totalPeople = totalCapacity - refunds.length;
        
        if (totalPeople <= 0) return 0; // Should not happen based on constraints (at least 1 person? or empty?)
        // If empty, return 0? Or 1? Problem says "highest occupied". If 0 people, 0.
        
        for (int i = 0; i < r; i++) {
            totalPeople -= capacities[i];
            if (totalPeople <= 0) {
                return i + 1;
            }
        }
        
        return r;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int r = sc.nextInt();
        int n = sc.nextInt();
        
        int[] capacities = new int[r];
        for (int i = 0; i < r; i++) {
            capacities[i] = sc.nextInt();
        }
        
        int[][] refunds = new int[n][2];
        for (int i = 0; i < n; i++) {
            refunds[i][0] = sc.nextInt();
            refunds[i][1] = sc.nextInt();
        }
        
        Solution solution = new Solution();
        System.out.println(solution.highestOccupiedRow(r, capacities, refunds));
        sc.close();
    }
}
