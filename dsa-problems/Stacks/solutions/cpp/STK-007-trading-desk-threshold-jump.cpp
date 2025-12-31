#include <vector>
#include <algorithm>
#include <map>

using namespace std;

class Solution {
    vector<int> tree;
    int size;

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) update(2 * node, start, mid, idx, val);
        else update(2 * node + 1, mid + 1, end, idx, val);
        tree[node] = min(tree[2 * node], tree[2 * node + 1]);
    }

    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return 2e9;
        if (l <= start && end <= r) return tree[node];
        int mid = (start + end) / 2;
        return min(query(2 * node, start, mid, l, r), query(2 * node + 1, mid + 1, end, l, r));
    }

public:
    vector<int> thresholdJump(const vector<int>& prices, int t) {
        int n = prices.size();
        vector<int> distinct = prices;
        sort(distinct.begin(), distinct.end());
        distinct.erase(unique(distinct.begin(), distinct.end()), distinct.end());
        
        size = distinct.size();
        tree.assign(4 * size, 2e9);
        
        vector<int> result(n, 0);
        
        for (int i = n - 1; i >= 0; i--) {
            long long target = (long long)prices[i] + t;
            auto it = lower_bound(distinct.begin(), distinct.end(), target);
            
            if (it != distinct.end()) {
                int r = distance(distinct.begin(), it);
                int nearestIdx = query(1, 0, size - 1, r, size - 1);
                if (nearestIdx != 2e9) {
                    result[i] = nearestIdx - i;
                }
            }
            
            int rank = lower_bound(distinct.begin(), distinct.end(), prices[i]) - distinct.begin();
            update(1, 0, size - 1, rank, i);
        }
        
        return result;
    }
};
