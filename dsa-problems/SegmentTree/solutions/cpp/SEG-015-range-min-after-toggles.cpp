#include <vector>
#include <string>
#include <algorithm>
#include <climits>
#include <iostream>

using namespace std;

struct Node {
    long long minVal, maxVal;
    long long lazyAdd;
    bool lazyFlip;
};

class Solution {
    vector<Node> tree;
    int n;

    void applyFlip(int node) {
        long long temp = tree[node].minVal;
        tree[node].minVal = -tree[node].maxVal;
        tree[node].maxVal = -temp;
        tree[node].lazyAdd = -tree[node].lazyAdd;
        tree[node].lazyFlip = !tree[node].lazyFlip;
    }

    void applyAdd(int node, long long val) {
        tree[node].minVal += val;
        tree[node].maxVal += val;
        tree[node].lazyAdd += val;
    }

    void push(int node, int start, int end) {
        if (tree[node].lazyFlip) {
            applyFlip(2 * node + 1);
            applyFlip(2 * node + 2);
            tree[node].lazyFlip = false;
        }
        if (tree[node].lazyAdd != 0) {
            applyAdd(2 * node + 1, tree[node].lazyAdd);
            applyAdd(2 * node + 2, tree[node].lazyAdd);
            tree[node].lazyAdd = 0;
        }
    }

    void merge(int node) {
        tree[node].minVal = min(tree[2 * node + 1].minVal, tree[2 * node + 2].minVal);
        tree[node].maxVal = max(tree[2 * node + 1].maxVal, tree[2 * node + 2].maxVal);
    }

    void build(const vector<long long>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = {arr[start], arr[start], 0, false};
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            merge(node);
            tree[node].lazyAdd = 0;
            tree[node].lazyFlip = false;
        }
    }

    void updateAdd(int node, int start, int end, int l, int r, long long val) {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            applyAdd(node, val);
            return;
        }
        push(node, start, end);
        int mid = (start + end) / 2;
        updateAdd(2 * node + 1, start, mid, l, r, val);
        updateAdd(2 * node + 2, mid + 1, end, l, r, val);
        merge(node);
    }

    void updateFlip(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            applyFlip(node);
            return;
        }
        push(node, start, end);
        int mid = (start + end) / 2;
        updateFlip(2 * node + 1, start, mid, l, r);
        updateFlip(2 * node + 2, mid + 1, end, l, r);
        merge(node);
    }

    long long query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return LLONG_MAX;
        if (l <= start && end <= r) return tree[node].minVal;
        
        push(node, start, end);
        int mid = (start + end) / 2;
        return min(query(2 * node + 1, start, mid, l, r),
                   query(2 * node + 2, mid + 1, end, l, r));
    }

public:
    vector<long long> process(const vector<long long>& inputArr, const vector<vector<string>>& ops) {
        n = inputArr.size();
        tree.assign(4 * n, {0, 0, 0, false});
        
        build(inputArr, 0, 0, n - 1);
        
        vector<long long> results;
        for (const auto& op : ops) {
            if (op[0] == "ADD") {
                updateAdd(0, 0, n - 1, stoi(op[1]), stoi(op[2]), stoll(op[3]));
            } else if (op[0] == "FLIP") {
                updateFlip(0, 0, n - 1, stoi(op[1]), stoi(op[2]));
            } else {
                results.push_back(query(0, 0, n - 1, stoi(op[1]), stoi(op[2])));
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
            string a, b, c;
            cin >> a >> b >> c;
            ops[i] = {type, a, b, c};
        } else {
            string a, b;
            cin >> a >> b;
            ops[i] = {type, a, b};
        }
    }
    Solution sol;
    vector<long long> results = sol.process(arr, ops);
    for (long long res : results) {
        cout << res << "\n";
    }
    return 0;
}
