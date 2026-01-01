import java.util.*;

class Solution {
    public int[] distributeKits(int k, int m, int[] quantities) {
        // PriorityQueue is min-heap by default, use reverseOrder for max-heap
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        long totalKits = 0;
        int initialZeros = 0;
        
        for (int q : quantities) {
            if (q > 0) {
                pq.offer(q);
                totalKits += q;
            } else {
                initialZeros++;
            }
        }
        
        int fulfilled = (int) Math.min((long) m, totalKits);
        int toDistribute = fulfilled;
        
        while (toDistribute > 0 && !pq.isEmpty()) {
            int maxQ = pq.poll();
            maxQ--;
            toDistribute--;
            
            if (maxQ > 0) {
                pq.offer(maxQ);
            }
        }
        
        // Zeroed types = Total types - Types remaining in heap
        // Or: Initial zeros + (Initial non-zeros - Final non-zeros)
        int remainingTypes = pq.size();
        int zeroedTypes = k - remainingTypes;
        
        return new int[]{fulfilled, zeroedTypes};
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int k = sc.nextInt();
        int m = sc.nextInt();
        
        int[] quantities = new int[k];
        for (int i = 0; i < k; i++) {
            quantities[i] = sc.nextInt();
        }
        
        Solution solution = new Solution();
        int[] result = solution.distributeKits(k, m, quantities);
        System.out.println(result[0] + " " + result[1]);
        sc.close();
    }
}
