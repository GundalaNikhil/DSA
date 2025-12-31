#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
private:
    int timer = 0;
    unordered_set<int> ap;
    
    void dfs(int u, vector<vector<int>>& adj, vector<int>& disc, 
             vector<int>& low, vector<int>& parent) {
        int children = 0;
        disc[u] = low[u] = timer++;
        
        for (int v : adj[u]) {
            if (disc[v] == -1) {
                children++;
                parent[v] = u;
                dfs(v, adj, disc, low, parent);
                
                low[u] = min(low[u], low[v]);
                
                if (parent[u] != -1 && low[v] >= disc[u]) {
                    ap.insert(u);
                }
            } else if (v != parent[u]) {
                low[u] = min(low[u], disc[v]);
            }
        }
        
        if (parent[u] == -1 && children > 1) {
            ap.insert(u);
        }
    }
    
public:
    vector<int> findArticulationPoints(int n, vector<vector<int>>& adj) {
        vector<int> disc(n, -1);
        vector<int> low(n, -1);
        vector<int> parent(n, -1);
        
        for (int i = 0; i < n; i++) {
            if (disc[i] == -1) {
                dfs(i, adj, disc, low, parent);
            }
        }
        
        return vector<int>(ap.begin(), ap.end());
    }
};
