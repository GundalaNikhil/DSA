import java.util.*;

class Solution {
    public long minTotalDelay(int n, int[][] trips) {
        // Sort by (start + duration)
        Arrays.sort(trips, (a, b) -> Long.compare((long)a[0] + a[1], (long)b[0] + b[1]));
        
        long currentTime = 0;
        long totalDelay = 0;
        
        for (int[] trip : trips) {
            int s = trip[0];
            int d = trip[1];
            
            long delay = Math.max(0, currentTime - s);
            totalDelay += delay;
            currentTime += d;
        }
        
        return totalDelay;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int[][] trips = new int[n][2];
        for (int i = 0; i < n; i++) {
            trips[i][0] = sc.nextInt();
            trips[i][1] = sc.nextInt();
        }
        
        Solution solution = new Solution();
        System.out.println(solution.minTotalDelay(n, trips));
        sc.close();
    }
}
