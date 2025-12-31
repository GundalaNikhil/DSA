import java.util.*;

class Solution {
    static class Node {
        long sum1, sum2, sum3;
        
        Node(long val) {
            long v = val % 1000000007;
            if (v < 0) v += 1000000007;
            sum1 = v;
            sum2 = (v * v) % 1000000007;
            sum3 = (sum2 * v) % 1000000007;
        }
        
        Node() {}
    }
    
    private Node[] tree;
    private int n;
    private static final long MOD = 1000000007;

    public List<Long> process(long[] arr, List<String[]> ops) {
        n = arr.length;
        tree = new Node[4 * n];
        
        build(arr, 0, 0, n - 1);
        
        List<Long> results = new ArrayList<>();
        
        for (String[] op : ops) {
            if (op[0].equals("SET")) {
                int idx = Integer.parseInt(op[1]);
                long val = Long.parseLong(op[2]);
                update(0, 0, n - 1, idx, val);
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                int p = Integer.parseInt(op[3]);
                Node res = query(0, 0, n - 1, l, r);
                if (p == 1) results.add(res.sum1);
                else if (p == 2) results.add(res.sum2);
                else results.add(res.sum3);
            }
        }
        return results;
    }

    private Node merge(Node left, Node right) {
        Node res = new Node();
        res.sum1 = (left.sum1 + right.sum1) % MOD;
        res.sum2 = (left.sum2 + right.sum2) % MOD;
        res.sum3 = (left.sum3 + right.sum3) % MOD;
        return res;
    }

    private void build(long[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = new Node(arr[start]);
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    private void update(int node, int start, int end, int idx, long val) {
        if (start == end) {
            tree[node] = new Node(val);
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    private Node query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return new Node();
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        Node p1 = query(2 * node + 1, start, mid, l, r);
        Node p2 = query(2 * node + 2, mid + 1, end, l, r);
        return merge(p1, p2);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            long[] arr = new long[n];
            for (int i = 0; i < n; i++) arr[i] = sc.nextLong();
            List<String[]> ops = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String type = sc.next();
                if (type.equals("SET")) {
                    ops.add(new String[]{type, sc.next(), sc.next()});
                } else {
                    ops.add(new String[]{type, sc.next(), sc.next(), sc.next()});
                }
            }
            Solution sol = new Solution();
            List<Long> results = sol.process(arr, ops);
            for (long res : results) {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
