import java.util.*;

class Solution {
    public long[] computePrefixHashes(String s, long B, long M) {
        int n = s.length();
        long[] hashes = new long[n];
        long currentHash = 0;

        for (int i = 0; i < n; i++) {
            // Use long to prevent overflow before modulo
            // s.charAt(i) returns char, which promotes to int/long automatically
            currentHash = (currentHash * B + s.charAt(i)) % M;
            hashes[i] = currentHash;
        }

        return hashes;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            if (sc.hasNextLong()) {
                long B = sc.nextLong();
                long M = sc.nextLong();

                Solution solution = new Solution();
                long[] result = solution.computePrefixHashes(s, B, M);

                for (int i = 0; i < result.length; i++) {
                    System.out.print(result[i]);
                    if (i < result.length - 1) System.out.print(" ");
                }
                System.out.println();
            }
        }
        sc.close();
    }
}
