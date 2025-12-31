import java.util.*;

class Solution {
    public long totalSize(int[] sizes) {
        long S = 0;
        for (int s : sizes) {
            S += (long)s * s;
        }
        return S;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLong()) {
            long n = sc.nextLong();
            int t = sc.nextInt();
            int[] sizes = new int[t];
            for (int i = 0; i < t; i++) sizes[i] = sc.nextInt();
    
            Solution solution = new Solution();
            long S = solution.totalSize(sizes);
            System.out.println(S + " " + (S <= 4 * n ? "YES" : "NO"));
        }
        sc.close();
    }
}
