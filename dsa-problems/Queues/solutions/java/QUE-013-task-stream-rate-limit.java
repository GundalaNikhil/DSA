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

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            long t = sc.nextLong();
            int k = sc.nextInt();
            long[] times = new long[n];
            for (int i = 0; i < n; i++) {
                times[i] = sc.nextLong();
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
