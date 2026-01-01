import java.util.*;

class Solution {
    private int[] tree;
    private int[] vals;
    private boolean[] active;
    private int n;

    private int gcd(int a, int b) {
        a = Math.abs(a);
        b = Math.abs(b);
        if (a == 0) return b;
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    public List<Integer> process(int[] arr, boolean[] forbidden, List<String[]> ops) {
        n = arr.length;
        vals = arr.clone();
        active = new boolean[n];
        for (int i = 0; i < n; i++) active[i] = !forbidden[i];
        
        tree = new int[4 * n];
        build(0, 0, n - 1);
        
        List<Integer> results = new ArrayList<>();
        
        for (String[] op : ops) {
            String type = op[0];
            if (type.equals("TOGGLE")) {
                int idx = Integer.parseInt(op[1]);
                active[idx] = !active[idx];
                int effectiveVal = active[idx] ? vals[idx] : 0;
                update(0, 0, n - 1, idx, effectiveVal);
            } else if (type.equals("SET")) {
                int idx = Integer.parseInt(op[1]);
                int val = Integer.parseInt(op[2]);
                vals[idx] = val;
                int effectiveVal = active[idx] ? vals[idx] : 0;
                update(0, 0, n - 1, idx, effectiveVal);
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                results.add(query(0, 0, n - 1, l, r));
            }
        }
        return results;
    }

    private void build(int node, int start, int end) {
        if (start == end) {
            tree[node] = active[start] ? vals[start] : 0;
        } else {
            int mid = (start + end) / 2;
            build(2 * node + 1, start, mid);
            build(2 * node + 2, mid + 1, end);
            tree[node] = gcd(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    private void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val;
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            tree[node] = gcd(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    private int query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return 0;
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        int p1 = query(2 * node + 1, start, mid, l, r);
        int p2 = query(2 * node + 2, mid + 1, end, l, r);
        return gcd(p1, p2);
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
            int f = sc.nextInt();
            boolean[] forbidden = new boolean[n];
            for (int i = 0; i < f; i++) {
                forbidden[sc.nextInt()] = true;
            }
            List<String[]> ops = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String type = sc.next();
                if (type.equals("TOGGLE")) {
                    ops.add(new String[]{type, sc.next()});
                } else if (type.equals("SET")) {
                    ops.add(new String[]{type, sc.next(), sc.next()});
                } else {
                    ops.add(new String[]{type, sc.next(), sc.next()});
                }
            }
            Solution sol = new Solution();
            List<Integer> results = sol.process(arr, forbidden, ops);
            for (int res : results) {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
