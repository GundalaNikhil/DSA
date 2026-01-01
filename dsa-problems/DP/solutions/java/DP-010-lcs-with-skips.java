import java.util.*;

class Solution {
    public int lcsWithSkipLimit(String a, String b, int s) {
        int n = a.length(), m = b.length();
        int[] prev = new int[m + 1];
        int[] cur = new int[m + 1];

        for (int i = 1; i <= n; i++) {
            char ca = a.charAt(i - 1);
            cur[0] = 0;
            for (int j = 1; j <= m; j++) {
                if (ca == b.charAt(j - 1)) {
                    cur[j] = prev[j - 1] + 1;
                } else {
                    cur[j] = Math.max(prev[j], cur[j - 1]);
                }
            }
            int[] tmp = prev; prev = cur; cur = tmp;
        }

        int L = prev[m];
        return (n - L <= s) ? L : -1;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine().trim();
        String b = sc.nextLine().trim();
        int s = sc.nextInt();
        System.out.println(new Solution().lcsWithSkipLimit(a, b, s));
        sc.close();
    }
}
