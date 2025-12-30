import java.util.*;

class Solution {
    public long distinctSubarrayXors(int[] a) {
        int n = a.length;
        // Total subarrays: n*(n+1)/2
        // Be careful with integer overflow for size index?
        // n=10000 -> size ~ 5*10^7. Fits in int.
        int totalSubarrays = n * (n + 1) / 2;
        int[] results = new int[totalSubarrays];
        
        int idx = 0;
        for (int i = 0; i < n; i++) {
            int currentXor = 0;
            for (int j = i; j < n; j++) {
                currentXor ^= a[j];
                results[idx++] = currentXor;
            }
        }
        
        // Sorting primitive array is memory efficient (Dual-Pivot Quicksort)
        Arrays.sort(results);
        
        if (totalSubarrays == 0) return 0;
        
        long distinctCount = 1;
        for (int i = 1; i < totalSubarrays; i++) {
            if (results[i] != results[i-1]) {
                distinctCount++;
            }
        }
        
        return distinctCount;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.distinctSubarrayXors(a));
        sc.close();
    }
}
