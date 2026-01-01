import java.util.*;

class Solution {
    static class Part implements Comparable<Part> {
        long w;
        int q;

        public Part(long w, int q) {
            this.w = w;
            this.q = q;
        }

        @Override
        public int compareTo(Part other) {
            // Max-heap based on quality, then min-heap on weight
            if (this.q != other.q) {
                return Integer.compare(other.q, this.q); // Reverse for max-heap
            }
            return Long.compare(this.w, other.w); // Normal for min-heap on weight
        }
    }

    public long maxBundleWeight(int n, int T, int[] weights, int[] qualities) {
        PriorityQueue<Part> pq = new PriorityQueue<>();
        
        for (int i = 0; i < n; i++) {
            pq.offer(new Part(weights[i], qualities[i]));
        }
        
        while (pq.size() > 1) {
            Part p1 = pq.poll();
            Part p2 = pq.poll();
            
            int newQ = Math.min(p1.q, p2.q) - 1;
            
            if (newQ < T) {
                return -1;
            }
            
            long minW = Math.min(p1.w, p2.w);
            long loss = (long) Math.floor(0.1 * minW);
            long newW = p1.w + p2.w - loss;
            
            pq.offer(new Part(newW, newQ));
        }
        
        return pq.isEmpty() ? -1 : pq.poll().w;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int T = sc.nextInt();

        int[] weights = new int[n];
        for (int i = 0; i < n; i++) {
            weights[i] = sc.nextInt();
        }

        int[] qualities = new int[n];
        for (int i = 0; i < n; i++) {
            qualities[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxBundleWeight(n, T, weights, qualities));
        sc.close();
    }
}
