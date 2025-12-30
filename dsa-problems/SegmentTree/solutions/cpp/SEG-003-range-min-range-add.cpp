#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
    vector<long long> tree;
    vector<long long> lazy;
    int n;

    void build(const vector<long long>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = min(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    void push(int node) {
        if (lazy[node] != 0) {
            tree[2 * node + 1] += lazy[node];
            lazy[2 * node + 1] += lazy[node];
            
            tree[2 * node + 2] += lazy[node];
            lazy[2 * node + 2] += lazy[node];
            
            lazy[node] = 0;
        }
    }

    void update(int node, int start, int end, int l, int r, long long val) {
        if (l > end || r < start) return;

        if (l <= start && end <= r) {
            tree[node] += val;
            lazy[node] += val;
            return;
        }

        push(node);
        int mid = (start + end) / 2;
        update(2 * node + 1, start, mid, l, r, val);
        update(2 * node + 2, mid + 1, end, l, r, val);
        tree[node] = min(tree[2 * node + 1], tree[2 * node + 2]);
    }

    long long query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return LLONG_MAX;

        if (l <= start && end <= r) {
            return tree[node];
        }

        push(node);
        int mid = (start + end) / 2;
        return min(query(2 * node + 1, start, mid, l, r),
                   query(2 * node + 2, mid + 1, end, l, r));
    }

public:
    vector<long long> process(const vector<long long>& arr, const vector<vector<string>>& ops) {
        n = arr.size();
        tree.assign(4 * n, 0);
        lazy.assign(4 * n, 0);
        
        build(arr, 0, 0, n - 1);
        
        vector<long long> results;
        for (const auto& op : ops) {
            if (op[0] == "ADD") {
                int l = stoi(op[1]);
                int r = stoi(op[2]);
                long long x = stoll(op[3]);
                update(0, 0, n - 1, l, r, x);
            } else {
                int l = stoi(op[1]);
                int r = stoi(op[2]);
                results.push_back(query(0, 0, n - 1, l, r));
            }
        }
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<long long> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<vector<string>> ops(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type;
        if (type == "ADD") {
            string l, r, x;
            cin >> l >> r >> x;
            ops[i] = {type, l, r, x};
        } else {
            string l, r;
            cin >> l >> r;
            ops[i] = {type, l, r};
        }
    }
    Solution sol;
    vector<long long> results = sol.process(arr, ops);
    for (long long res : results) {
        cout << res << "\n";
    }
    return 0;
}
