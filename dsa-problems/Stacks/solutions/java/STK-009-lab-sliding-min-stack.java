import java.util.*;

class Solution {
    int[] tree;
    int n = 100005; // Max operations
    int currentSize = 0;
    
    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) update(2 * node, start, mid, idx, val);
        else update(2 * node + 1, mid + 1, end, idx, val);
        tree[node] = Math.min(tree[2 * node], tree[2 * node + 1]);
    }
    
    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return Integer.MAX_VALUE;
        if (l <= start && end <= r) return tree[node];
        int mid = (start + end) / 2;
        return Math.min(query(2 * node, start, mid, l, r), query(2 * node + 1, mid + 1, end, l, r));
    }

    public List<String> process(List<String[]> ops) {
        List<String> result = new ArrayList<>();
        tree = new int[4 * n];
        Arrays.fill(tree, Integer.MAX_VALUE);
        currentSize = 0;
        
        for (String[] op : ops) {
            String cmd = op[0];
            if (cmd.equals("PUSH")) {
                int val = Integer.parseInt(op[1]);
                update(1, 0, n - 1, currentSize, val);
                currentSize++;
            } else if (cmd.equals("POP")) {
                if (currentSize == 0) {
                    result.add("EMPTY");
                } else {
                    // To output the popped value, we need to store it or query it.
                    // Querying point is O(log N). Storing in array is O(1).
                    // Let's query.
                    int val = query(1, 0, n - 1, currentSize - 1, currentSize - 1);
                    result.add(String.valueOf(val));
                    currentSize--;
                }
            } else if (cmd.equals("MIN")) {
                int k = Integer.parseInt(op[1]);
                if (currentSize < k) {
                    result.add("NA");
                } else {
                    int minVal = query(1, 0, n - 1, currentSize - k, currentSize - 1);
                    result.add(String.valueOf(minVal));
                }
            }
        }
        return result;
    }
}
