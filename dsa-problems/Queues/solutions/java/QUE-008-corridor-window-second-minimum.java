import java.util.*;

class Solution {
    public int[] secondMinimums(int[] values, int k) {
        int n = values.length;
        int[] result = new int[n - k + 1];
        TreeMap<Integer, Integer> map = new TreeMap<>();
        
        // Initialize first window
        for (int i = 0; i < k; i++) {
            map.put(values[i], map.getOrDefault(values[i], 0) + 1);
        }
        
        for (int i = 0; i <= n - k; i++) {
            // Query
            if (k == 1) {
                result[i] = map.firstKey();
            } else {
                int minVal = map.firstKey();
                if (map.get(minVal) > 1) {
                    result[i] = minVal;
                } else {
                    // Since k > 1, there must be a second key if first has count 1
                    result[i] = map.higherKey(minVal);
                }
            }
            
            // Slide window (remove outgoing, add incoming)
            if (i < n - k) {
                int out = values[i];
                int in = values[i + k];
                
                if (map.get(out) == 1) map.remove(out);
                else map.put(out, map.get(out) - 1);
                
                map.put(in, map.getOrDefault(in, 0) + 1);
            }
        }
        return result;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            List<Integer> remaining = new ArrayList<>();
            while (sc.hasNextInt()) {
                remaining.add(sc.nextInt());
            }

            int[] values;
            int k = 2;  // Default

            // If we have exactly n values
            if (remaining.size() == n) {
                values = new int[n];
                for (int i = 0; i < n; i++) {
                    values[i] = remaining.get(i);
                }
                k = 2;
            } else if (remaining.size() == n + 1) {
                // First is k, rest are values
                k = remaining.get(0);
                values = new int[n];
                for (int i = 0; i < n; i++) {
                    values[i] = remaining.get(i + 1);
                }
            } else {
                // Fallback
                k = !remaining.isEmpty() ? remaining.get(0) : 2;
                values = new int[Math.min(n, remaining.size() - 1)];
                for (int i = 0; i < values.length; i++) {
                    values[i] = remaining.get(i + 1);
                }
            }

            Solution solution = new Solution();
            int[] result = solution.secondMinimums(values, k);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.length; i++) {
                if (i > 0) sb.append(' ');
                sb.append(result[i]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
