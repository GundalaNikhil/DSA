import java.util.*;

class TrieNode {
    TrieNode[] children = new TrieNode[2];  // 0 and 1
}

class Solution {
    private TrieNode root = new TrieNode();
    private static final int MAX_BITS = 30;

    public int minimizeXOR(int[] a, int X) {
        int n = a.length;
        int[] prefix = new int[n + 1];

        // Compute prefix XORs
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] ^ a[i];
        }

        int minXor = Integer.MAX_VALUE;

        // Process each prefix
        for (int j = 0; j <= n; j++) {
            if (root.children[0] != null || root.children[1] != null) {
                // Query for best match
                int target = prefix[j] ^ X;
                int closest = query(target);
                minXor = Math.min(minXor, closest ^ target);
            }
            // Insert current prefix
            insert(prefix[j]);
        }

        return minXor;
    }

    private void insert(int num) {
        TrieNode node = root;
        for (int i = MAX_BITS; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (node.children[bit] == null) {
                node.children[bit] = new TrieNode();
            }
            node = node.children[bit];
        }
    }

    private int query(int num) {
        TrieNode node = root;
        int result = 0;

        for (int i = MAX_BITS; i >= 0; i--) {
            int bit = (num >> i) & 1;

            // Prefer same bit (to minimize XOR)
            if (node.children[bit] != null) {
                node = node.children[bit];
            } else {
                // Take opposite bit
                result |= (1 << i);
                node = node.children[1 - bit];
            }
        }

        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int X = sc.nextInt();

        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        Solution solution = new Solution();
        int result = solution.minimizeXOR(a, X);

        System.out.println(result);
        sc.close();
    }
}
