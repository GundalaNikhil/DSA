import java.util.*;

class Solution {
    private long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public int maxPointsOnSegment(int[][] points, int L) {
        int n = points.length;
        if (n <= 1) return n;
        
        // Count frequencies of each point
        Map<String, Integer> pointCounts = new HashMap<>();
        for (int[] p : points) {
            String key = p[0] + "," + p[1];
            pointCounts.put(key, pointCounts.getOrDefault(key, 0) + 1);
        }
        
        List<int[]> uniquePoints = new ArrayList<>();
        List<Integer> counts = new ArrayList<>();
        for (String key : pointCounts.keySet()) {
            String[] parts = key.split(",");
            uniquePoints.add(new int[]{Integer.parseInt(parts[0]), Integer.parseInt(parts[1])});
            counts.add(pointCounts.get(key));
        }
        
        int maxPts = 0;
        for (int c : counts) maxPts = Math.max(maxPts, c);
        
        int m = uniquePoints.size();
        for (int i = 0; i < m; i++) {
            Map<String, Integer> slopeMap = new HashMap<>();
            int[] p1 = uniquePoints.get(i);
            
            for (int j = 0; j < m; j++) {
                if (i == j) continue;
                int[] p2 = uniquePoints.get(j);
                
                long dx = (long)p2[0] - p1[0];
                long dy = (long)p2[1] - p1[1];
                double dist = Math.sqrt((double)dx * dx + (double)dy * dy);
                
                if (dist > L + 1e-9) continue;
                
                long g = gcd(Math.abs(dx), Math.abs(dy));
                String slope = (dx / g) + "," + (dy / g);
                
                slopeMap.put(slope, slopeMap.getOrDefault(slope, 0) + counts.get(j));
            }
            
            for (int count : slopeMap.values()) {
                maxPts = Math.max(maxPts, counts.get(i) + count);
            }
        }
        
        return maxPts;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int L = sc.nextInt();
            int[][] points = new int[n][2];
            for (int i = 0; i < n; i++) {
                points[i][0] = sc.nextInt();
                points[i][1] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.maxPointsOnSegment(points, L));
        }
        sc.close();
    }
}
