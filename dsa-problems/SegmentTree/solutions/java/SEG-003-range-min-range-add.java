import java.util.*;

class Solution {
    private long[] tree;
    private long[] lazy;
    private int n;

    public List<Long> process(long[] arr, List<String[]> ops) {
        n = arr.length;
        tree = new long[4 * n];
        lazy = new long[4 * n];
        
        build(arr, 0, 0, n - 1);
        
        List<Long> results = new ArrayList<>();
        
        for (String[] op : ops) {
            String type = op[0];
            if (type.equals("ADD")) {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                long x = Long.parseLong(op[3]);
                update(0, 0, n - 1, l, r, x);
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                results.add(query(0, 0, n - 1, l, r));
            }
        }
        return results;
    }

    private void build(long[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = Math.min(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    private void push(int node) {
        if (lazy[node] != 0) {
            // Left child
            tree[2 * node + 1] += lazy[node];
            lazy[2 * node + 1] += lazy[node];
            
            // Right child
            tree[2 * node + 2] += lazy[node];
            lazy[2 * node + 2] += lazy[node];
            
            lazy[node] = 0;
        }
    }

    private void update(int node, int start, int end, int l, int r, long val) {
        if (l > end || r < start) return;

        if (l <= start && end <= r) {
            tree[node] += val;
            lazy[node] += val;
            return;
        }

        push(node);
        int mid = (start + end) / 2;
        update(2 * node + 1, start, mid, l, r, val);
        update(2 * node + 2, mid + 1, end, l, r, val);
        tree[node] = Math.min(tree[2 * node + 1], tree[2 * node + 2]);
    }

    private long query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return Long.MAX_VALUE;

        if (l <= start && end <= r) {
            return tree[node];
        }

        push(node);
        int mid = (start + end) / 2;
        return Math.min(query(2 * node + 1, start, mid, l, r),
                        query(2 * node + 2, mid + 1, end, l, r));
    }
}

class Main {
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
                if (type.equals("ADD")) {
                    ops.add(new String[]{type, sc.next(), sc.next(), sc.next()});
                } else {
                    ops.add(new String[]{type, sc.next(), sc.next()});
                }
            }
            Solution sol = new Solution();
            List<Long> results = sol.process(arr, ops);
            for (long res : results) {
                if (res == Long.MAX_VALUE) {
                    System.out.println("inf");
                } else {
                    System.out.println(res);
                }
            }
        }
        sc.close();
    }
}
