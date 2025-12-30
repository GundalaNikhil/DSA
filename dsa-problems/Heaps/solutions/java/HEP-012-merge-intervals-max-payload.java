import java.util.*;

class Solution {
    public int[][] mergeIntervals(int[][] intervals) {
        if (intervals.length == 0) return new int[0][0];
        
        // Sort by start time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        
        List<int[]> merged = new ArrayList<>();
        int[] current = intervals[0];
        
        for (int i = 1; i < intervals.length; i++) {
            int[] next = intervals[i];
            
            // Check overlap
            if (next[0] <= current[1]) {
                // Merge
                current[1] = Math.max(current[1], next[1]);
                current[2] = Math.max(current[2], next[2]);
            } else {
                // No overlap, push current and start new
                merged.add(current);
                current = next;
            }
        }
        merged.add(current);
        
        return merged.toArray(new int[merged.size()][]);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[][] intervals = new int[n][3];
            for (int i = 0; i < n; i++) {
                intervals[i][0] = sc.nextInt();
                intervals[i][1] = sc.nextInt();
                intervals[i][2] = sc.nextInt();
            }
            
            Solution solution = new Solution();
            int[][] result = solution.mergeIntervals(intervals);
            System.out.println(result.length);
            for (int[] row : result) {
                System.out.println(row[0] + " " + row[1] + " " + row[2]);
            }
        }
        sc.close();
    }
}
