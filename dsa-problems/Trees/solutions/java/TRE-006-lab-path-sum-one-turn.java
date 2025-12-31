import java.util.*;

class Solution {
    boolean found = false;

    public boolean hasOneTurnPath(int n, long[] values, int[] left, int[] right, long target) {
        if (n == 0) return false;
        found = false;
        // Start DFS from root. Root starts a Left-chain.
        dfs(0, 0, new HashSet<>(), values, left, right, target, true);
        return found;
    }

    // isStart: true if 'u' is the start of a new Left-chain (root or right child)
    private void dfs(int u, long currentLeftSum, Set<Long> prefixes, 
                     long[] values, int[] left, int[] right, long target, boolean isStart) {
        if (u == -1 || found) return;

        long val = values[u];
        long nextSum = currentLeftSum + val;

        // If we are not the start, we have incoming Left edges. We can Turn Right.
        if (!isStart) {
            checkRightChain(right[u], val, nextSum, prefixes, values, left, right, target);
        }

        // Add current prefix to set for children
        prefixes.add(currentLeftSum);

        // 1. Continue Left
        dfs(left[u], nextSum, prefixes, values, left, right, target, false);

        // Backtrack for this chain
        prefixes.remove(currentLeftSum);

        // 2. Go Right (Starts a NEW Left-chain logic for the subtree)
        // We pass a NEW empty set because the Left-chain breaks here.
        dfs(right[u], 0, new HashSet<>(), values, left, right, target, true);
    }

    private void checkRightChain(int u, long turnVal, long turnLeftSum, Set<Long> prefixes,
                                 long[] values, int[] left, int[] right, long target) {
        long currentRightSum = 0;
        int curr = u;
        while (curr != -1 && !found) {
            currentRightSum += values[curr];
            // Total = SuffixLeft + RightChainSum
            // SuffixLeft = turnLeftSum - somePrefix
            // Total = (turnLeftSum - somePrefix) + currentRightSum = T
            // somePrefix = turnLeftSum + currentRightSum - T
            long neededPrefix = turnLeftSum + currentRightSum - target;
            if (prefixes.contains(neededPrefix)) {
                found = true;
                return;
            }
            curr = right[curr];
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[] values = new long[n];
        int[] left = new int[n];
        int[] right = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = sc.nextLong();
            left[i] = sc.nextInt();
            right[i] = sc.nextInt();
        }
        long target = 0;
        if (sc.hasNextLong()) target = sc.nextLong();

        Solution solution = new Solution();
        System.out.println(solution.hasOneTurnPath(n, values, left, right, target) ? "true" : "false");
        sc.close();
    }
}
