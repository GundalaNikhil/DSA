import java.util.*;

class Solution {
    private static final long MOD = 1_000_000_007L;
    private static final long BASE = 313L;
    
    private long[] tree;
    private long[] power;
    private int n;
    private char[] chars;
    
    public List<Long> processOperations(String s, List<String[]> operations) {
        n = s.length();
        chars = s.toCharArray();
        tree = new long[4 * n];
        power = new long[n + 1];
        
        power[0] = 1;
        for (int i = 1; i <= n; i++) {
            power[i] = (power[i - 1] * BASE) % MOD;
        }
        
        build(1, 0, n - 1);
        
        List<Long> results = new ArrayList<>();
        
        for (String[] op : operations) {
            String type = op[0];
            if (type.equals("U")) {
                int idx = Integer.parseInt(op[1]);
                char c = op[2].charAt(0);
                update(1, 0, n - 1, idx, c);
            } else {
                int l = Integer.parseInt(op[1]);
                int r = Integer.parseInt(op[2]);
                // Query returns {hash, length}
                // But since we query range [l, r], length is always r-l+1.
                // Standard query logic:
                results.add(query(1, 0, n - 1, l, r));
            }
        }
        
        return results;
    }
    
    private void build(int node, int start, int end) {
        if (start == end) {
            tree[node] = chars[start];
            return;
        }
        int mid = (start + end) / 2;
        build(2 * node, start, mid);
        build(2 * node + 1, mid + 1, end);
        
        int rightLen = end - mid;
        tree[node] = (tree[2 * node] * power[rightLen] + tree[2 * node + 1]) % MOD;
    }
    
    private void update(int node, int start, int end, int idx, char val) {
        if (start == end) {
            chars[idx] = val;
            tree[node] = val;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) update(2 * node, start, mid, idx, val);
        else update(2 * node + 1, mid + 1, end, idx, val);
        
        int rightLen = end - mid;
        tree[node] = (tree[2 * node] * power[rightLen] + tree[2 * node + 1]) % MOD;
    }
    
    private long query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return -1; // Null
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        long p1 = query(2 * node, start, mid, l, r);
        long p2 = query(2 * node + 1, mid + 1, end, l, r);
        
        if (p1 == -1) return p2;
        if (p2 == -1) return p1;
        
        // We need length of the right part that was actually included in the query
        // Intersection of [mid+1, end] and [l, r]
        int rightStart = Math.max(mid + 1, l);
        int rightEnd = Math.min(end, r);
        int rightLen = rightEnd - rightStart + 1;
        
        return (p1 * power[rightLen] + p2) % MOD;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextLine()) {
            String s = sc.nextLine();
            if (sc.hasNextInt()) {
                int q = sc.nextInt();
                sc.nextLine();
                List<String[]> operations = new ArrayList<>();
                for (int i = 0; i < q; i++) {
                    operations.add(sc.nextLine().split(" "));
                }
                Solution solution = new Solution();
                List<Long> result = solution.processOperations(s, operations);
                for (long hash : result) {
                    System.out.println(hash);
                }
            }
        }
        sc.close();
    }
}
