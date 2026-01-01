#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    pair<int, int> checkFeasibility(int n, vector<pair<int,int>>& edges) {
        vector<int> indegree(n, 0);
        vector<vector<int>> adj(n);

        // Build graph
        for (auto& [u, v] : edges) {
            adj[u].push_back(v);
            indegree[v]++;
        }

        // Sort adjacency lists for deterministic behavior
        for (int i = 0; i < n; i++) {
            sort(adj[i].begin(), adj[i].end());
        }

        // Count nodes with indegree 0
        int initialZeros = 0;
        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                q.push(i);
                initialZeros++;
            }
        }

        int processed = 0;

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            processed++;

            for (int v : adj[u]) {
                indegree[v]--;
                if (indegree[v] == 0) {
                    q.push(v);
                }
            }
        }

        if (processed == n) {
            return {1, initialZeros};
        } else {
            return {-1, -1};
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<pair<int,int>> edges;
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        edges.push_back({u, v});
    }

    Solution solution;
    auto [result, zeros] = solution.checkFeasibility(n, edges);

    if (result == -1) {
        cout << -1 << endl;
    } else {
        cout << result << " " << zeros << endl;
    }

    return 0;
}
