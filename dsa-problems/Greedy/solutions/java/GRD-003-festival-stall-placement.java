import java.util.*;

class Solution {
    public int maxStalls(int[][] stalls, int d) {
        // Sort by end time
        Arrays.sort(stalls, (a, b) -> Integer.compare(a[1], b[1]));
        
        int count = 0;
        // Use long for lastEnd to handle initial case safely, 
        // though -infinity logic works with integer min value if careful.
        // Since coordinates are >= 0, initializing to a sufficiently small negative number works.
        long lastEnd = Long.MIN_VALUE; 
        
        for (int[] stall : stalls) {
            int start = stall[0];
            int end = stall[1];
            
            // Check if start is far enough from lastEnd
            // Use long arithmetic to avoid overflow if lastEnd is very small
            if (lastEnd == Long.MIN_VALUE || (long)start - lastEnd >= d) {
                count++;
                lastEnd = end;
            }
        }
        
        return count;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int d = sc.nextInt();

        int[][] stalls = new int[n][2];
        for (int i = 0; i < n; i++) {
            stalls[i][0] = sc.nextInt();
            stalls[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxStalls(stalls, d));
        sc.close();
    }
}
