#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

struct NodeInfo {
    int val, weight, depth;
};

class Solution {
public:
    vector<vector<int>> verticalOrderWithWeights(int n, const vector<int>& values,
                                                 const vector<int>& weights, const vector<int>& left,
                                                 const vector<int>& right, long long W) {
        if (n == 0) return {};

        map<int, vector<NodeInfo>> cols;
        queue<pair<int, pair<int, int>>> q; // u, {col, depth}
        q.push({0, {0, 0}});

        while (!q.empty()) {
            auto curr = q.front();
            q.pop();
            int u = curr.first;
            int c = curr.second.first;
            int d = curr.second.second;

            cols[c].push_back({values[u], weights[u], d});

            if (left[u] != -1) q.push({left[u], {c - 1, d + 1}});
            if (right[u] != -1) q.push({right[u], {c + 1, d + 1}});
        }

        vector<vector<int>> result;
        for (auto& entry : cols) {
            long long totalWeight = 0;
            for (const auto& node : entry.second) totalWeight += node.weight;

            if (totalWeight >= W) {
                sort(entry.second.begin(), entry.second.end(), [](const NodeInfo& a, const NodeInfo& b) {
                    if (a.depth != b.depth) return a.depth < b.depth;
                    if (a.weight != b.weight) return a.weight > b.weight; // Descending
                    return a.val < b.val;
                });

                vector<int> colValues;
                for (const auto& node : entry.second) colValues.push_back(node.val);
                result.push_back(colValues);
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
    vector<int> values(n), weights(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> weights[i] >> left[i] >> right[i];
    }
    long long W;
    cin >> W;

    Solution solution;
    vector<vector<int>> cols = solution.verticalOrderWithWeights(n, values, weights, left, right, W);
    if (cols.empty()) {
        cout << "\n";
    } else {
        for (int i = 0; i < (int)cols.size(); i++) {
            for (int j = 0; j < (int)cols[i].size(); j++) {
                if (j) cout << ' ';
                cout << cols[i][j];
            }
            if (i + 1 < (int)cols.size()) cout << "\n";
        }
    }
    return 0;
}
