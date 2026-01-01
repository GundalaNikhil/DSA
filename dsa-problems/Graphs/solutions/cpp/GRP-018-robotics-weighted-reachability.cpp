#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int countReachable(int n, vector<tuple<int,int,int>>& edges, int threshold) {
        vector<vector<pair<int,int>>> adj(n);

        // Build adjacency list only with edges within threshold
        for (auto& [u, v, w] : edges) {
            if (w <= threshold) {
                adj[u].push_back({v, w});
                adj[v].push_back({u, w});
            }
        }

        // BFS from node 0
        unordered_set<int> visited;
        queue<int> q;

        q.push(0);
        visited.insert(0);

        while (!q.empty()) {
            int node = q.front();
            q.pop();

            // Sort neighbors for deterministic traversal
            sort(adj[node].begin(), adj[node].end());

            for (auto& [neighbor, weight] : adj[node]) {
                if (visited.find(neighbor) == visited.end()) {
                    visited.insert(neighbor);
                    q.push(neighbor);
                }
            }
        }

        return visited.size();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, threshold, m;
    cin >> n >> threshold >> m;

    vector<tuple<int,int,int>> edges;
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        edges.push_back({u, v, w});
    }

    Solution solution;
    cout << solution.countReachable(n, edges, threshold) << endl;

    return 0;
}
