#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct Basis {
    int b[30] = {0};
    
    void insert(int x) {
        for (int i = 29; i >= 0; i--) {
            if ((x >> i) & 1) {
                if (!b[i]) {
                    b[i] = x;
                    return;
                }
                x ^= b[i];
            }
        }
    }
    
    void merge(const Basis& other) {
        for (int i = 0; i < 30; i++) {
            if (other.b[i]) insert(other.b[i]);
        }
    }
    
    int maxXor() {
        int res = 0;
        for (int i = 29; i >= 0; i--) {
            if ((res ^ b[i]) > res) res ^= b[i];
        }
        return res;
    }
};

class Solution {
    vector<Basis> tree;
    int n;

    void build(const vector<int>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node].insert(arr[start]);
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            
            tree[node] = tree[2 * node + 1];
            tree[node].merge(tree[2 * node + 2]);
        }
    }

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = Basis();
            tree[node].insert(val);
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            
            tree[node] = tree[2 * node + 1];
            tree[node].merge(tree[2 * node + 2]);
        }
    }

    Basis query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return Basis();
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        Basis p1 = query(2 * node + 1, start, mid, l, r);
        Basis p2 = query(2 * node + 2, mid + 1, end, l, r);
        
        p1.merge(p2);
        return p1;
    }

public:
    vector<int> process(const vector<int>& arr, const vector<vector<string>>& ops) {
        n = arr.size();
        tree.assign(4 * n, Basis());
        
        build(arr, 0, 0, n - 1);
        
        vector<int> results;
        for (const auto& op : ops) {
            if (op[0] == "SET") {
                int idx = stoi(op[1]);
                int val = stoi(op[2]);
                update(0, 0, n - 1, idx, val);
            } else {
                int l = stoi(op[1]);
                int r = stoi(op[2]);
                Basis res = query(0, 0, n - 1, l, r);
                results.push_back(res.maxXor());
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
    vector<vector<string>> ops(q);
    for (int i = 0; i < q; i++) {
        string type, a, b;
        cin >> type >> a >> b;
        ops[i] = {type, a, b};
    }
    Solution sol;
    vector<int> results = sol.process(arr, ops);
    for (int res : results) {
        cout << res << "\n";
    }
    return 0;
}
