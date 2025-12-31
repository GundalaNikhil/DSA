#include <array>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

class Solution {
public:
    vector<vector<long long>> allPairsShortestPaths(int n, const vector<array<int, 3>>& edges) {
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
        }

        // Bellman-Ford
        vector<long long> h(n + 1, 0); // Virtual source n, connected to all with 0
        // Init h[0..n-1] = 0 is equivalent to 1st iteration of BF from virtual source
        
        for (int i = 0; i < n; i++) {
            bool changed = false;
            for (const auto& e : edges) {
                if (h[e[0]] + e[2] < h[e[1]]) {
                    h[e[1]] = h[e[0]] + e[2];
                    changed = true;
                }
            }
            if (!changed) break;
        }

        vector<vector<long long>> result(n, vector<long long>(n, INF));

        for (int s = 0; s < n; s++) {
            priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
            vector<long long> d(n, INF);

            d[s] = 0;
            pq.push({0, s});

            while (!pq.empty()) {
                long long distU = pq.top().first;
                int u = pq.top().second;
                pq.pop();

                if (distU > d[u]) continue;

                for (const auto& e : adj[u]) {
                    int v = e.first;
                    int w = e.second;
                    long long newWeight = w + h[u] - h[v];
                    if (d[u] + newWeight < d[v]) {
                        d[v] = d[u] + newWeight;
                        pq.push({d[v], v});
                    }
                }
            }

            for (int v = 0; v < n; v++) {
                if (d[v] != INF) {
                    result[s][v] = d[v] - h[s] + h[v];
                }
            }
        }

        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    vector<vector<long long>> dist = solution.allPairsShortestPaths(n, edges);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (j) cout << ' ';
            if (dist[i][j] >= INF / 2) cout << "INF";
            else cout << dist[i][j];
        }
        if (i + 1 < n) cout << "\n";
    }
    return 0;
}
