#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <unordered_map>
#include <algorithm>
#include <queue>

using namespace std;

struct NodeInfo {
    int val;
    int weight;
    int depth;
};

class Solution {
public:
    vector<vector<int>> verticalOrderWithWeights(int n, const vector<int>& values,
                                                 const vector<int>& weights, const vector<int>& left,
                                                 const vector<int>& right, int W) {
        if (n == 0) return {};

        vector<bool> hasParent(n, false);
        for (int i = 0; i < n; i++) {
            if (left[i] != -1) hasParent[left[i]] = true;
            if (right[i] != -1) hasParent[right[i]] = true;
        }
        int root = 0;
        for (int i = 0; i < n; i++) {
            if (!hasParent[i]) {
                root = i;
                break;
            }
        }

        unordered_map<int, vector<NodeInfo>> cols;
        queue<pair<int, pair<int, int>>> q;
        vector<bool> visited(n, false);
        q.push({root, {0, 0}});
        visited[root] = true;

        int minCol = 0;
        int maxCol = 0;

        while (!q.empty()) {
            auto curr = q.front();
            q.pop();
            int u = curr.first;
            int c = curr.second.first;
            int d = curr.second.second;

            cols[c].push_back({values[u], weights[u], d});
            minCol = min(minCol, c);
            maxCol = max(maxCol, c);

            if (left[u] != -1 && !visited[left[u]]) {
                visited[left[u]] = true;
                q.push({left[u], {c - 1, d + 1}});
            }
            if (right[u] != -1 && !visited[right[u]]) {
                visited[right[u]] = true;
                q.push({right[u], {c + 1, d + 1}});
            }
        }

        vector<vector<int>> result;
        for (int c = minCol; c <= maxCol; c++) {
            auto it = cols.find(c);
            if (it == cols.end()) continue;
            auto& list = it->second;
            long long totalWeight = 0;
            for (const auto& node : list) totalWeight += node.weight;
            if (totalWeight >= W) {
                sort(list.begin(), list.end(), [](const NodeInfo& a, const NodeInfo& b) {
                    if (a.depth != b.depth) return a.depth < b.depth;
                    if (a.weight != b.weight) return a.weight > b.weight;
                    return a.val < b.val;
                });
                vector<int> colValues;
                for (const auto& node : list) colValues.push_back(node.val);
                result.push_back(colValues);
            }
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<string> lines;
    string line;
    while (getline(cin, line)) {
        if (!line.empty()) {
            bool allSpace = true;
            for (char ch : line) {
                if (ch > ' ') {
                    allSpace = false;
                    break;
                }
            }
            if (!allSpace) lines.push_back(line);
        }
    }
    if (lines.empty()) return 0;

    int n = stoi(lines[0]);
    vector<int> values(n, 0), weights(n, 1), left(n, -1), right(n, -1);

    for (int i = 0; i < n && i + 1 < (int)lines.size(); i++) {
        stringstream ss(lines[i + 1]);
        vector<long long> parts;
        long long x;
        while (ss >> x) parts.push_back(x);
        if (parts.size() < 3) continue;
        values[i] = (int)parts[0];
        if (parts.size() >= 4) {
            weights[i] = (int)parts[1];
            left[i] = (int)parts[2];
            right[i] = (int)parts[3];
        } else {
            weights[i] = 1;
            left[i] = (int)parts[1];
            right[i] = (int)parts[2];
        }
    }

    int W = 0;
    if ((int)lines.size() > n + 1) {
        W = stoi(lines[n + 1]);
    }

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
