#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
private:
    int timer = 0;
    vector<pair<int,int>> bridges;
    
    void dfs(int u, vector<vector<int>>& adj, vector<int>& disc, 
             vector<int>& low, vector<int>& parent) {
        disc[u] = low[u] = timer++;
        
        for (int v : adj[u]) {
            if (disc[v] == -1) {
                parent[v] = u;
                dfs(v, adj, disc, low, parent);
                
                low[u] = min(low[u], low[v]);
                
                if (low[v] > disc[u]) {
                    bridges.push_back({u, v});
                }
            } else if (v != parent[u]) {
                low[u] = min(low[u], disc[v]);
            }
        }
    }
    
public:
    vector<pair<int,int>> findBridges(int n, vector<vector<int>>& adj) {
        vector<int> disc(n, -1);
        vector<int> low(n, -1);
        vector<int> parent(n, -1);
        
        for (int i = 0; i < n; i++) {
            if (disc[i] == -1) {
                dfs(i, adj, disc, low, parent);
            }
        }
        
        return bridges;
    }
};
