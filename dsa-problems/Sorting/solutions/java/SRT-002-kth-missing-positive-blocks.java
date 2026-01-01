import java.util.*;

class Solution {
    public long[] solve(int[] arr, long[][] queries) {
        int n = arr.length;
        long[] results = new long[queries.length];
        
        for (int i = 0; i < queries.length; i++) {
            long k = queries[i][0];
            long b = queries[i][1];
            long m = k * b;
            
            // Binary search for largest idx such that arr[idx] - (idx + 1) < m
            int low = 0, high = n - 1;
            int idx = -1;
            
            while (low <= high) {
                int mid = low + (high - low) / 2;
                long missingCount = arr[mid] - (mid + 1);
                if (missingCount < m) {
                    idx = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            
            results[i] = m + idx + 1;
        }
        return results;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) {
            sc.close();
            return;
        }
        int n = sc.nextInt();
        int q = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        long[][] queries = new long[q][2];
        for (int i = 0; i < q; i++) {
            queries[i][0] = sc.nextLong();
            queries[i][1] = sc.nextLong();
        }
        Solution solution = new Solution();
        long[] results = solution.solve(arr, queries);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < results.length; i++) {
            if (i > 0) sb.append('\n');
            sb.append(results[i]);
        }
        System.out.println(sb.toString());
        sc.close();
    }
}
