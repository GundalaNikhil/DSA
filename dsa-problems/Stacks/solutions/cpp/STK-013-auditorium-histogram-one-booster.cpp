#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
    vector<int> tree;
    int n;

    void build(const vector<int>& h, int node, int start, int end) {
        if (start == end) {
            tree[node] = h[start];
        } else {
            int mid = (start + end) / 2;
            build(h, 2 * node, start, mid);
            build(h, 2 * node + 1, mid + 1, end);
            tree[node] = min(tree[2 * node], tree[2 * node + 1]);
        }
    }

    int findLastLess(int node, int start, int end, int l, int r, long long val) {
        if (l > r || tree[node] >= val) return -1;
        if (start == end) return start;
        
        int mid = (start + end) / 2;
        int res = -1;
        if (mid < r) res = findLastLess(2 * node + 1, mid + 1, end, l, r, val);
        if (res != -1) return res;
        if (l <= mid) return findLastLess(2 * node, start, mid, l, r, val);
        return -1;
    }

    int findFirstLess(int node, int start, int end, int l, int r, long long val) {
        if (l > r || tree[node] >= val) return -1;
        if (start == end) return start;
        
        int mid = (start + end) / 2;
        int res = -1;
        if (l <= mid) res = findFirstLess(2 * node, start, mid, l, r, val);
        if (res != -1) return res;
        if (mid < r) return findFirstLess(2 * node + 1, mid + 1, end, l, r, val);
        return -1;
    }

public:
    long long maxAreaWithBoost(const vector<int>& h, long long b) {
        n = h.size();
        tree.assign(4 * n, 0);
        build(h, 1, 0, n - 1);
        
        long long maxArea = 0;
        
        for (int i = 0; i < n; i++) {
            long long boostedH = h[i] + b;
            int L = findLastLess(1, 0, n - 1, 0, i - 1, boostedH);
            int R = findFirstLess(1, 0, n - 1, i + 1, n - 1, boostedH);
            if (R == -1) R = n;
            maxArea = max(maxArea, boostedH * (R - L - 1));
            
            long long normalH = h[i];
            int L1 = findLastLess(1, 0, n - 1, 0, i - 1, normalH);
            int R1 = findFirstLess(1, 0, n - 1, i + 1, n - 1, normalH);
            if (R1 == -1) R1 = n;
            
            maxArea = max(maxArea, normalH * (R1 - L1 - 1));
            
            if (L1 != -1 && h[L1] + b >= normalH) {
                int L2 = findLastLess(1, 0, n - 1, 0, L1 - 1, normalH);
                maxArea = max(maxArea, normalH * (R1 - L2 - 1));
            }
            
            if (R1 != n && h[R1] + b >= normalH) {
                int R2 = findFirstLess(1, 0, n - 1, R1 + 1, n - 1, normalH);
                if (R2 == -1) R2 = n;
                maxArea = max(maxArea, normalH * (R2 - L1 - 1));
            }
        }
        
        return maxArea;
    }
};
