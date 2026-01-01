#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
private:
    vector<int> result;
    vector<bool> visited;
    
    void dfs(int node, vector<vector<int>>& adj) {
        // Mark as visited and add to result (preorder)
        visited[node] = true;
        result.push_back(node);
        
        // Recursively visit all unvisited neighbors
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor, adj);
            }
        }
    }
    
public:
    vector<int> dfsTraversal(int n, vector<vector<int>>& adj) {
        result.clear();
        visited.assign(n, false);
        
        // Start DFS from node 0
        dfs(0, adj);
        
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

    // Sort neighbors for deterministic traversal
    for (int i = 0; i < n; i++) {
        sort(adj[i].begin(), adj[i].end());
    }

    Solution solution;
    vector<int> result = solution.dfsTraversal(n, adj);
    
    for (int i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i < result.size() - 1) cout << " ";
    }
    cout << "\n";
    
    return 0;
}
