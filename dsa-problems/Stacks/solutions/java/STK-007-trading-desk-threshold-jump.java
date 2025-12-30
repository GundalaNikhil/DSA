import java.util.*;

class Solution {
    int[] tree;
    int size;

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val; // We process R-to-L, so new val (index i) is always smaller/better
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

    public int[] thresholdJump(int[] prices, int t) {
        int n = prices.length;
        TreeSet<Integer> sortedValues = new TreeSet<>();
        for (int p : prices) {
            sortedValues.add(p);
            // We don't strictly need p+t in compression if we use lower_bound logic on just p values
            // But adding p+t makes it easier to map exactly.
        }
        
        // Map values to ranks 0..m-1
        List<Integer> distinct = new ArrayList<>(sortedValues);
        Map<Integer, Integer> rankMap = new HashMap<>();
        for (int i = 0; i < distinct.size(); i++) {
            rankMap.put(distinct.get(i), i);
        }
        
        size = distinct.size();
        tree = new int[4 * size];
        Arrays.fill(tree, Integer.MAX_VALUE);
        
        int[] result = new int[n];
        
        for (int i = n - 1; i >= 0; i--) {
            int target = prices[i] + t;
            // Find rank of smallest value >= target
            int r = Collections.binarySearch(distinct, target);
            if (r < 0) r = -r - 1; // Insertion point
            
            if (r < size) {
                int nearestIdx = query(1, 0, size - 1, r, size - 1);
                if (nearestIdx != Integer.MAX_VALUE) {
                    result[i] = nearestIdx - i;
                } else {
                    result[i] = 0;
                }
            } else {
                result[i] = 0;
            }
            
            update(1, 0, size - 1, rankMap.get(prices[i]), i);
        }
        
        return result;
    }
}
