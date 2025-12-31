#include <bits/stdc++.h>
using namespace std;

int n;
vector<pair<int, long long>> adj[100005];
map<int, long long> marked;

long long bfs(int start) {
    vector<long long> dist(n + 1, LLONG_MAX);
    dist[start] = 0;
    queue<int> q;
    q.push(start);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (auto& [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                q.push(v);
            }
        }
    }
    long long minCost = LLONG_MAX;
    for (auto& [node, val] : marked) {
        if (dist[node] != LLONG_MAX) {
            minCost = min(minCost, dist[node] + val);
        }
    }
    return minCost;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int D;
    cin >> n >> D;

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    int q;
    cin >> q;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int v, t;
            long long val;
            cin >> v >> val >> t;
            marked[v] = val;
        } else {
            int v, t;
            cin >> v >> t;
            cout << bfs(v) << "\n";
        }
    }
    return 0;
}
