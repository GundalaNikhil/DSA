import java.util.*;

class Solution {
    public int[] smallestRange(List<int[]> lists) {
        List<int[]> events = new ArrayList<>();
        int k = lists.size();
        int[] required = new int[k];
        
        for (int i = 0; i < k; i++) {
            int[] list = lists.get(i);
            if (list.length == 0) return new int[]{}; // Impossible
            required[i] = (list.length == 1) ? 1 : 2;
            for (int val : list) {
                events.add(new int[]{val, i});
            }
        }
        
        events.sort((a, b) -> Integer.compare(a[0], b[0]));
        
        int[] counts = new int[k];
        int satisfied = 0;
        int left = 0;
        int minLen = Integer.MAX_VALUE;
        int[] res = new int[]{};
        
        for (int right = 0; right < events.size(); right++) {
            int listId = events.get(right)[1];
            counts[listId]++;
            
            if (counts[listId] == required[listId]) {
                satisfied++;
            }
            
            while (satisfied == k) {
                int startVal = events.get(left)[0];
                int endVal = events.get(right)[0];
                int len = endVal - startVal;
                
                if (len < minLen) {
                    minLen = len;
                    res = new int[]{startVal, endVal};
                }
                
                // Shrink
                int leftListId = events.get(left)[1];
                if (counts[leftListId] == required[leftListId]) {
                    satisfied--;
                }
                counts[leftListId]--;
                left++;
            }
        }
        
        return res;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) {
            sc.close();
            return;
        }
        int k = sc.nextInt();
        List<int[]> lists = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            int m = sc.nextInt();
            int[] list = new int[m];
            for (int j = 0; j < m; j++) {
                list[j] = sc.nextInt();
            }
            lists.add(list);
        }
        Solution solution = new Solution();
        int[] result = solution.smallestRange(lists);
        if (result.length == 0) {
            System.out.println("NONE");
        } else {
            System.out.println(result[0] + " " + result[1]);
        }
        sc.close();
    }
}
