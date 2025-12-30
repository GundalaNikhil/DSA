#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    int dfs(int u, const vector<int>& left, const vector<int>& right) {
        if (u == -1) return -1;
        int lHeight = dfs(left[u], left, right);
        int rHeight = dfs(right[u], left, right);
        return 1 + max(lHeight, rHeight);
    }

public:
    int treeHeight(int n, const vector<int>& left, const vector<int>& right) {
        if (n == 0) return -1;
        return dfs(0, left, right);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    if (n == 0) {
        cout << "-1\n";
        return 0;
    }

    vector<int> left(n), right(n);
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val >> left[i] >> right[i];
    }

    Solution solution;
    cout << solution.treeHeight(n, left, right) << "\n";
    return 0;
}
