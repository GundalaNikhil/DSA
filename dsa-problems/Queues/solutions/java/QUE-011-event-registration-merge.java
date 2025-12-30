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

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = sc.nextInt();
            }
            int m = sc.nextInt();
            int[] b = new int[m];
            for (int i = 0; i < m; i++) {
                b[i] = sc.nextInt();
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
