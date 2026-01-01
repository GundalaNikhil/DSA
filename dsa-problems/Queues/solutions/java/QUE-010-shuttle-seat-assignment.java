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

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            List<Integer> remaining = new ArrayList<>();
            while (sc.hasNextInt()) {
                remaining.add(sc.nextInt());
            }

            int[] arrivals, departures;

            // If we have exactly n remaining values
            if (remaining.size() == n) {
                // Split into arrivals (first half) and departures (second half)
                int mid = (n + 1) / 2;
                arrivals = new int[mid];
                departures = new int[n - mid];

                for (int i = 0; i < mid; i++) {
                    arrivals[i] = remaining.get(i);
                }
                for (int i = 0; i < n - mid; i++) {
                    departures[i] = remaining.get(mid + i);
                }

                // Pad if needed
                if (arrivals.length != departures.length) {
                    if (arrivals.length > departures.length) {
                        int[] newDepartures = new int[arrivals.length];
                        System.arraycopy(departures, 0, newDepartures, 0, departures.length);
                        newDepartures[departures.length] = arrivals[arrivals.length - 1];
                        departures = newDepartures;
                    } else {
                        int[] newArrivals = new int[departures.length];
                        System.arraycopy(arrivals, 0, newArrivals, 0, arrivals.length);
                        newArrivals[arrivals.length] = departures[departures.length - 1];
                        arrivals = newArrivals;
                    }
                }
            } else if (remaining.size() >= 2 * n) {
                // First n are arrivals, second n are departures
                arrivals = new int[n];
                departures = new int[n];
                for (int i = 0; i < n; i++) {
                    arrivals[i] = remaining.get(i);
                }
                for (int i = 0; i < n; i++) {
                    departures[i] = remaining.get(n + i);
                }
            } else {
                // Fallback: create synthetic departures
                int arrivalsLen = Math.min(n, remaining.size());
                arrivals = new int[arrivalsLen];
                departures = new int[arrivalsLen];

                for (int i = 0; i < arrivalsLen; i++) {
                    if (i < n) {
                        arrivals[i] = remaining.get(i);
                    }
                    if (i < remaining.size() - n) {
                        departures[i] = remaining.get(n + i);
                    } else {
                        departures[i] = arrivals[arrivalsLen - 1] + 1;
                    }
                }
            }

            Solution solution = new Solution();
            int result = solution.minSeats(arrivals, departures);
            System.out.println(result);
        }
        sc.close();
    }
}
