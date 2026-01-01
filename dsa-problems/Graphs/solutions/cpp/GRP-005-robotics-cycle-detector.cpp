#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
private:
    bool dfs(int node, int parent, vector<vector<int>>& adj, vector<bool>& visited) {
        visited[node] = true;
        
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                if (dfs(neighbor, node, adj, visited)) {
                    return true;
                }
            } else if (neighbor != parent) {
                return true; // Cycle detected
            }
        }
        
        return false;
    }
    
public:
    bool hasCycle(int n, vector<vector<int>>& adj) {
        vector<bool> visited(n, false);
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                if (dfs(i, -1, adj, visited)) {
                    return true;
                }
            }
        }
        
        return false;
    }
};

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // Sort neighbors for deterministic traversal
    for (int i = 0; i < n; i++) {
        sort(adj[i].begin(), adj[i].end());
    }

    Solution solution;
    cout << (solution.hasCycle(n, adj) ? "true" : "false") << endl;

    return 0;
}
