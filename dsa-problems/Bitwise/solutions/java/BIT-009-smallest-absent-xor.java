import java.util.*;

class Solution {
    public long smallestAbsentXor(int[] a) {
        int[] basis = new int[32];
        
        for (int x : a) {
            for (int i = 30; i >= 0; i--) {
                if (((x >> i) & 1) == 1) {
                    if (basis[i] == 0) {
                        basis[i] = x;
                        break;
                    }
                    x ^= basis[i];
                }
            }
        }
        
        for (int i = 0; i <= 30; i++) {
            if (basis[i] == 0) {
                return (1L << i);
            }
        }
        
        return (1L << 31);
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
        System.out.println(solution.smallestAbsentXor(a));
        sc.close();
    }
}
