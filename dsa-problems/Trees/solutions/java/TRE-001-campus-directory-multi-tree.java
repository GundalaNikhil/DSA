import java.util.*;

class Solution {
    static class Node {
        int val;
        int left = -1;
        int right = -1;
    }

    public List<List<Integer>> traverseAll(int n, int[][] nodes) {
        List<List<Integer>> results = new ArrayList<>();
        if (n == 0) {
            results.add(new ArrayList<>());
            results.add(new ArrayList<>());
            results.add(new ArrayList<>());
            return results;
        }

        Node[] tree = new Node[n];
        for (int i = 0; i < n; i++) {
            tree[i] = new Node();
            tree[i].val = nodes[i][0];
            tree[i].left = nodes[i][1];
            tree[i].right = nodes[i][2];
        }

        List<Integer> pre = new ArrayList<>();
        List<Integer> in = new ArrayList<>();
        List<Integer> post = new ArrayList<>();

        preorder(tree, 0, pre);
        inorder(tree, 0, in);
        postorder(tree, 0, post);

        results.add(pre);
        results.add(in);
        results.add(post);
        return results;
    }

    private void preorder(Node[] tree, int u, List<Integer> list) {
        if (u == -1) return;
        list.add(tree[u].val);
        preorder(tree, tree[u].left, list);
        preorder(tree, tree[u].right, list);
    }

    private void inorder(Node[] tree, int u, List<Integer> list) {
        if (u == -1) return;
        inorder(tree, tree[u].left, list);
        list.add(tree[u].val);
        inorder(tree, tree[u].right, list);
    }

    private void postorder(Node[] tree, int u, List<Integer> list) {
        if (u == -1) return;
        postorder(tree, tree[u].left, list);
        postorder(tree, tree[u].right, list);
        list.add(tree[u].val);
    }

    public boolean structuralIdentical(int n1, int[][] t1, int n2, int[][] t2) {
        if (n1 == 0 && n2 == 0) return true;
        if (n1 == 0 || n2 == 0) return false;
        return checkStructure(t1, 0, t2, 0);
    }

    private boolean checkStructure(int[][] t1, int u1, int[][] t2, int u2) {
        if (u1 == -1 && u2 == -1) return true;
        if (u1 == -1 || u2 == -1) return false;

        // Check left child existence
        boolean l1 = t1[u1][1] != -1;
        boolean l2 = t2[u2][1] != -1;
        if (l1 != l2) return false;

        // Check right child existence
        boolean r1 = t1[u1][2] != -1;
        boolean r2 = t2[u2][2] != -1;
        if (r1 != r2) return false;

        return checkStructure(t1, t1[u1][1], t2, t2[u2][1]) &&
               checkStructure(t1, t1[u1][2], t2, t2[u2][2]);
    }

    public List<String> matchingTraversals(List<List<Integer>> t1, List<List<Integer>> t2) {
        List<String> matches = new ArrayList<>();
        if (t1.get(0).equals(t2.get(0))) matches.add("preorder");
        if (t1.get(1).equals(t2.get(1))) matches.add("inorder");
        if (t1.get(2).equals(t2.get(2))) matches.add("postorder");
        return matches;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n1 = sc.nextInt();
        int[][] t1 = new int[n1][3];
        for (int i = 0; i < n1; i++) {
            t1[i][0] = sc.nextInt();
            t1[i][1] = sc.nextInt();
            t1[i][2] = sc.nextInt();
        }
        int n2 = sc.nextInt();
        int[][] t2 = new int[n2][3];
        for (int i = 0; i < n2; i++) {
            t2[i][0] = sc.nextInt();
            t2[i][1] = sc.nextInt();
            t2[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        List<List<Integer>> trav1 = solution.traverseAll(n1, t1);
        List<List<Integer>> trav2 = solution.traverseAll(n2, t2);
        boolean same = solution.structuralIdentical(n1, t1, n2, t2);
        List<String> matches = solution.matchingTraversals(trav1, trav2);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 3; i++) {
            sb.append(join(trav1.get(i))).append('\n');
        }
        for (int i = 0; i < 3; i++) {
            sb.append(join(trav2.get(i))).append('\n');
        }
        sb.append(same ? "true" : "false").append('\n');
        if (matches.isEmpty()) {
            sb.append("NONE");
        } else {
            sb.append(String.join(" ", matches));
        }
        System.out.print(sb.toString());
        sc.close();
    }

    private static String join(List<Integer> list) {
        if (list.isEmpty()) return "";
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < list.size(); i++) {
            sb.append(list.get(i));
            if (i + 1 < list.size()) sb.append(' ');
        }
        return sb.toString();
    }
}
