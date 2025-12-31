#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
private:
    bool bfs(int start, vector<vector<int>>& adj, vector<int>& color, vector<int>& locked) {
        queue<int> q;
        q.push(start);
        if (color[start] == -1) {
            color[start] = (locked[start] == 0) ? 1 : locked[start];
        }
        
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            int requiredNeighborColor = 3 - color[node];
            
            for (int neighbor : adj[node]) {
                if (color[neighbor] == -1) {
                    if (locked[neighbor] != 0 && locked[neighbor] != requiredNeighborColor) {
                        return false;
                    }
                    color[neighbor] = requiredNeighborColor;
                    q.push(neighbor);
                } else if (color[neighbor] != requiredNeighborColor) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
public:
    bool canColorBipartite(int n, vector<vector<int>>& adj, vector<int>& locked) {
        vector<int> color(n, -1);
        
        // Pre-color locked nodes
        for (int i = 0; i < n; i++) {
            if (locked[i] != 0) {
                color[i] = locked[i];
            }
        }
        
        // Check each component
        for (int i = 0; i < n; i++) {
            if (color[i] == -1) {
                if (!bfs(i, adj, color, locked)) {
                    return false;
                }
            }
        }
        
        return true;
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
    
    vector<int> locked(n);
    for (int i = 0; i < n; i++) {
        cin >> locked[i];
    }
    
    Solution solution;
    cout << (solution.canColorBipartite(n, adj, locked) ? "true" : "false") << "\n";
    
    return 0;
}
