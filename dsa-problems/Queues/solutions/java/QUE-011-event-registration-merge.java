import java.util.*;

class Solution {
    public int[] mergeQueues(int[] a, int[] b) {
        int n = a.length;
        int m = b.length;
        int[] result = new int[n + m];
        
        int i = 0, j = 0, k = 0;
        
        while (i < n && j < m) {
            if (a[i] <= b[j]) {
                result[k++] = a[i++];
            } else {
                result[k++] = b[j++];
            }
        }
        
        while (i < n) {
            result[k++] = a[i++];
        }
        
        while (j < m) {
            result[k++] = b[j++];
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

            int[] a, b;

            // If we have exactly 2n values, split them in half
            if (remaining.size() == 2 * n) {
                a = new int[n];
                b = new int[n];
                for (int i = 0; i < n; i++) {
                    a[i] = remaining.get(i);
                }
                for (int i = 0; i < n; i++) {
                    b[i] = remaining.get(n + i);
                }
            } else if (remaining.size() == n) {
                // Only n values - use as a, create empty b
                a = new int[n];
                b = new int[0];
                for (int i = 0; i < n; i++) {
                    a[i] = remaining.get(i);
                }
            } else if (remaining.size() > n) {
                // First value is m (size of b), rest split
                int m = remaining.get(0);
                if (remaining.size() >= n + m) {
                    a = new int[n];
                    b = new int[m];
                    for (int i = 0; i < n; i++) {
                        a[i] = remaining.get(i + 1);
                    }
                    for (int i = 0; i < m; i++) {
                        b[i] = remaining.get(n + 1 + i);
                    }
                } else {
                    int aLen = Math.min(n, remaining.size() - 1);
                    a = new int[aLen];
                    b = new int[remaining.size() - 1 - aLen];
                    for (int i = 0; i < aLen; i++) {
                        a[i] = remaining.get(i + 1);
                    }
                    for (int i = 0; i < b.length; i++) {
                        b[i] = remaining.get(aLen + 1 + i);
                    }
                }
            } else {
                // Fallback
                a = new int[remaining.size()];
                b = new int[0];
                for (int i = 0; i < a.length; i++) {
                    a[i] = remaining.get(i);
                }
            }

            Solution solution = new Solution();
            int[] result = solution.mergeQueues(a, b);
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
