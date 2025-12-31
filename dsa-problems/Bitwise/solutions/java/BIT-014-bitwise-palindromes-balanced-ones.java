import java.util.*;

class Solution {
    private long makePalindrome(long half, int len) {
        long res = half;
        int bitsToMirror = len / 2;
        // If len is 5 (10101), half has 3 bits. We mirror non-middle.
        // If len is 4 (1001), half has 2 bits. We mirror all.
        // General: We mirror 'len - ceil(len/2)' bits.
        // Which are the lower bits of half? No, the whole half is prefix.
        // Example len=5. half=110 (6). Palindrome 11011.
        // Sequence: half (110) then append reverse of 11 (3).

        long lower = 0;
        long temp = half;
        if (len % 2 == 1) temp >>= 1; // Skip middle bit for mirroring

        for (int i = 0; i < len / 2; i++) {
            lower = (lower << 1) | (temp & 1);
            temp >>= 1;
        }
        return (res << (len / 2)) | lower;
    }

    // Counts valid palindromes <= N with exact bit length 'len'
    private long countForLen(long N, int len, boolean isLimit) {
        int halfLen = (len + 1) / 2;
        long minHalf = 1L << (halfLen - 1);
        long maxHalf = (1L << halfLen) - 1;

        if (isLimit) {
            long prefix = N >>> (len - halfLen);
            if (prefix < minHalf) return 0; // Should not happen if len matches N
            maxHalf = Math.min(maxHalf, prefix);
        }

        long count = 0;

        // If len is odd, half must be even (LSB 0) implies palindrome middle is 0.
        // If len is even, any half is valid.

        // We need numbers in [minHalf, maxHalf] satisfying condition
        // If isLimit is true and we pick maxHalf, we must verify reconstruction.
        // So standard logic: Count strictly less than maxHalf, then check maxHalf.

        long limitVal = maxHalf;

        // Count in range [minHalf, limitVal - 1]
        // If len even: count all integers.
        // If len odd: count even integers.

        long validBelow = 0;

        if (limitVal > minHalf) {
            if (len % 2 == 0) {
                validBelow = limitVal - minHalf;
            } else {
                // Count evens in [minHalf, limitVal - 1]
                // minHalf is power of 2, so it is even.
                // Range [E, X). Count evens is (X - E + 1) / 2
                validBelow = (limitVal - minHalf + 1) / 2;
            }
        }

        // Check boundary limitVal
        boolean checkBoundary = true;

        // If len odd and limitVal is odd, it's invalid
        if (len % 2 == 1 && (limitVal % 2 != 0)) checkBoundary = false;

        if (checkBoundary) {
            long p = makePalindrome(limitVal, len);
            if (!isLimit || p <= N) {
                validBelow++;
            }
        }

        return validBelow;
    }

    private long solve(long N) {
        if (N < 0) return 0;
        if (N == 0) return 1; // 0 is palindrome and even bits (0)

        // Length of N
        int L = 0;
        long temp = N;
        while (temp > 0) { L++; temp >>= 1; }

        long total = 1; // Count 0

        // Lengths strictly less than L
        for (int len = 1; len < L; len++) {
            total += countForLen(Long.MAX_VALUE, len, false);
        }

        // Length equal to L
        total += countForLen(N, L, true);

        return total;
    }

    public long countBitwisePalindromesBalancedOnes(long L, long R) {
        return solve(R) - solve(L - 1);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long L = sc.nextLong();
        long R = sc.nextLong();

        Solution solution = new Solution();
        System.out.println(solution.countBitwisePalindromesBalancedOnes(L, R));
        sc.close();
    }
}
