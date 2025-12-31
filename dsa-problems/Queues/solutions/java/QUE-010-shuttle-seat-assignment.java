import java.util.*;

class Solution {
    public int minSeats(int[] arrivals, int[] departures) {
        int n = arrivals.length;
        int[][] intervals = new int[n][2];
        for (int i = 0; i < n; i++) {
            intervals[i][0] = arrivals[i];
            intervals[i][1] = departures[i];
        }
        
        // Sort by arrival time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        
        // Min-heap stores departure times
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int maxSeats = 0;
        
        for (int[] interval : intervals) {
            int start = interval[0];
            int end = interval[1];
            
            // Free up seats that have ended by 'start'
            while (!pq.isEmpty() && pq.peek() <= start) {
                pq.poll();
            }
            
            pq.offer(end);
            maxSeats = Math.max(maxSeats, pq.size());
        }
        
        return maxSeats;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] arrivals = new int[n];
            int[] departures = new int[n];
            for (int i = 0; i < n; i++) {
                arrivals[i] = sc.nextInt();
            }
            for (int i = 0; i < n; i++) {
                departures[i] = sc.nextInt();
            }
    
            Solution solution = new Solution();
            int result = solution.minSeats(arrivals, departures);
            System.out.println(result);
        }
        sc.close();
    }
}
