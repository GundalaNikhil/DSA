#include <iostream>
#include <vector>
#include <algorithm>
#include <array>

using namespace std;

class Solution {
    int timer;
    vector<int> disc, low;
    vector<int> criticalIndices;
    vector<vector<array<int, 3>>> adj; // {v, cap, idx}

    void dfs(int u, int parentEdgeIdx, int T) {
        disc[u] = low[u] = ++timer;

        for (auto& edge : adj[u]) {
            int v = edge[0];
            int cap = edge[1];
            int idx = edge[2];

            if (idx == parentEdgeIdx) continue;

            if (disc[v] != -1) {
                low[u] = min(low[u], disc[v]);
            } else {
                dfs(v, idx, T);
                low[u] = min(low[u], low[v]);

                if (low[v] > disc[u]) {
                    if (cap < T) {
                        criticalIndices.push_back(idx);
                    }
                }
            }
        }
    }

public:
    vector<pair<int, int>> criticalEdges(int n, const vector<array<int, 3>>& edges, int T) {
        adj.assign(n, vector<array<int, 3>>());
        for (int i = 0; i < edges.size(); i++) {
            adj[edges[i][0]].push_back({edges[i][1], edges[i][2], i});
            adj[edges[i][1]].push_back({edges[i][0], edges[i][2], i});
        }

        disc.assign(n, -1);
        low.assign(n, -1);
        criticalIndices.clear();
        timer = 0;

        for (int i = 0; i < n; i++) {
            if (disc[i] == -1) {
                dfs(i, -1, T);
            }
        }

        sort(criticalIndices.begin(), criticalIndices.end());

        vector<pair<int, int>> result;
        for (int idx : criticalIndices) {
            result.push_back({edges[idx][0], edges[idx][1]});
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, T;
    if (!(cin >> n >> m >> T)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    vector<pair<int, int>> ans = solution.criticalEdges(n, edges, T);
    cout << ans.size() << "\n";
    for (auto& e : ans) {
        cout << e.first << ' ' << e.second << "\n";
    }
    return 0;
}
