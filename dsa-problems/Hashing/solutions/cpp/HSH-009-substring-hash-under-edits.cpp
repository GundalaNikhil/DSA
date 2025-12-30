#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 313;
    
    vector<long long> tree;
    vector<long long> power;
    string chars;
    int n;

public:
    vector<long long> processOperations(string s, vector<vector<string>>& operations) {
        n = s.length();
        chars = s;
        tree.resize(4 * n);
        power.resize(n + 1);
        
        power[0] = 1;
        for (int i = 1; i <= n; i++) {
            power[i] = (power[i - 1] * BASE) % MOD;
        }
        
        build(1, 0, n - 1);
        
        vector<long long> results;
        for (const auto& op : operations) {
            if (op[0] == "U") {
                int idx = stoi(op[1]);
                char c = op[2][0];
                update(1, 0, n - 1, idx, c);
            } else {
                int l = stoi(op[1]);
                int r = stoi(op[2]);
                results.push_back(query(1, 0, n - 1, l, r));
            }
        }
        return results;
    }
    
    void build(int node, int start, int end) {
        if (start == end) {
            tree[node] = chars[start];
            return;
        }
        int mid = (start + end) / 2;
        build(2 * node, start, mid);
        build(2 * node + 1, mid + 1, end);
        
        int rightLen = end - mid;
        tree[node] = (tree[2 * node] * power[rightLen] + tree[2 * node + 1]) % MOD;
    }
    
    void update(int node, int start, int end, int idx, char val) {
        if (start == end) {
            chars[idx] = val;
            tree[node] = val;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) update(2 * node, start, mid, idx, val);
        else update(2 * node + 1, mid + 1, end, idx, val);
        
        int rightLen = end - mid;
        tree[node] = (tree[2 * node] * power[rightLen] + tree[2 * node + 1]) % MOD;
    }
    
    long long query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return -1;
        if (l <= start && end <= r) return tree[node];
        
        int mid = (start + end) / 2;
        long long p1 = query(2 * node, start, mid, l, r);
        long long p2 = query(2 * node + 1, mid + 1, end, l, r);
        
        if (p1 == -1) return p2;
        if (p2 == -1) return p1;
        
        int rightStart = max(mid + 1, l);
        int rightEnd = min(end, r);
        int rightLen = rightEnd - rightStart + 1;
        
        return (p1 * power[rightLen] + p2) % MOD;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    if (!(cin >> s)) return 0;
    
    int q;
    if (!(cin >> q)) return 0;
    
    vector<vector<string>> operations(q);
    for (int i = 0; i < q; i++) {
        char type;
        cin >> type;
        if (type == 'U') {
            int idx;
            char c;
            cin >> idx >> c;
            operations[i] = {"U", to_string(idx), string(1, c)};
        } else {
            int l, r;
            cin >> l >> r;
            operations[i] = {"Q", to_string(l), to_string(r)};
        }
    }
    
    Solution solution;
    vector<long long> result = solution.processOperations(s, operations);
    
    for (long long hash : result) {
        cout << hash << "\n";
    }
    
    return 0;
}
