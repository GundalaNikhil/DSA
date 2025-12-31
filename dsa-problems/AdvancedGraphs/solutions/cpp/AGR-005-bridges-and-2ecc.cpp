#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    int timer;
    vector<int> tin, low;
    vector<int> bridgeFlags;
    vector<vector<pair<int, int>>> adj; // {neighbor, edgeIndex}
    vector<int> comp;
    vector<bool> visited;

    void dfsBridges(int u, int pEdgeIndex) {
        visited[u] = true;
        tin[u] = low[u] = timer++;
        for (auto& edge : adj[u]) {
            int v = edge.first;
            int idx = edge.second;
            if (idx == pEdgeIndex) continue;
            if (visited[v]) {
                low[u] = min(low[u], tin[v]);
            } else {
                dfsBridges(v, idx);
                low[u] = min(low[u], low[v]);
                if (low[v] > tin[u]) {
                    bridgeFlags[idx] = 1;
                }
            }
        }
    }

    void dfsComponents(int u, int c) {
        comp[u] = c;
        for (auto& edge : adj[u]) {
            int v = edge.first;
            int idx = edge.second;
            if (bridgeFlags[idx]) continue;
            if (comp[v] == 0) {
                dfsComponents(v, c);
            }
        }
    }

public:
    pair<vector<int>, vector<int>> bridgesAndComponents(int n, const vector<pair<int, int>>& edges) {
        int m = edges.size();
        adj.assign(n, vector<pair<int, int>>());
        for (int i = 0; i < m; i++) {
            adj[edges[i].first].push_back({edges[i].second, i});
            adj[edges[i].second].push_back({edges[i].first, i});
        }

        tin.assign(n, -1);
        low.assign(n, -1);
        visited.assign(n, false);
        bridgeFlags.assign(m, 0);
        timer = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfsBridges(i, -1);
            }
        }

        comp.assign(n, 0);
        int compCount = 0;
        for (int i = 0; i < n; i++) {
            if (comp[i] == 0) {
                compCount++;
                dfsComponents(i, compCount);
            }
        }

        return {bridgeFlags, comp};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    Solution solution;
    auto res = solution.bridgesAndComponents(n, edges);
    const vector<int>& bridgeFlags = res.first;
    const vector<int>& comp = res.second;

    int bridgeCount = 0;
    for (int f : bridgeFlags) bridgeCount += f;

    cout << bridgeCount << "\n";
    for (int i = 0; i < m; i++) {
        if (bridgeFlags[i]) {
            cout << edges[i].first << ' ' << edges[i].second << "\n";
        }
    }
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << comp[i];
    }
    return 0;
}
