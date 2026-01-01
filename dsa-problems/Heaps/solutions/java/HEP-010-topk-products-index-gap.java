import java.util.*;

class Solution {
    static class Node implements Comparable<Node> {
        long val;
        int r, c;
        int dir; // 1 for TL (increase indices), -1 for BR (decrease indices)
        
        public Node(long val, int r, int c, int dir) {
            this.val = val;
            this.r = r;
            this.c = c;
            this.dir = dir;
        }
        
        @Override
        public int compareTo(Node other) {
            return Long.compare(other.val, this.val); // Max heap
        }
    }
    
    public List<Long> topKProducts(long[] A, long[] B, int k, int d) {
        int n = A.length;
        int m = B.length;
        PriorityQueue<Node> pq = new PriorityQueue<>();
        Set<String> visited = new HashSet<>();
        
        // Helper to add
        // dir=1: TL expansion. dir=-1: BR expansion.
        
        // TL Starts
        if (d < n) add(pq, visited, A, B, d, 0, 1, d);
        if (d < m && d > 0) add(pq, visited, A, B, 0, d, 1, d); // d>0 check to avoid duplicate (0,0) if d=0
        else if (d == 0) add(pq, visited, A, B, 0, 0, 1, d);
        
        // BR Starts
        // Region 1: j <= i - d. Max i=n-1. Max j = n-1-d. Constrained by m-1.
        if (d < n) {
            int startI = n - 1;
            int startJ = Math.min(m - 1, n - 1 - d);
            if (startJ >= 0) add(pq, visited, A, B, startI, startJ, -1, d);
        }
        
        // Region 2: j >= i + d. Max j=m-1. Max i = m-1-d. Constrained by n-1.
        if (d < m && d > 0) {
            int startJ = m - 1;
            int startI = Math.min(n - 1, m - 1 - d);
            if (startI >= 0) add(pq, visited, A, B, startI, startJ, -1, d);
        }
        
        List<Long> res = new ArrayList<>();
        while (k > 0 && !pq.isEmpty()) {
            Node node = pq.poll();
            res.add(node.val);
            k--;
            
            int r = node.r;
            int c = node.c;
            int dir = node.dir;
            
            if (dir == 1) {
                // Expand +1
                tryAdd(pq, visited, A, B, r + 1, c, 1, d);
                tryAdd(pq, visited, A, B, r, c + 1, 1, d);
            } else {
                // Expand -1
                tryAdd(pq, visited, A, B, r - 1, c, -1, d);
                tryAdd(pq, visited, A, B, r, c - 1, -1, d);
            }
        }
        
        return res;
    }
    
    private void add(PriorityQueue<Node> pq, Set<String> visited, long[] A, long[] B, int r, int c, int dir, int d) {
        String key = r + "," + c;
        if (!visited.contains(key)) {
            visited.add(key);
            pq.offer(new Node(A[r] * B[c], r, c, dir));
        }
    }
    
    private void tryAdd(PriorityQueue<Node> pq, Set<String> visited, long[] A, long[] B, int r, int c, int dir, int d) {
        if (r >= 0 && r < A.length && c >= 0 && c < B.length) {
            if (Math.abs(r - c) >= d) {
                add(pq, visited, A, B, r, c, dir, d);
            }
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int k = sc.nextInt();
            int d = sc.nextInt();
            long[] A = new long[n];
            long[] B = new long[m];
            for (int i = 0; i < n; i++) A[i] = sc.nextLong();
            for (int i = 0; i < m; i++) B[i] = sc.nextLong();
            
            Solution solution = new Solution();
            List<Long> result = solution.topKProducts(A, B, k, d);
            for (int i = 0; i < result.size(); i++) {
                System.out.print(result.get(i));
                if (i < result.size() - 1) System.out.print(" ");
            }
            System.out.println();
        }
        sc.close();
    }
}
