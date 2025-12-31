#include <iostream>
#include <vector>
#include <map>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> bottomViewWithLimit(int n, const vector<int>& values,
                                    const vector<int>& left, const vector<int>& right, int D) {
        if (n == 0) return {};

        map<int, int> viewMap;
        queue<pair<int, pair<int, int>>> q; // u, {col, depth}
        q.push({0, {0, 0}});

        while (!q.empty()) {
            auto curr = q.front();
            q.pop();
            int u = curr.first;
            int c = curr.second.first;
            int d = curr.second.second;

            viewMap[c] = values[u];

            if (d < D) {
                if (left[u] != -1) q.push({left[u], {c - 1, d + 1}});
                if (right[u] != -1) q.push({right[u], {c + 1, d + 1}});
            }
        }

        vector<int> result;
        for (auto const& [col, val] : viewMap) {
            result.push_back(val);
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
    int D;
    cin >> D;

    Solution solution;
    vector<int> ans = solution.bottomViewWithLimit(n, values, left, right, D);
    for (int i = 0; i < (int)ans.size(); i++) {
        if (i) cout << ' ';
        cout << ans[i];
    }
    return 0;
}
