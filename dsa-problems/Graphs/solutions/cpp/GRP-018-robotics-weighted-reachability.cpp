#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<int> reachableNodes(int n, vector<vector<pair<int,int>>>& adj, 
                               int source, int threshold) {
        unordered_set<int> visited;
        queue<int> q;
        
        q.push(source);
        visited.insert(source);
        
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            
            for (auto& [neighbor, weight] : adj[node]) {
                if (weight <= threshold && visited.find(neighbor) == visited.end()) {
                    visited.insert(neighbor);
                    q.push(neighbor);
                }
            }
        }
        
        return vector<int>(visited.begin(), visited.end());
    }
};
