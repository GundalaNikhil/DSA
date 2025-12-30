#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

struct Pair {
    long long val;
    int idx;
    
    bool operator<(const Pair& other) const {
        if (val != other.val) return val < other.val;
        return idx < other.idx;
    }
};

class Solution {
    vector<Pair> tree;
    int n;

    Pair merge(const Pair& p1, const Pair& p2) {
        if (p1.val < p2.val) return p1;
        if (p2.val < p1.val) return p2;
        return p1.idx < p2.idx ? p1 : p2;
    }

    void build(const vector<long long>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = {arr[start], start};
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    void update(int node, int start, int end, int idx, long long val) {
        if (start == end) {
            tree[node] = {val, idx};
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    Pair query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return {LLONG_MAX, -1};
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        Pair p1 = query(2 * node + 1, start, mid, l, r);
        Pair p2 = query(2 * node + 2, mid + 1, end, l, r);
        return merge(p1, p2);
    }

public:
    vector<int> process(const vector<long long>& inputArr, const vector<vector<string>>& ops) {
        n = inputArr.size();
        tree.assign(4 * n, {LLONG_MAX, -1});
        
        build(inputArr, 0, 0, n - 1);
        
        vector<int> results;
        for (const auto& op : ops) {
            if (op[0] == "SET") {
                int idx = stoi(op[1]);
                long long val = stoll(op[2]);
                update(0, 0, n - 1, idx, val);
            } else {
                int l = stoi(op[1]);
                int r = stoi(op[2]);
                Pair res = query(0, 0, n - 1, l, r);
                results.push_back(res.idx);
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
        string a, b;
        cin >> a >> b;
        ops[i] = {type, a, b};
    }
    Solution sol;
    vector<int> results = sol.process(arr, ops);
    for (int res : results) {
        cout << res << "\n";
    }
    return 0;
}
