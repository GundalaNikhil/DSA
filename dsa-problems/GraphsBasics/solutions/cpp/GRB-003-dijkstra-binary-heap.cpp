#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

class Solution {
public:
    vector<long long> dijkstra(int n, const vector<vector<pair<int, int>>>& adj, int s) {
        vector<long long> dist(n, -1);
        
        // Min-priority queue: stores {distance, node}
        // Use greater to make it a min-heap
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        
        dist[s] = 0;
        pq.push({0, s});
        
        while (!pq.empty()) {
            long long d = pq.top().first;
            int u = pq.top().second;
            pq.pop();
            
            // Lazy deletion check
            if (dist[u] != -1 && d > dist[u]) continue;
            
            for (auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;
                
                if (dist[v] == -1 || dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    pq.push({dist[v], v});
                }
            }
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
    vector<long long> dist = solution.dijkstra(n, adj, s);
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << dist[i];
    }
    cout << "\n";
    return 0;
}
