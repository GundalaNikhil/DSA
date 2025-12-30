import java.util.*;

class Solution {
    public String nimLimit(int n, int[] A, int[] L) {
        long xorSum = 0;
        for (int i = 0; i < n; i++) {
            xorSum ^= (A[i] % (L[i] + 1));
        }
        return xorSum > 0 ? "First" : "Second";
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int[] A = new int[n];
            for (int i = 0; i < n; i++) {
                A[i] = sc.nextInt();
            }
            int[] L = new int[n];
            for (int i = 0; i < n; i++) {
                L[i] = sc.nextInt();
            }

            Solution solution = new Solution();
            System.out.println(solution.nimLimit(n, A, L));
        }
        sc.close();
    }
}
