import java.util.*;

class Solution {
    public int minProctors(int n, int r, int[][] exams) {
        // Events: time, type (+1 for start, -1 for end)
        // To handle inclusive intervals [start, end] correctly where end overlaps with next start:
        // We want to count overlap at time T.
        // If one starts at T and another ends at T, they overlap.
        // So we should process Start (+1) before End (-1).
        // So we process Start before End.
        // BUT, usually "End" event happens *after* the duration.
        // If the input is [start, end] inclusive, the exam occupies time `end`.
        // So it effectively finishes *after* `end`.
        // Let's treat the events as: Start at `start`, End at `end + epsilon`.
        // Or simply: Sort by time. If times equal, process Start first.
        
        int[][] events = new int[2 * n][2];
        for (int i = 0; i < n; i++) {
            events[2 * i][0] = exams[i][0];
            events[2 * i][1] = 1; // +1 for start
            
            events[2 * i + 1][0] = exams[i][1];
            events[2 * i + 1][1] = -1; // -1 for end
        }
        
        Arrays.sort(events, (a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            // If times are equal, process Start (+1) before End (-1) to maximize overlap
            // Since +1 > -1, sorting descending by type works? 
            // We want +1 before -1.
            return Integer.compare(b[1], a[1]);
        });
        
        int maxOverlap = 0;
        int currentOverlap = 0;
        
        for (int[] event : events) {
            currentOverlap += event[1];
            maxOverlap = Math.max(maxOverlap, currentOverlap);
        }
        
        // Ceiling division: (a + b - 1) / b
        return (maxOverlap + r - 1) / r;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int r = sc.nextInt();
        
        int[][] exams = new int[n][2];
        for (int i = 0; i < n; i++) {
            exams[i][0] = sc.nextInt();
            exams[i][1] = sc.nextInt();
        }
        
        Solution solution = new Solution();
        System.out.println(solution.minProctors(n, r, exams));
        sc.close();
    }
}
