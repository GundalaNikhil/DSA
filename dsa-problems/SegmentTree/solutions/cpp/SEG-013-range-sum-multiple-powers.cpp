#include <vector>
#include <string>
#include <iostream>

using namespace std;

struct Node {
    long long sum1, sum2, sum3;
    
    Node() : sum1(0), sum2(0), sum3(0) {}
    Node(long long val) {
        long long MOD = 1000000007;
        long long v = val % MOD;
        if (v < 0) v += MOD;
        sum1 = v;
        sum2 = (v * v) % MOD;
        sum3 = (sum2 * v) % MOD;
    }
};

class Solution {
    vector<Node> tree;
    int n;
    const long long MOD = 1000000007;

    Node merge(const Node& left, const Node& right) {
        Node res;
        res.sum1 = (left.sum1 + right.sum1) % MOD;
        res.sum2 = (left.sum2 + right.sum2) % MOD;
        res.sum3 = (left.sum3 + right.sum3) % MOD;
        return res;
    }

    void build(const vector<long long>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = Node(arr[start]);
        } else {
            int mid = (start + end) / 2;
            build(arr, 2 * node + 1, start, mid);
            build(arr, 2 * node + 2, mid + 1, end);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    void update(int node, int start, int end, int idx, long long val) {
        if (start == end) {
            tree[node] = Node(val);
        } else {
            int mid = (start + end) / 2;
            if (idx <= mid) update(2 * node + 1, start, mid, idx, val);
            else update(2 * node + 2, mid + 1, end, idx, val);
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2]);
        }
    }

    Node query(int node, int start, int end, int l, int r) {
        if (l > end || r < start) return Node();
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        Node p1 = query(2 * node + 1, start, mid, l, r);
        Node p2 = query(2 * node + 2, mid + 1, end, l, r);
        return merge(p1, p2);
    }

public:
    vector<long long> process(const vector<long long>& inputArr, const vector<vector<string>>& ops) {
        n = inputArr.size();
        tree.assign(4 * n, Node());
        
        build(inputArr, 0, 0, n - 1);
        
        vector<long long> results;
        for (const auto& op : ops) {
            if (op[0] == "SET") {
                int idx = stoi(op[1]);
                long long val = stoll(op[2]);
                update(0, 0, n - 1, idx, val);
            } else {
                int l = stoi(op[1]);
                int r = stoi(op[2]);
                int p = stoi(op[3]);
                Node res = query(0, 0, n - 1, l, r);
                if (p == 1) results.push_back(res.sum1);
                else if (p == 2) results.push_back(res.sum2);
                else results.push_back(res.sum3);
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
        if (type == "SET") {
            string a, b;
            cin >> a >> b;
            ops[i] = {type, a, b};
        } else {
            string a, b, c;
            cin >> a >> b >> c;
            ops[i] = {type, a, b, c};
        }
    }
    Solution sol;
    vector<long long> results = sol.process(arr, ops);
    for (long long res : results) {
        cout << res << "\n";
    }
    return 0;
}
