import java.util.*;

class Solution {
    public String compressWithWindow(String s, int w) {
        if (s == null || s.isEmpty()) {
            return "";
        }

        StringBuilder result = new StringBuilder();
        int i = 0;
        int n = s.length();

        while (i < n) {
            int start = i;
            char ch = s.charAt(i);

            // Count consecutive occurrences
            while (i < n && s.charAt(i) == ch) {
                i++;
            }

            int runLength = i - start;

            // Compress if >= threshold
            if (runLength >= w) {
                result.append(ch).append(runLength);
            } else {
                for (int j = 0; j < runLength; j++) {
                    result.append(ch);
                }
            }
        }

        return result.toString();
    }
}

















class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int w = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.compressWithWindow(s, w));
        sc.close();
    }
}
