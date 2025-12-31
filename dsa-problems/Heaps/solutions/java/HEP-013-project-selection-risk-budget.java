import java.util.*;

class Solution {
    static class Project {
        long c, p, r;
        public Project(long c, long p, long r) {
            this.c = c;
            this.p = p;
            this.r = r;
        }
    }
    
    public long maximizeCapital(int k, long C, long R, long[] cost, long[] profit, long[] risk) {
        int n = cost.length;
        Project[] projects = new Project[n];
        for (int i = 0; i < n; i++) {
            projects[i] = new Project(cost[i], profit[i], risk[i]);
        }
        
        // Sort by cost
        Arrays.sort(projects, (a, b) -> Long.compare(a.c, b.c));
        
        // Max-Heap by profit
        PriorityQueue<Project> pq = new PriorityQueue<>((a, b) -> Long.compare(b.p, a.p));
        
        int ptr = 0;
        long currentC = C;
        long remainingR = R;
        
        for (int i = 0; i < k; i++) {
            // Add affordable projects
            while (ptr < n && projects[ptr].c <= currentC) {
                pq.offer(projects[ptr]);
                ptr++;
            }
            
            // Pick best valid
            boolean picked = false;
            while (!pq.isEmpty()) {
                Project p = pq.peek();
                if (p.r <= remainingR) {
                    // Valid
                    pq.poll();
                    currentC += p.p;
                    remainingR -= p.r;
                    picked = true;
                    break;
                } else {
                    // Too risky, will never be valid
                    pq.poll();
                }
            }
            
            if (!picked) break;
        }
        
        return currentC;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            long C = sc.nextLong();
            long R = sc.nextLong();
            long[] cost = new long[n];
            long[] profit = new long[n];
            long[] risk = new long[n];
            for (int i = 0; i < n; i++) {
                cost[i] = sc.nextLong();
                profit[i] = sc.nextLong();
                risk[i] = sc.nextLong();
            }
            
            Solution solution = new Solution();
            System.out.println(solution.maximizeCapital(k, C, R, cost, profit, risk));
        }
        sc.close();
    }
}
