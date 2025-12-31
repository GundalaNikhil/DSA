import java.util.*;

class Solution {
    static class Pair {
        long val;
        int idx;
        
        Pair(long val, int idx) {
            this.val = val;
            this.idx = idx;
        }
    }
    
    private Pair[] tree;
    private int n;

    public int[] process(long[] arr, List<String[]> ops) {
        n = arr.length;
        tree = new Pair[4 * n];
        
        build(arr, 0, 0, n - 1);
        
        List<Integer> results = new ArrayList<>();
        
        for (String[] op : ops) {
            if (op[0].equals("SET")) {
                int idx = Integer.parseInt(op[1]);
                long val = Long.parseLong(op[2]);
                update(0, 0, n - 1, idx, val);
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                Pair res = query(0, 0, n - 1, l, r);
                results.add(res.idx);
            }
        }
        
        int[] out = new int[results.size()];
        for (int i = 0; i < results.size(); i++) out[i] = results.get(i);
        return out;
    }

    private Pair merge(Pair p1, Pair p2) {
        if (p1.val < p2.val) return p1;
        if (p2.val < p1.val) return p2;
        return p1.idx < p2.idx ? p1 : p2;
    }

    private void build(long[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = new Pair(arr[start], start);
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    private void update(int node, int start, int end, int idx, long val) {
        if (start == end) {
            tree[node] = new Pair(val, idx);
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    private Pair query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return new Pair(Long.MAX_VALUE, -1);
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        Pair p1 = query(2 * node + 1, start, mid, l, r);
        Pair p2 = query(2 * node + 2, mid + 1, end, l, r);
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
                ops.add(new String[]{type, sc.next(), sc.next()});
            }
            Solution sol = new Solution();
            int[] results = sol.process(arr, ops);
            for (int res : results) {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
