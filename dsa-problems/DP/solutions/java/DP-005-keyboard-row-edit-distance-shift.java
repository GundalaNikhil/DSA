import java.util.*;

class Solution {
    private static final String ROW1 = "qwertyuiop";
    private static final String ROW2 = "asdfghjkl";
    private static final String ROW3 = "zxcvbnm";
    private static final String LEFT = "qwertasdfgzxcvb";

    private static int row(char c) {
        if (ROW1.indexOf(c) >= 0) return 1;
        if (ROW2.indexOf(c) >= 0) return 2;
        return 3;
    }

    private static int hand(char c) {
        return LEFT.indexOf(c) >= 0 ? 0 : 1;
    }

    private static int replaceCost(char x, char y) {
        if (x == y) return 0;
        int rx = row(x), ry = row(y);
        if (rx == ry) return 1;
        return hand(x) == hand(y) ? 2 : 3;
    }

    public int minKeyboardEditCost(String a, String b) {
        int n = a.length(), m = b.length();
        int[] prev = new int[m + 1];
        int[] cur = new int[m + 1];

        for (int j = 0; j <= m; j++) prev[j] = j;

        for (int i = 1; i <= n; i++) {
            cur[0] = i;
            char ca = a.charAt(i - 1);
            for (int j = 1; j <= m; j++) {
                char cb = b.charAt(j - 1);
                int del = prev[j] + 1;
                int ins = cur[j - 1] + 1;
                int rep = prev[j - 1] + replaceCost(ca, cb);
                cur[j] = Math.min(del, Math.min(ins, rep));
            }
            int[] tmp = prev; prev = cur; cur = tmp;
        }

        return prev[m];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.hasNextLine() ? sc.nextLine().trim() : "";
        String b = sc.hasNextLine() ? sc.nextLine().trim() : "";
        System.out.println(new Solution().minKeyboardEditCost(a, b));
        sc.close();
    }
}
