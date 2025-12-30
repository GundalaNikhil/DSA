#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

class Solution {
public:
    long long mstPrim(int n, const vector<vector<pair<int, int>>>& adj) {
        long long mstWeight = 0;
        vector<bool> visited(n, false);
        
        // Min-heap: {weight, node}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, 0});
        
        int nodesCount = 0;
        
        while (!pq.empty()) {
            int w = pq.top().first;
            int u = pq.top().second;
            pq.pop();
            
            if (visited[u]) continue;
            
            visited[u] = true;
            mstWeight += w;
            nodesCount++;
            
            if (nodesCount == n) break;
            
            for (auto& edge : adj[u]) {
                int v = edge.first;
                int weight = edge.second;
                if (!visited[v]) {
                    pq.push({weight, v});
                }
            }
        }
        
        return mstWeight;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<pair<int, int>>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    Solution solution;
    cout << solution.mstPrim(n, adj) << "\n";
    return 0;
}
