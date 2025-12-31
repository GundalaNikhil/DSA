import java.util.*;

class Solution {
    public long bitwiseAndSkipMultiples(long L, long R, int m) {
        // If range is manageable, iterate.
        // Threshold: 3 million ops is trivial (~10ms)
        if (R - L <= 3000000) {
            long ans = -1;
            boolean found = false;
            for (long i = L; i <= R; i++) {
                if (i % m != 0) {
                    ans &= i;
                    found = true;
                }
            }
            return found ? ans : -1;
        }

        // Large Range Logic
        // 1. Compute Standard Range AND
        // Logic: Keep common prefix of L and R, rest 0.
        // Efficient way: while L < R, R &= (R-1) ? No, standard algo:
        /*
           shift = 0
           while (L != R) { L >>=1; R >>=1; shift++; }
           res = L << shift
        */
        // Or cleaner: bits where L and R match prefix.
        
        // However, R - L is HUGE. So L and R differ at a high bit.
        // We can just find the highest diff bit.
        // Or simply:
        
        long diff = L ^ R;
        // Highest Set Bit of diff
        if (diff == 0) return (L % m != 0) ? L : -1; 
        
        // Mask out everything below the MSB of diff
        // msb(x) can be found by Long.highestOneBit(diff)
        // If diff has bit K set, then bits 0..K must become 0.
        // Mask = ~((highestOneBit(diff) << 1) - 1) ?
        // Simpler loop:
        
        long lTemp = L;
        long rTemp = R;
        int shift = 0;
        while (lTemp != rTemp) {
            lTemp >>= 1;
            rTemp >>= 1;
            shift++;
        }
        long standardAnd = lTemp << shift;
        
        // Special Case: m=2 means we skipped all evens. 
        // Odd & Odd ... always has bit 0 set.
        if (m == 2) {
            standardAnd |= 1;
        }
        
        return standardAnd;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLong()) return;
        long L = sc.nextLong();
        long R = sc.nextLong();
        int m = sc.nextInt();

        Solution solution = new Solution();
        long result = solution.bitwiseAndSkipMultiples(L, R, m);
        System.out.println(result);
        sc.close();
    }
}
