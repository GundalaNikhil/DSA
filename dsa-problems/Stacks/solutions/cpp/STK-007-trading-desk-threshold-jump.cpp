#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <climits>

using namespace std;

class Solution {
    vector<int> tree;
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
        tree[node] = min(tree[2 * node], tree[2 * node + 1]);
    }

    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) {
            return INT_MAX;
        }
        if (l <= start && end <= r) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        return min(query(2 * node, start, mid, l, r),
                   query(2 * node + 1, mid + 1, end, l, r));
    }

public:
    vector<int> thresholdJump(vector<int>& prices, int t) {
        int n = prices.size();
        
        // Coordinate Compression
        vector<int> distinct = prices;
        sort(distinct.begin(), distinct.end());
        distinct.erase(unique(distinct.begin(), distinct.end()), distinct.end());
        
        m = distinct.size();
        map<int, int> rankMap;
        for (int i = 0; i < m; i++) rankMap[distinct[i]] = i;
        
        tree.assign(4 * m, INT_MAX);
        vector<int> result(n, 0);
        
        for (int i = n - 1; i >= 0; i--) {
            long long target = (long long)prices[i] + t;
            
            // Find rank >= target
            auto it = lower_bound(distinct.begin(), distinct.end(), target);
            int r = distance(distinct.begin(), it);
            
            if (r < m) {
                int nearestIdx = query(1, 0, m - 1, r, m - 1);
                if (nearestIdx != INT_MAX) {
                    result[i] = nearestIdx - i;
                }
            }
            
            update(1, 0, m - 1, rankMap[prices[i]], i);
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> prices(n);
    for (int i = 0; i < n; i++) {
        cin >> prices[i];
    }
    
    int t;
    cin >> t;
    
    Solution sol;
    vector<int> res = sol.thresholdJump(prices, t);
    
    for (int val : res) {
        cout << val << "\n";
    }
    
    return 0;
}
