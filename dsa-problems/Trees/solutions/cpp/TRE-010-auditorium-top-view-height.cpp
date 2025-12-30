#include <iostream>
#include <vector>
#include <map>
#include <queue>

using namespace std;

struct NodeInfo {
    int val;
    int depth;
};

class Solution {
public:
    vector<int> topView(int n, const vector<int>& values,
                        const vector<int>& left, const vector<int>& right) {
        if (n == 0) return {};

        map<int, NodeInfo> viewMap;
        queue<pair<int, pair<int, int>>> q; // u, {col, depth}
        q.push({0, {0, 0}});

        while (!q.empty()) {
            auto curr = q.front();
            q.pop();
            int u = curr.first;
            int c = curr.second.first;
            int d = curr.second.second;

            if (viewMap.find(c) == viewMap.end()) {
                viewMap[c] = {values[u], d};
            } else {
                if (d < viewMap[c].depth) {
                    viewMap[c] = {values[u], d};
                } else if (d == viewMap[c].depth) {
                    if (values[u] > viewMap[c].val) {
                        viewMap[c].val = values[u];
                    }
                }
            }

            if (left[u] != -1) q.push({left[u], {c - 1, d + 1}});
            if (right[u] != -1) q.push({right[u], {c + 1, d + 1}});
        }

        vector<int> result;
        for (auto const& [col, info] : viewMap) {
            result.push_back(info.val);
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
    vector<int> ans = solution.topView(n, values, left, right);
    for (int i = 0; i < (int)ans.size(); i++) {
        if (i) cout << ' ';
        cout << ans[i];
    }
    return 0;
}
