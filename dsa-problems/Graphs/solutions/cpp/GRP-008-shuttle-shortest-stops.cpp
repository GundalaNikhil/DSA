#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> shortestDistances(int n, vector<vector<int>>& adj, int source) {
        vector<int> dist(n, -1);
        dist[source] = 0;
        
        queue<int> q;
        q.push(source);
        
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            
            for (int neighbor : adj[node]) {
                if (dist[neighbor] == -1) {
                    dist[neighbor] = dist[node] + 1;
                    q.push(neighbor);
                }
            }
        }
        
        return dist;
    }
};
