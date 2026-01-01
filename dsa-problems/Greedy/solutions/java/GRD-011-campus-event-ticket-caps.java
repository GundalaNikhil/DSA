import java.util.*;

class Solution {
    public long maxTickets(int n, int[][] requests) {
        // Sort by deadline
        Arrays.sort(requests, (a, b) -> Integer.compare(a[1], b[1]));
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        long totalTickets = 0;
        
        for (int[] req : requests) {
            int quantity = req[0];
            int deadline = req[1];
            
            pq.offer(quantity);
            totalTickets += quantity;
            
            // If we have more tasks than the current deadline allows,
            // remove the one with the smallest quantity.
            // Note: Since we sorted by deadline, the current deadline is the max time available
            // for ALL tasks currently in the heap.
            if (pq.size() > deadline) {
                totalTickets -= pq.poll();
            }
        }
        
        return totalTickets;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int[][] requests = new int[n][2];
        for (int i = 0; i < n; i++) {
            requests[i][0] = sc.nextInt();
            requests[i][1] = sc.nextInt();
        }
        
        Solution solution = new Solution();
        System.out.println(solution.maxTickets(n, requests));
        sc.close();
    }
}
