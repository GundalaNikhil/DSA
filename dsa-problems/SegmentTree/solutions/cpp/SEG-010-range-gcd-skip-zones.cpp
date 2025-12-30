#include <iostream>
#include <vector>
#include <numeric>
#include <string>
#include <algorithm>

using namespace std;

long long gcd(long long a, long long b) {
    a = abs(a); b = abs(b);
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

class Solution {
    vector<int> tree;
    vector<int> vals;
    vector<bool> active;
    int n;

    void build(int node, int start, int end) {
        if (start == end) {
            tree[node] = active[start] ? vals[start] : 0;
        } else {
            int mid = (start + end) / 2;
            build(2 * node + 1, start, mid);
            build(2 * node + 2, mid + 1, end);
            tree[node] = gcd(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val;
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            tree[node] = gcd(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    int query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return 0;
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        int p1 = query(2 * node + 1, start, mid, l, r);
        int p2 = query(2 * node + 2, mid + 1, end, l, r);
        return gcd(p1, p2);
    }

public:
    vector<int> process(const vector<int>& arr, const vector<bool>& forbidden, const vector<vector<string>>& ops) {
        n = arr.size();
        vals = arr;
        active.assign(n, false);
        for (int i = 0; i < n; i++) active[i] = !forbidden[i];
        
        tree.assign(4 * n, 0);
        build(0, 0, n - 1);
        
        vector<int> results;
        for (const auto& op : ops) {
            if (op[0] == "TOGGLE") {
                int idx = stoi(op[1]);
                active[idx] = !active[idx];
                int effVal = active[idx] ? abs(vals[idx]) : 0;
                update(0, 0, n - 1, idx, effVal);
            } else if (op[0] == "SET") {
                int idx = stoi(op[1]);
                int val = stoi(op[2]);
                vals[idx] = val;
                int effVal = active[idx] ? abs(vals[idx]) : 0;
                update(0, 0, n - 1, idx, effVal);
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
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int f;
    cin >> f;
    vector<bool> forbidden(n, false);
    for (int i = 0; i < f; i++) {
        int idx;
        cin >> idx;
        forbidden[idx] = true;
    }
    vector<vector<string>> ops(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type;
        if (type == "TOGGLE") {
            string idx;
            cin >> idx;
            ops[i] = {type, idx};
        } else {
            string a, b;
            cin >> a >> b;
            ops[i] = {type, a, b};
        }
    }
    Solution sol;
    vector<int> results = sol.process(arr, forbidden, ops);
    for (int res : results) {
        cout << res << "\n";
    }
    return 0;
}
