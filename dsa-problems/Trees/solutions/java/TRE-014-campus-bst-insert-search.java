import java.util.*;

class Solution {
    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int val) { this.val = val; }
    }

    private TreeNode root;

    public List<Integer> buildInorder(int[] values) {
        root = null;
        for (int v : values) {
            root = insert(root, v);
        }
        List<Integer> result = new ArrayList<>();
        inorder(root, result);
        return result;
    }

    public boolean searchValue(int[] values, int x) {
        // Note: We reuse the root built in buildInorder if called sequentially,
        // but for safety/independence, we can rebuild or assume state.
        // The template implies independent calls or stateful object.
        // Let's assume buildInorder is called first or we rebuild.
        // Given the template structure, it's safer to rebuild if root is null.
        if (root == null && values.length > 0) {
            buildInorder(values);
        }
        return search(root, x);
    }

    private TreeNode insert(TreeNode node, int val) {
        if (node == null) return new TreeNode(val);
        if (val < node.val) {
            node.left = insert(node.left, val);
        } else {
            // Duplicates to the right
            node.right = insert(node.right, val);
        }
        return node;
    }

    private void inorder(TreeNode node, List<Integer> result) {
        if (node == null) return;
        inorder(node.left, result);
        result.add(node.val);
        inorder(node.right, result);
    }

    private boolean search(TreeNode node, int x) {
        if (node == null) return false;
        if (node.val == x) return true;
        if (x < node.val) return search(node.left, x);
        return search(node.right, x);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int[] values = new int[n];
        for (int i = 0; i < n; i++) values[i] = sc.nextInt();
        int x = 0;
        if (sc.hasNextInt()) x = sc.nextInt();

        Solution solution = new Solution();
        List<Integer> inorder = solution.buildInorder(values);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < inorder.size(); i++) {
            if (i > 0) sb.append(' ');
            sb.append(inorder.get(i));
        }
        System.out.println(sb.toString());
        System.out.println(solution.searchValue(values, x) ? "true" : "false");
        sc.close();
    }
}
