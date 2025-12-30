#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
    vector<bool> visited;
    stack<int> st;

    void dfs(int u, const vector<vector<pair<int, int>>>& adj) {
        visited[u] = true;
        for (auto& edge : adj[u]) {
            int v = edge.first;
            if (!visited[v]) dfs(v, adj);
        }
        st.push(u);
    }

public:
    vector<long long> shortestPathDAG(int n, const vector<vector<pair<int, int>>>& adj, int s) {
        visited.assign(n, false);
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) dfs(i, adj);
        }

        vector<long long> dist(n, 2e18); // Large value for infinity
        dist[s] = 0;

        while (!st.empty()) {
            int u = st.top();
            st.pop();

            if (dist[u] != 2e18) {
                for (auto& edge : adj[u]) {
                    int v = edge.first;
                    int w = edge.second;
                    if (dist[u] + w < dist[v]) {
                        dist[v] = dist[u] + w;
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (dist[i] == 2e18) dist[i] = -1;
        }
        return dist;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;
    vector<vector<pair<int, int>>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }

    Solution solution;
    vector<long long> dist = solution.shortestPathDAG(n, adj, s);
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << dist[i];
    }
    return 0;
}
