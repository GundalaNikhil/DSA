import java.util.*;

class Solution {
    public int maxGapAfterRemovals(int[] seats, int[] removeIndices) {
        int n = seats.length;
        boolean[] removed = new boolean[n];
        
        for (int idx : removeIndices) {
            removed[idx] = true;
        }
        
        int maxGap = 0;
        int lastPos = -1;
        boolean first = true;
        
        for (int i = 0; i < n; i++) {
            if (!removed[i]) {
                if (!first) {
                    maxGap = Math.max(maxGap, seats[i] - lastPos);
                }
                lastPos = seats[i];
                first = false;
            }
        }
        
        return maxGap;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] seats = new int[n];
        for (int i = 0; i < n; i++) seats[i] = sc.nextInt();
        
        int r = sc.nextInt();
        int[] removeIndices = new int[r];
        for (int i = 0; i < r; i++) removeIndices[i] = sc.nextInt();

        Solution solution = new Solution();
        int result = solution.maxGapAfterRemovals(seats, removeIndices);
        System.out.println(result);
        sc.close();
    }
}
