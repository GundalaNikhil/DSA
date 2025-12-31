#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
    int maxDepth = -1;
    void dfs(int u, int depth, const vector<int>& values, const vector<int>& left, const vector<int>& right, map<int, int>& view) {
        if (u == -1) return;

        maxDepth = max(maxDepth, depth);

        if (values[u] >= 0 && view.find(depth) == view.end()) {
            view[depth] = values[u];
        }

        dfs(right[u], depth + 1, values, left, right, view);
        dfs(left[u], depth + 1, values, left, right, view);
    }

public:
    vector<int> rightViewWithSkips(int n, const vector<int>& values,
                                   const vector<int>& left, const vector<int>& right) {
        if (n == 0) return {};

        map<int, int> view;
        maxDepth = -1;
        dfs(0, 0, values, left, right, view);

        vector<int> result;
        for (int d = 0; d <= maxDepth; d++) {
            if (view.count(d)) {
                result.push_back(view[d]);
            }
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> left[i] >> right[i];
    }

    Solution solution;
    vector<int> ans = solution.rightViewWithSkips(n, values, left, right);
    for (int i = 0; i < (int)ans.size(); i++) {
        if (i) cout << ' ';
        cout << ans[i];
    }
    return 0;
}
