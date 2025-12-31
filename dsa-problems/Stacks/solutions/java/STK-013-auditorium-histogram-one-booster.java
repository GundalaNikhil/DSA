import java.util.*;

class Solution {
    int[] tree;
    int n;

    void build(int[] h, int node, int start, int end) {
        if (start == end) {
            tree[node] = h[start];
        } else {
            int mid = (start + end) / 2;
            build(h, 2 * node, start, mid);
            build(h, 2 * node + 1, mid + 1, end);
            tree[node] = Math.min(tree[2 * node], tree[2 * node + 1]);
        }
    }

    // Find last index in [start, end] with value < val
    // Search from right to left (descent)
    int findLastLess(int node, int start, int end, int l, int r, long val) {
        if (l > r || tree[node] >= val) return -1;
        if (start == end) return start;
        
        int mid = (start + end) / 2;
        // Try right child first
        int res = -1;
        if (mid < r) res = findLastLess(2 * node + 1, mid + 1, end, l, r, val);
        if (res != -1) return res;
        // Try left child
        if (l <= mid) return findLastLess(2 * node, start, mid, l, r, val);
        return -1;
    }

    // Find first index in [start, end] with value < val
    // Search from left to right
    int findFirstLess(int node, int start, int end, int l, int r, long val) {
        if (l > r || tree[node] >= val) return -1;
        if (start == end) return start;
        
        int mid = (start + end) / 2;
        // Try left child first
        int res = -1;
        if (l <= mid) res = findFirstLess(2 * node, start, mid, l, r, val);
        if (res != -1) return res;
        // Try right child
        if (mid < r) return findFirstLess(2 * node + 1, mid + 1, end, l, r, val);
        return -1;
    }

    public long maxAreaWithBoost(int[] h, long b) {
        n = h.length;
        tree = new int[4 * n];
        build(h, 1, 0, n - 1);
        
        long maxArea = 0;
        
        for (int i = 0; i < n; i++) {
            // Case 1: Height determined by boosted bar i
            long boostedH = h[i] + b;
            int L = findLastLess(1, 0, n - 1, 0, i - 1, boostedH);
            int R = findFirstLess(1, 0, n - 1, i + 1, n - 1, boostedH);
            if (R == -1) R = n;
            maxArea = Math.max(maxArea, boostedH * (R - L - 1));
            
            // Case 2: Height determined by unboosted bar i
            long normalH = h[i];
            int L1 = findLastLess(1, 0, n - 1, 0, i - 1, normalH);
            int R1 = findFirstLess(1, 0, n - 1, i + 1, n - 1, normalH);
            if (R1 == -1) R1 = n;
            
            // Base area
            maxArea = Math.max(maxArea, normalH * (R1 - L1 - 1));
            
            // Extend Left
            if (L1 != -1 && h[L1] + b >= normalH) {
                int L2 = findLastLess(1, 0, n - 1, 0, L1 - 1, normalH);
                maxArea = Math.max(maxArea, normalH * (R1 - L2 - 1));
            }
            
            // Extend Right
            if (R1 != n && h[R1] + b >= normalH) {
                int R2 = findFirstLess(1, 0, n - 1, R1 + 1, n - 1, normalH);
                if (R2 == -1) R2 = n;
                maxArea = Math.max(maxArea, normalH * (R2 - L1 - 1));
            }
        }
        
        return maxArea;
    }
}
