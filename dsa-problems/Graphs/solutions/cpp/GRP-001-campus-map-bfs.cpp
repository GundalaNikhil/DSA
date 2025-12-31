#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> bfsTraversal(int n, vector<vector<int>>& adj) {
        vector<int> result;
        vector<bool> visited(n, false);
        queue<int> q;
        
        // Start BFS from node 0
        q.push(0);
        visited[0] = true;
        
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            result.push_back(curr);
            
            // Visit all unvisited neighbors
            for (int neighbor : adj[curr]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
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
    cin >> n >> m;
    
    vector<vector<int>> adj(n);
    
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    Solution solution;
    vector<int> result = solution.bfsTraversal(n, adj);
    
    for (int i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i < result.size() - 1) cout << " ";
    }
    cout << "\n";
    
    return 0;
}
