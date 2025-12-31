import java.util.*;

class Solution {
    static class Task {
        String id;
        int count;
        long priority;
        int x; // assigned count
        
        public Task(String id, int count, long priority) {
            this.id = id;
            this.count = count;
            this.priority = priority;
            this.x = count;
        }
    }
    
    public long maxPriority(int T, int cooldown, String[] ids, int[] count, long[] priority) {
        int m = ids.length;
        List<Task> tasks = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            tasks.add(new Task(ids[i], count[i], priority[i]));
        }
        
        // 1. Clamp
        int limit = (T + cooldown) / (cooldown + 1);
        for (Task t : tasks) {
            t.x = Math.min(t.count, limit);
        }
        
        // 2. Satisfy Schedule Constraint
        while (true) {
            int maxX = 0;
            for (Task t : tasks) maxX = Math.max(maxX, t.x);
            
            if (maxX == 0) break;
            
            List<Task> atMax = new ArrayList<>();
            for (Task t : tasks) {
                if (t.x == maxX) atMax.add(t);
            }
            
            long required = (long)(maxX - 1) * (cooldown + 1) + atMax.size();
            
            if (required <= T) break;
            
            // Too many at maxX. Allowed?
            long allowed = T - (long)(maxX - 1) * (cooldown + 1);
            // allowed can be negative if T is very small, but clamp handles basic bounds.
            // If allowed < 0, it means even 1 task at maxX is too much?
            // (maxX-1)(k+1) + 1 > T.
            // This implies maxX is too high.
            // But we clamped maxX <= (T+k)/(k+1).
            // So (maxX-1)(k+1) + 1 <= T is guaranteed for a SINGLE task.
            // So allowed >= 1.
            
            // Sort atMax by Priority Descending (Keep high priority)
            atMax.sort((a, b) -> Long.compare(b.priority, a.priority));
            
            // Keep top 'allowed', demote others
            for (int i = (int)allowed; i < atMax.size(); i++) {
                atMax.get(i).x--;
            }
        }
        
        // 3. Satisfy Sum Constraint
        long sumX = 0;
        for (Task t : tasks) sumX += t.x;
        
        if (sumX > T) {
            long toRemove = sumX - T;
            // Sort by Priority Ascending (Remove low priority)
            tasks.sort((a, b) -> Long.compare(a.priority, b.priority));
            
            for (Task t : tasks) {
                if (toRemove <= 0) break;
                int remove = (int)Math.min(t.x, toRemove);
                t.x -= remove;
                toRemove -= remove;
            }
        }
        
        long totalScore = 0;
        for (Task t : tasks) totalScore += t.x * t.priority;
        
        return totalScore;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            int cooldown = sc.nextInt();
            int T = sc.nextInt();
            String[] ids = new String[m];
            int[] count = new int[m];
            long[] priority = new long[m];
            for (int i = 0; i < m; i++) {
                ids[i] = sc.next();
                count[i] = sc.nextInt();
                priority[i] = sc.nextLong();
            }
            
            Solution solution = new Solution();
            System.out.println(solution.maxPriority(T, cooldown, ids, count, priority));
        }
        sc.close();
    }
}
