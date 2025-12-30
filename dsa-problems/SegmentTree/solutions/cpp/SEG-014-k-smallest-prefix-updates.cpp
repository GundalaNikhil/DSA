#include <vector>
#include <string>
#include <iostream>

using namespace std;

struct Node {
    long long sum;
    long long lazySet;
    bool hasLazy;
};

class Solution {
    vector<Node> tree;
    int n;

    void push(int node, int start, int end) {
        if (tree[node].hasLazy) {
            int mid = (start + end) / 2;
            long long val = tree[node].lazySet;
            
            tree[2 * node + 1].lazySet = val;
            tree[2 * node + 1].hasLazy = true;
            tree[2 * node + 1].sum = val * (mid - start + 1);
            
            tree[2 * node + 2].lazySet = val;
            tree[2 * node + 2].hasLazy = true;
            tree[2 * node + 2].sum = val * (end - mid);
            
            tree[node].hasLazy = false;
        }
    }

    void build(const vector<long long>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = {arr[start], 0, false};
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = {tree[2 * node + 1].sum + tree[2 * node + 2].sum, 0, false};
        }
    }

    void update(int node, int start, int end, int l, int r, long long val) {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            tree[node].lazySet = val;
            tree[node].hasLazy = true;
            tree[node].sum = val * (end - start + 1);
            return;
        }
        
        push(node, start, end);
        int mid = (start + end) / 2;
        update(2 * node + 1, start, mid, l, r, val);
        update(2 * node + 2, mid + 1, end, l, r, val);
        tree[node].sum = tree[2 * node + 1].sum + tree[2 * node + 2].sum;
    }

    long long query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return 0;
        if (l <= start && end <= r) return tree[node].sum;
        
        push(node, start, end);
        int mid = (start + end) / 2;
        return query(2 * node + 1, start, mid, l, r) + 
               query(2 * node + 2, mid + 1, end, l, r);
    }

public:
    vector<long long> process(const vector<long long>& arr, const vector<vector<string>>& ops) {
        n = arr.size();
        tree.assign(4 * n, {0, 0, false});
        
        build(arr, 0, 0, n - 1);
        
        vector<long long> results;
        for (const auto& op : ops) {
            if (op[0] == "SETPREFIX") {
                int k = stoi(op[1]);
                long long x = stoll(op[2]);
                if (k > 0) update(0, 0, n - 1, 0, k - 1, x);
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
        string type, a, b;
        cin >> type >> a >> b;
        ops[i] = {type, a, b};
    }
    Solution sol;
    vector<long long> results = sol.process(arr, ops);
    for (long long res : results) {
        cout << res << "\n";
    }
    return 0;
}
