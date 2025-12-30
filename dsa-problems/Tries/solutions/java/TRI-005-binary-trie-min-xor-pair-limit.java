class TrieNode {
    TrieNode[] children = new TrieNode[2];
}

class Solution {
    private static final int MAX_BITS = 30;
    private TrieNode root;

    public int minXORPairUnderLimit(int[] arr, int L) {
        if (arr == null || arr.length < 2) return -1;

        root = new TrieNode();
        int minXOR = Integer.MAX_VALUE;

        for (int num : arr) {
            if (root.children[0] != null || root.children[1] != null) {
                int closest = findClosest(num);
                int xorVal = num ^ closest;
                if (xorVal <= L) {
                    minXOR = Math.min(minXOR, xorVal);
                }
            }
            insert(num);
        }

        return minXOR == Integer.MAX_VALUE ? -1 : minXOR;
    }

    private void insert(int num) {
        TrieNode curr = root;
        for (int i = MAX_BITS; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (curr.children[bit] == null) {
                curr.children[bit] = new TrieNode();
            }
            curr = curr.children[bit];
        }
    }

    private int findClosest(int num) {
        TrieNode curr = root;
        int result = 0;

        for (int i = MAX_BITS; i >= 0; i--) {
            int bit = (num >> i) & 1;

            // Prefer same bit for minimum XOR
            if (curr.children[bit] != null) {
                curr = curr.children[bit];
            } else {
                bit = 1 - bit;
                curr = curr.children[bit];
            }

            result |= (bit << i);
        }

        return result;
    }
}

// Time: O(n × 30), Space: O(n × 30)
