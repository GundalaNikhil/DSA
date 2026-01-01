import java.util.*;

class Solution {
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public int[] prefixGcds(int[] a) {
        int n = a.length;
        if (n == 0) return new int[0];
        
        int[] pref = new int[n];
        pref[0] = Math.abs(a[0]);
        
        for (int i = 1; i < n; i++) {
            pref[i] = gcd(pref[i - 1], Math.abs(a[i]));
        }
        
        return pref;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        
        int n = sc.nextInt();
        int q = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] pref = solution.prefixGcds(a);
        
        for (int i = 0; i < q; i++) {
            int r = sc.nextInt();
            System.out.println(pref[r]);
        }
        sc.close();
    }
}
