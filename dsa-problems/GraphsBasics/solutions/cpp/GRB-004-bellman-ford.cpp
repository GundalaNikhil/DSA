#include <iostream>
#include <vector>
#include <array>

using namespace std;

class Solution {
public:
    vector<long long> bellmanFord(int n, int s, const vector<array<int, 3>>& edges) {
        const long long INF = 1e18;
        vector<long long> dist(n, INF);
        dist[s] = 0;

        // Relax edges N-1 times
        for (int i = 0; i < n - 1; ++i) {
            bool changed = false;
            for (const auto& edge : edges) {
                int u = edge[0];
                int v = edge[1];
                int w = edge[2];
                if (dist[u] != INF && dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    changed = true;
                }
            }
            if (!changed) break;
        }

        // Check for negative cycle
        for (const auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            if (dist[u] != INF && dist[u] + w < dist[v]) {
                return {}; // Empty vector signals negative cycle
            }
        }

        for (int i = 0; i < n; ++i) {
            if (dist[i] == INF) dist[i] = -1;
        }

        return dist;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; ++i) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    vector<long long> dist = solution.bellmanFord(n, s, edges);

    if (dist.empty()) {
        cout << "NEGATIVE CYCLE";
    } else {
        for (int i = 0; i < n; ++i) {
            if (i) cout << ' ';
            cout << dist[i];
        }
    }
    cout << "\n";
    return 0;
}
