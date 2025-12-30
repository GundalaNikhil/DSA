#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    bool isFeasible(int n, vector<vector<int>>& edges) {
        vector<int> indegree(n, 0);
        vector<vector<int>> adj(n);
        
        // Build graph
        for (auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            indegree[edge[1]]++;
        }
        
        // Initialize queue with indegree 0 nodes
        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        
        int processed = 0;
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            processed++;
            
            for (int v : adj[u]) {
                indegree[v]--;
                if (indegree[v] == 0) {
                    q.push(v);
                }
            }
        }
        
        return processed == n;
    }
};
