import java.util.*;
import java.io.*;

class Solution {
    int[] tree;
    int m;

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) {
            update(2 * node, start, mid, idx, val);
        } else {
            update(2 * node + 1, mid + 1, end, idx, val);
        }
        tree[node] = Math.min(tree[2 * node], tree[2 * node + 1]);
    }

    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) {
            return Integer.MAX_VALUE;
        }
        if (l <= start && end <= r) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        return Math.min(query(2 * node, start, mid, l, r),
                        query(2 * node + 1, mid + 1, end, l, r));
    }

    public int[] thresholdJump(int[] prices, int t) {
        int n = prices.length;
        
        // Coordinate Compression
        Set<Integer> distinctSet = new TreeSet<>();
        for (int p : prices) distinctSet.add(p);
        List<Integer> distinct = new ArrayList<>(distinctSet);
        m = distinct.size();
        
        Map<Integer, Integer> rankMap = new HashMap<>();
        for (int i = 0; i < m; i++) rankMap.put(distinct.get(i), i);
        
        // Segment Tree (Min Index)
        tree = new int[4 * m];
        Arrays.fill(tree, Integer.MAX_VALUE);
        
        int[] result = new int[n];
        
        for (int i = n - 1; i >= 0; i--) {
            int target = prices[i] + t;
            
            // Find rank >= target using binary search on distinct list
            int r = Collections.binarySearch(distinct, target);
            if (r < 0) r = -r - 1; // Insertion point
            
            if (r < m) {
                int nearestIdx = query(1, 0, m - 1, r, m - 1);
                if (nearestIdx != Integer.MAX_VALUE) {
                    result[i] = nearestIdx - i;
                }
            }
            
            update(1, 0, m - 1, rankMap.get(prices[i]), i);
        }
        return result;
    }
}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // Read N
        String line = "";
        while ((line = br.readLine()) != null && line.trim().isEmpty()) {}
        if (line == null) return;
        int n = Integer.parseInt(line.trim());
        
        // Read Array
        List<Integer> list = new ArrayList<>();
        StringTokenizer st = new StringTokenizer("");
        
        while (list.size() < n) {
            while (!st.hasMoreTokens()) {
                String l = br.readLine();
                if (l == null) break;
                st = new StringTokenizer(l);
            }
            if (!st.hasMoreTokens()) break;
            list.add(Integer.parseInt(st.nextToken()));
        }
        
        int[] prices = new int[list.size()];
        for(int i=0; i<list.size(); i++) prices[i] = list.get(i);
        
        // Read T
        while (!st.hasMoreTokens()) {
            String l = br.readLine();
            if (l == null) break;
            st = new StringTokenizer(l);
        }
        int t = 0;
        if (st.hasMoreTokens()) {
            t = Integer.parseInt(st.nextToken());
        }
        
        Solution sol = new Solution();
        int[] res = sol.thresholdJump(prices, t);
        for (int val : res) {
            System.out.println(val);
        }
    }
}
