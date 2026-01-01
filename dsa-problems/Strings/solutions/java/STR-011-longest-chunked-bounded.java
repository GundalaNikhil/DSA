import java.util.*;

class Solution {
    public int longestChunkedDecomposition(String s, int L) {
        int n = s.length();
        int left = 0, right = n - 1;
        int chunks = 0;

        while (left < right) {
            boolean matched = false;
            int maxLen = Math.min(L, (right - left + 1) / 2);

            for (int len = 1; len <= maxLen; len++) {
                String leftChunk = s.substring(left, left + len);
                String rightChunk = s.substring(right - len + 1, right + 1);

                if (leftChunk.equals(rightChunk)) {
                    chunks += 2;
                    left += len;
                    right -= len;
                    matched = true;
                    break;
                }
            }

            if (!matched) {
                break;
            }
        }

        // Add middle chunk if exists
        if (left <= right) {
            chunks++;
        }

        return chunks;
    }
}

















class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int L = sc.nextInt();
        Solution sol = new Solution();
        System.out.println(sol.longestChunkedDecomposition(s, L));
        sc.close();
    }
}
