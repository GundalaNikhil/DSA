import java.util.*;

class Solution {
    public int[] reservoirSample(int n, int k, long seed) {
        if (k == 0) return new int[0];
        if (k > n) k = n; // Should not happen based on constraints but safe to handle

        int[] reservoir = new int[k];
        for (int i = 0; i < k; i++) {
            reservoir[i] = i + 1;
        }

        long state = seed;

        for (int i = k + 1; i <= n; i++) {
            // LCG Update
            state = state * 6364136223846793005L + 1;

            // Generate random index j in [0, i-1]
            // Use Long.compareUnsigned logic or simple remainder if positive
            // Since state can be negative (interpreted as unsigned), we need careful modulo.
            // Java's % operator returns negative if dividend is negative.
            // Correct way for unsigned modulo by i:
            // Long.remainderUnsigned(state, i)

            long j = Long.remainderUnsigned(state, i);

            if (j < k) {
                reservoir[(int)j] = i;
            }
        }

        return reservoir;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            long seed = sc.nextLong();

            Solution solution = new Solution();
            int[] res = solution.reservoirSample(n, k, seed);
            for (int i = 0; i < res.length; i++) {
                System.out.print(res[i]);
                if (i + 1 < res.length) System.out.print(" ");
            }
            System.out.println();
        }
        sc.close();
    }
}
