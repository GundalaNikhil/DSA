#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

class Solution {
public:
    int shortestPathWithBattery(int n, vector<vector<int>>& edges, int source, int dest, int battery) {
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        vector<int> dist(n, numeric_limits<int>::max());

        dist[source] = 0;
        pq.push({0, source});

        while (!pq.empty()) {
            int d = pq.top().first;
            int u = pq.top().second;
            pq.pop();

            if (d > dist[u]) continue;
            if (u == dest) return d;

            for (const auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;

                if (w <= battery) { // Constraint Check
                    if (dist[u] != numeric_limits<int>::max() && dist[u] + w < dist[v]) {
                        dist[v] = dist[u] + w;
                        pq.push({dist[v], v});
                    }
                }
            }
        }

        return dist[dest] == numeric_limits<int>::max() ? -1 : dist[dest];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    if (!(cin >> n >> m)) return 0;
    
    vector<vector<int>> edges;
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        edges.push_back({u, v, w});
    }
    
    int source, dest, battery;
    cin >> source >> dest >> battery;
    
    Solution solution;
    cout << solution.shortestPathWithBattery(n, edges, source, dest, battery) << "\n";
    
    return 0;
}
