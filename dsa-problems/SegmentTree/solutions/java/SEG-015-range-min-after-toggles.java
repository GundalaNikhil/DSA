import java.util.*;

class Solution {
    static class Node {
        long minVal, maxVal;
        long lazyAdd;
        boolean lazyFlip;
        
        Node(long val) {
            minVal = maxVal = val;
            lazyAdd = 0;
            lazyFlip = false;
        }
        
        Node() {
            minVal = Long.MAX_VALUE;
            maxVal = Long.MIN_VALUE;
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
            if (op[0].equals("ADD")) {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                long x = Long.parseLong(op[3]);
                updateAdd(0, 0, n - 1, l, r, x);
            } else if (op[0].equals("FLIP")) {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                updateFlip(0, 0, n - 1, l, r);
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                results.add(query(0, 0, n - 1, l, r));
            }
        }
        return results;
    }

    private void push(int node, int start, int end) {
        if (tree[node].lazyFlip) {
            applyFlip(2 * node + 1);
            applyFlip(2 * node + 2);
            tree[node].lazyFlip = false;
        }
        if (tree[node].lazyAdd != 0) {
            applyAdd(2 * node + 1, tree[node].lazyAdd);
            applyAdd(2 * node + 2, tree[node].lazyAdd);
            tree[node].lazyAdd = 0;
        }
    }
    
    private void applyFlip(int node) {
        long temp = tree[node].minVal;
        tree[node].minVal = -tree[node].maxVal;
        tree[node].maxVal = -temp;
        tree[node].lazyAdd = -tree[node].lazyAdd;
        tree[node].lazyFlip = !tree[node].lazyFlip;
    }
    
    private void applyAdd(int node, long val) {
        tree[node].minVal += val;
        tree[node].maxVal += val;
        tree[node].lazyAdd += val;
    }

    private void merge(int node) {
        tree[node].minVal = Math.min(tree[2 * node + 1].minVal, tree[2 * node + 2].minVal);
        tree[node].maxVal = Math.max(tree[2 * node + 1].maxVal, tree[2 * node + 2].maxVal);
    }

    private void build(long[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = new Node(arr[start]);
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            merge(node);
        }
    }

    private void updateAdd(int node, int start, int end, int l, int r, long val) {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            applyAdd(node, val);
            return;
        }
        push(node, start, end);
        int mid = (start + end) / 2;
        updateAdd(2 * node + 1, start, mid, l, r, val);
        updateAdd(2 * node + 2, mid + 1, end, l, r, val);
        merge(node);
    }

    private void updateFlip(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            applyFlip(node);
            return;
        }
        push(node, start, end);
        int mid = (start + end) / 2;
        updateFlip(2 * node + 1, start, mid, l, r);
        updateFlip(2 * node + 2, mid + 1, end, l, r);
        merge(node);
    }

    private long query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return Long.MAX_VALUE;
        if (l <= start && end <= r) return tree[node].minVal;
        
        push(node, start, end);
        int mid = (start + end) / 2;
        return Math.min(query(2 * node + 1, start, mid, l, r),
                        query(2 * node + 2, mid + 1, end, l, r));
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
                if (type.equals("ADD")) {
                    ops.add(new String[]{type, sc.next(), sc.next(), sc.next()});
                } else if (type.equals("FLIP")) {
                    ops.add(new String[]{type, sc.next(), sc.next()});
                } else {
                    ops.add(new String[]{type, sc.next(), sc.next()});
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
