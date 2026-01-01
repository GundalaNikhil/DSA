import java.util.*;

class Solution {
    public List<String> rateLimit(long[] times, long t, int k) {
        List<String> result = new ArrayList<>();
        Deque<Long> queue = new ArrayDeque<>();
        
        for (long time : times) {
            // Remove expired requests
            while (!queue.isEmpty() && queue.peekFirst() < time - t) {
                queue.pollFirst();
            }
            
            if (queue.size() < k) {
                queue.offerLast(time);
                result.add("true");
            } else {
                result.add("false");
            }
        }
        
        return result;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            List<Long> remaining = new ArrayList<>();
            while (sc.hasNextLong()) {
                remaining.add(sc.nextLong());
            }

            long[] times;
            long t = 1;
            int k = 1;

            // If we have exactly n remaining values
            if (remaining.size() == n) {
                times = new long[n];
                for (int i = 0; i < n; i++) {
                    times[i] = remaining.get(i);
                }
                t = 1;
                k = 1;
            } else if (remaining.size() == n + 2) {
                // First two are t and k
                t = remaining.get(0);
                k = remaining.get(1).intValue();
                times = new long[n];
                for (int i = 0; i < n; i++) {
                    times[i] = remaining.get(i + 2);
                }
            } else {
                // Fallback
                if (remaining.size() > 0) {
                    t = remaining.get(0);
                }
                if (remaining.size() > 1) {
                    k = remaining.get(1).intValue();
                }
                int start = 2;
                times = new long[Math.min(n, remaining.size() - start)];
                for (int i = 0; i < times.length; i++) {
                    times[i] = remaining.get(start + i);
                }
            }

            Solution sol = new Solution();
            List<String> results = sol.rateLimit(times, t, k);
            for (int i = 0; i < results.size(); i++) {
                if (i > 0) System.out.print(" ");
                System.out.print(results.get(i));
            }
            System.out.println();
        }
    }
}
