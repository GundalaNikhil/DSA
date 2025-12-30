#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
private:
    vector<vector<int>> tree;
    int diameter;

    int dfs(int node, int parent) {
        int max1 = 0, max2 = 0;

        for (int child : tree[node]) {
            if (child == parent) continue;

            int childDepth = dfs(child, node);

            if (childDepth > max1) {
                max2 = max1;
                max1 = childDepth;
            } else if (childDepth > max2) {
                max2 = childDepth;
            }
        }

        diameter = max(diameter, max1 + max2);
        return max1 + 1;
    }

public:
    int treeDiameter(int n, vector<pair<int, int>>& edges) {
        tree.resize(n + 1);
        diameter = 0;

        for (auto& edge : edges) {
            tree[edge.first].push_back(edge.second);
            tree[edge.second].push_back(edge.first);
        }

        dfs(1, -1);
        return diameter;
    }
};

int main() {
    int n;
    cin >> n;

    vector<pair<int, int>> edges;
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        edges.push_back({u, v});
    }

    Solution solution;
    int result = solution.treeDiameter(n, edges);

    cout << result << endl;

    return 0;
}
