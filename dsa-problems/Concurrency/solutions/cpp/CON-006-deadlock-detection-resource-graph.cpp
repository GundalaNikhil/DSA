#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    bool hasDeadlock(int n, vector<pair<int, int>>& edges) {
        vector<vector<int>> adj(n);
        vector<int> inDegree(n, 0);
        
        for (const auto& edge : edges) {
            adj[edge.first].push_back(edge.second);
            inDegree[edge.second]++;
        }
        
        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (inDegree[i] == 0) {
                q.push(i);
            }
        }
        
        int processedCount = 0;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            processedCount++;
            
            for (int v : adj[u]) {
                inDegree[v]--;
                if (inDegree[v] == 0) {
                    q.push(v);
                }
            }
        }
        
        return processedCount < n;
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
    cout << (solution.hasDeadlock(n, edges) ? "true" : "false") << "\n";
    
    return 0;
}
