#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Node {
    int maxLen;
    int prefLen;
    int suffLen;
    int len;
    int leftVal;
    int rightVal;
    
    Node() : maxLen(0), prefLen(0), suffLen(0), len(0), leftVal(0), rightVal(0) {}
    Node(int val) : maxLen(1), prefLen(1), suffLen(1), len(1), leftVal(val), rightVal(val) {}
};

class Solution {
    vector<Node> tree;
    int n;

    Node merge(const Node& left, const Node& right) {
        Node res;
        res.len = left.len + right.len;
        res.leftVal = left.leftVal;
        res.rightVal = right.rightVal;
        
        res.maxLen = max(left.maxLen, right.maxLen);
        res.prefLen = left.prefLen;
        res.suffLen = right.suffLen;
        
        if (left.rightVal < right.leftVal) {
            res.maxLen = max(res.maxLen, left.suffLen + right.prefLen);
            if (left.prefLen == left.len) {
                res.prefLen = left.len + right.prefLen;
            }
            if (right.suffLen == right.len) {
                res.suffLen = right.len + left.suffLen;
            }
        }
        return res;
    }

    void build(const vector<int>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = Node(arr[start]);
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = Node(val);
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

public:
    vector<int> process(const vector<int>& inputArr, const vector<pair<int,int>>& updates) {
        n = inputArr.size();
        tree.resize(4 * n);
        
        build(inputArr, 0, 0, n - 1);
        
        vector<int> results;
        results.reserve(updates.size());
        for (const auto& up : updates) {
            update(0, 0, n - 1, up.first, up.second);
            results.push_back(tree[0].maxLen);
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
    vector<pair<int, int>> updates(q);
    for (int i = 0; i < q; i++) {
        string type;
        cin >> type; // SET
        cin >> updates[i].first >> updates[i].second;
    }
    Solution sol;
    vector<int> results = sol.process(arr, updates);
    for (int res : results) {
        cout << res << "\n";
    }
    return 0;
}
