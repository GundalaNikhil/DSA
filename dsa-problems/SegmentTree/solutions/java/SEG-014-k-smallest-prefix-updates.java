import java.util.*;

class Solution {
    static class Node {
        long sum;
        long lazySet;
        boolean hasLazy;
        
        Node() {
            lazySet = 0;
            hasLazy = false;
        }
    }
    
    private Node[] tree;
    private int n;

    public List<Long> process(long[] arr, List<String[]> ops) {
        n = arr.length;
        tree = new Node[4 * n];
        for(int i=0; i<4*n; i++) tree[i] = new Node();
        
        build(arr, 0, 0, n - 1);
        
        List<Long> results = new ArrayList<>();
        
        for (String[] op : ops) {
            if (op[0].equals("SETPREFIX")) {
                int k = Integer.parseInt(op[1]);
                long x = Long.parseLong(op[2]);
                if (k > 0) update(0, 0, n - 1, 0, k - 1, x);
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                results.add(query(0, 0, n - 1, l, r));
            }
        }
        return results;
    }

    private void push(int node, int start, int end) {
        if (tree[node].hasLazy) {
            int mid = (start + end) / 2;
            long val = tree[node].lazySet;
            
            tree[2 * node + 1].lazySet = val;
            tree[2 * node + 1].hasLazy = true;
            tree[2 * node + 1].sum = val * (mid - start + 1);
            
            tree[2 * node + 2].lazySet = val;
            tree[2 * node + 2].hasLazy = true;
            tree[2 * node + 2].sum = val * (end - mid);
            
            tree[node].hasLazy = false;
        }
    }

    private void build(long[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node].sum = arr[start];
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node].sum = tree[2 * node + 1].sum + tree[2 * node + 2].sum;
        }
    }

    private void update(int node, int start, int end, int l, int r, long val) {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            tree[node].lazySet = val;
            tree[node].hasLazy = true;
            tree[node].sum = val * (end - start + 1);
            return;
        }
        
        push(node, start, end);
        int mid = (start + end) / 2;
        update(2 * node + 1, start, mid, l, r, val);
        update(2 * node + 2, mid + 1, end, l, r, val);
        tree[node].sum = tree[2 * node + 1].sum + tree[2 * node + 2].sum;
    }

    private long query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return 0;
        if (l <= start && end <= r) return tree[node].sum;
        
        push(node, start, end);
        int mid = (start + end) / 2;
        return query(2 * node + 1, start, mid, l, r) + 
               query(2 * node + 2, mid + 1, end, l, r);
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
                ops.add(new String[]{type, sc.next(), sc.next()});
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
