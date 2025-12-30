#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    vector<vector<int>> tree;
    vector<long long> values;
    vector<int> subtreeSize;
    vector<long long> subtreeSum;

    void dfs(int node, int parent) {
        subtreeSize[node] = 1;
        subtreeSum[node] = values[node];

        for (int child : tree[node]) {
            if (child == parent) continue;

            dfs(child, node);
            subtreeSize[node] += subtreeSize[child];
            subtreeSum[node] += subtreeSum[child];
        }
    }

public:
    void computeSubtreeMetrics(int n, vector<long long>& nodeValues, vector<pair<int, int>>& edges) {
        tree.resize(n + 1);
        values.resize(n + 1);
        subtreeSize.resize(n + 1);
        subtreeSum.resize(n + 1);

        for (int i = 1; i <= n; i++) {
            values[i] = nodeValues[i - 1];
        }

        for (auto& edge : edges) {
            tree[edge.first].push_back(edge.second);
            tree[edge.second].push_back(edge.first);
        }

        dfs(1, -1);
    }

    vector<long long> getSubtreeSums() {
        return vector<long long>(subtreeSum.begin() + 1, subtreeSum.end());
    }
};

int main() {
    int n;
    cin >> n;

    vector<long long> values(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i];
    }

    vector<pair<int, int>> edges;
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        edges.push_back({u, v});
    }

    Solution solution;
    solution.computeSubtreeMetrics(n, values, edges);

    vector<long long> sums = solution.getSubtreeSums();
    for (long long s : sums) {
        cout << s << endl;
    }

    return 0;
}
