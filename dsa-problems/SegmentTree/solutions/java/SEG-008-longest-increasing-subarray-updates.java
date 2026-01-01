import java.util.*;

class Solution {
    static class Node {
        int maxLen;
        int prefLen;
        int suffLen;
        int len;
        int leftVal;
        int rightVal;
        
        Node(int val) {
            maxLen = prefLen = suffLen = len = 1;
            leftVal = rightVal = val;
        }
        
        Node() {}
    }
    
    private Node[] tree;
    private int n;

    public int[] process(int[] arr, int[][] updates) {
        n = arr.length;
        tree = new Node[4 * n];
        
        build(arr, 0, 0, n - 1);
        
        int[] results = new int[updates.length];
        for (int i = 0; i < updates.length; i++) {
            int idx = updates[i][0];
            int val = updates[i][1];
            update(0, 0, n - 1, idx, val);
            results[i] = tree[0].maxLen;
        }
        return results;
    }

    private Node merge(Node left, Node right) {
        Node res = new Node();
        res.len = left.len + right.len;
        res.leftVal = left.leftVal;
        res.rightVal = right.rightVal;
        
        res.maxLen = Math.max(left.maxLen, right.maxLen);
        res.prefLen = left.prefLen;
        res.suffLen = right.suffLen;
        
        if (left.rightVal < right.leftVal) {
            res.maxLen = Math.max(res.maxLen, left.suffLen + right.prefLen);
            if (left.prefLen == left.len) {
                res.prefLen = left.len + right.prefLen;
            }
            if (right.suffLen == right.len) {
                res.suffLen = right.len + left.suffLen;
            }
        }
        return res;
    }

    private void build(int[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = new Node(arr[start]);
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    private void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = new Node(val);
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
            int[][] updates = new int[q][2];
            for (int i = 0; i < q; i++) {
                String type = sc.next(); // SET
                updates[i][0] = sc.nextInt();
                updates[i][1] = sc.nextInt();
            }
            Solution sol = new Solution();
            int[] results = sol.process(arr, updates);
            for (int res : results) {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
