import java.util.*;

class Solution {
    static class Basis {
        int[] b = new int[30];
        
        void insert(int x) {
            for (int i = 29; i >= 0; i--) {
                if (((x >> i) & 1) == 1) {
                    if (b[i] == 0) {
                        b[i] = x;
                        return;
                    }
                    x ^= b[i];
                }
            }
        }
        
        void merge(Basis other) {
            for (int i = 0; i < 30; i++) {
                if (other.b[i] != 0) {
                    insert(other.b[i]);
                }
            }
        }
        
        int maxXor() {
            int res = 0;
            for (int i = 29; i >= 0; i--) {
                if ((res ^ b[i]) > res) {
                    res ^= b[i];
                }
            }
            return res;
        }
    }
    
    private Basis[] tree;
    private int n;

    public List<Integer> process(int[] arr, List<String[]> ops) {
        n = arr.length;
        tree = new Basis[4 * n];
        for(int i=0; i<4*n; i++) tree[i] = new Basis();
        
        build(arr, 0, 0, n - 1);
        
        List<Integer> results = new ArrayList<>();
        
        for (String[] op : ops) {
            if (op[0].equals("SET")) {
                int idx = Integer.parseInt(op[1]);
                int val = Integer.parseInt(op[2]);
                update(0, 0, n - 1, idx, val);
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                Basis res = query(0, 0, n - 1, l, r);
                results.add(res.maxXor());
            }
        }
        return results;
    }

    private void build(int[] arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = new Basis();
            tree[node].insert(arr[start]);
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            
            tree[node] = new Basis();
            tree[node].merge(tree[2 * node + 1]);
            tree[node].merge(tree[2 * node + 2]);
        }
    }

    private void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = new Basis();
            tree[node].insert(val);
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            
            tree[node] = new Basis();
            tree[node].merge(tree[2 * node + 1]);
            tree[node].merge(tree[2 * node + 2]);
        }
    }

    private Basis query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return new Basis();
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        Basis p1 = query(2 * node + 1, start, mid, l, r);
        Basis p2 = query(2 * node + 2, mid + 1, end, l, r);
        
        Basis res = new Basis();
        res.merge(p1);
        res.merge(p2);
        return res;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int q = sc.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
            List<String[]> ops = new ArrayList<>();
            for (int i = 0; i < q; i++) {
                String type = sc.next();
                ops.add(new String[]{type, sc.next(), sc.next()});
            }
            Solution sol = new Solution();
            List<Integer> results = sol.process(arr, ops);
            for (int res : results) {
                System.out.println(res);
            }
        }
        sc.close();
    }
}
