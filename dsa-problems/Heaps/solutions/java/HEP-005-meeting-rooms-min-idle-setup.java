import java.util.*;

class Solution {
    public long minTotalSlack(int[][] meetings, int k, int s) {
        Arrays.sort(meetings, (a, b) -> Integer.compare(a[0], b[0]));
        
        // TreeMap to store <FreeTime, Count> for rooms already used
        TreeMap<Integer, Integer> rooms = new TreeMap<>();
        int unused = k;
        
        long totalSlack = 0;
        
        for (int[] meeting : meetings) {
            int start = meeting[0];
            int end = meeting[1];
            
            // Find largest free time <= start among used rooms
            Map.Entry<Integer, Integer> entry = rooms.floorEntry(start);

            if (entry != null) {
                int freeTime = entry.getKey();
                int count = entry.getValue();
                
                totalSlack += (long)(start - freeTime);
                
                if (count == 1) rooms.remove(freeTime);
                else rooms.put(freeTime, count - 1);
                
            } else {
                // Use a fresh room; first meeting in a room has 0 slack.
                // Valid schedule is guaranteed, so unused > 0 here.
                unused--;
            }

            int nextFree = end + s;
            rooms.put(nextFree, rooms.getOrDefault(nextFree, 0) + 1);
        }
        
        return totalSlack;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int s = sc.nextInt();
            int[][] meetings = new int[n][2];
            for (int i = 0; i < n; i++) {
                meetings[i][0] = sc.nextInt();
                meetings[i][1] = sc.nextInt();
            }
            
            Solution solution = new Solution();
            System.out.println(solution.minTotalSlack(meetings, k, s));
        }
        sc.close();
    }
}
