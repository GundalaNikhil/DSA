import java.util.*;

class Solution {
    private int getGrundy(int k) {
        if (k == 0) return 0;
        if (k == 1) return 1;
        if (k == 2) return 0;
        // Pattern for k >= 3: 2, 1, 0 repeating
        int rem = k % 3;
        if (rem == 0) return 2;
        if (rem == 1) return 1;
        return 0;
    }

    public String stringGame(int n, String[] strings) {
        int xorSum = 0;
        for (String s : strings) {
            if (s.isEmpty()) continue;
            int groups = 1;
            for (int i = 1; i < s.length(); i++) {
                if (s.charAt(i) != s.charAt(i - 1)) {
                    groups++;
                }
            }
            xorSum ^= getGrundy(groups);
        }
        return xorSum > 0 ? "First" : "Second";
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            String[] strings = new String[n];
            for (int i = 0; i < n; i++) {
                strings[i] = sc.next();
            }

            Solution solution = new Solution();
            System.out.println(solution.stringGame(n, strings));
        }
        sc.close();
    }
}
