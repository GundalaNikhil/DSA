#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
private:
    void bfs(int start, vector<vector<int>>& adj, vector<bool>& visited) {
        queue<int> q;
        q.push(start);
        visited[start] = true;
        
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            
            for (int neighbor : adj[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
    }
    
public:
    int countComponents(int n, vector<vector<int>>& adj) {
        vector<bool> visited(n, false);
        int components = 0;
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                components++;
                bfs(i, adj, visited);
            }
        }
        
        return components;
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
    cout << solution.countComponents(n, adj) << "\n";
    
    return 0;
}
