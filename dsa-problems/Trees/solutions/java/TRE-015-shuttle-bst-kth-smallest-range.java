import java.util.*;

class Solution {
    static class TreeNode {
        long val;
        TreeNode left, right;
        TreeNode(long val) { this.val = val; }
    }

    private int count;
    private long result;

    public long kthInRange(long[] values, long L, long R, int k) {
        TreeNode root = null;
        for (long v : values) {
            root = insert(root, v);
        }

        count = 0;
        result = -1;
        inorder(root, L, R, k);
        return result;
    }

    private TreeNode insert(TreeNode node, long val) {
        if (node == null) return new TreeNode(val);
        if (val < node.val) {
            node.left = insert(node.left, val);
        } else {
            node.right = insert(node.right, val);
        }
        return node;
    }

    private void inorder(TreeNode node, long L, long R, int k) {
        if (node == null || result != -1) return;

        // Pruning: if node.val < L, left subtree is useless (all < L)
        // Correct logic: Visit left if it COULD contain values >= L.
        // Left child values are < node.val.
        // If node.val <= L, then left child < L. Useless.
        // So visit left only if node.val > L.
        
        if (node.val > L) {
            inorder(node.left, L, R, k);
        }

        if (result != -1) return; // Check again after returning from left

        if (node.val >= L && node.val <= R) {
            count++;
            if (count == k) {
                result = node.val;
                return;
            }
        }

        // Pruning: Visit right only if node.val < R.
        // If node.val >= R, right child > R. Useless.
        if (node.val < R) {
            inorder(node.right, L, R, k);
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        long[] values = new long[n];
        for (int i = 0; i < n; i++) values[i] = sc.nextLong();
        long L = 0, R = 0;
        if (sc.hasNextLong()) L = sc.nextLong();
        if (sc.hasNextLong()) R = sc.nextLong();
        int k = 0;
        if (sc.hasNextInt()) k = sc.nextInt();

        Solution solution = new Solution();
        System.out.println(solution.kthInRange(values, L, R, k));
        sc.close();
    }
}
