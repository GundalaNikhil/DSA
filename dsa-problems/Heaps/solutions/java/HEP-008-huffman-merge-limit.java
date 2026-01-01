import java.util.*;

class Solution {
    public long huffmanCost(int[] freq, int m) {
        PriorityQueue<Long> pq = new PriorityQueue<>();
        for (int f : freq) {
            pq.offer((long)f);
        }
        
        // Padding
        // Current size is n. Target is 1.
        // Reduction per step is m-1.
        // We need (size - 1) % (m - 1) == 0.
        while ((pq.size() - 1) % (m - 1) != 0) {
            pq.offer(0L);
        }
        
        long totalCost = 0;
        
        while (pq.size() > 1) {
            long sum = 0;
            for (int i = 0; i < m; i++) {
                sum += pq.poll();
            }
            totalCost += sum;
            pq.offer(sum);
        }
        
        return totalCost;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[] freq = new int[n];
            for (int i = 0; i < n; i++) {
                freq[i] = sc.nextInt();
            }
            
            Solution solution = new Solution();
            System.out.println(solution.huffmanCost(freq, m));
        }
        sc.close();
    }
}
