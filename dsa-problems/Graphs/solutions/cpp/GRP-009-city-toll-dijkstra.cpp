#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<long long> dijkstra(int n, vector<vector<pair<int,int>>>& adj, int source) {
        vector<long long> dist(n, LLONG_MAX);
        dist[source] = 0;

        priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<>> pq;
        pq.push({0, source});

        while (!pq.empty()) {
            auto [d, node] = pq.top();
            pq.pop();

            if (d > dist[node]) continue;

            // Sort neighbors for deterministic behavior
            sort(adj[node].begin(), adj[node].end(), [](const auto& a, const auto& b) {
                return a.second < b.second || (a.second == b.second && a.first < b.first);
            });

            for (auto [neighbor, weight] : adj[node]) {
                long long newDist = dist[node] + weight;
                if (newDist < dist[neighbor]) {
                    dist[neighbor] = newDist;
                    pq.push({newDist, neighbor});
                }
            }
        }

        return dist;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<pair<int,int>>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        int w = 1;  // Default weight
        if (cin.peek() != '\n' && cin.peek() != EOF) {
            cin >> w;
        }
        adj[u].push_back({v, w});
    }

    int source = 0;
    if (cin.peek() != EOF) {
        cin >> source;
    }

    Solution solution;
    vector<long long> result = solution.dijkstra(n, adj, source);

    for (int i = 0; i < result.size(); i++) {
        if (result[i] == LLONG_MAX) {
            cout << -1;
        } else {
            cout << result[i];
        }
        if (i < result.size() - 1) cout << " ";
    }
    cout << endl;

    return 0;
}
