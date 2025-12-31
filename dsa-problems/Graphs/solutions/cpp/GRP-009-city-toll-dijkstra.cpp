#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

class Solution {
public:
    vector<long long> dijkstra(int n, vector<vector<pair<int,int>>>& adj, int source) {
        vector<long long> dist(n, LLONG_MAX);
        dist[source] = 0;
        
        priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<>> pq;
        pq.push({0, source});
        
        while (!pq.empty()) {
            auto [d, node] = pq.top();
            pq.pop();
            
            if (d > dist[node]) continue;
            
            for (auto [neighbor, weight] : adj[node]) {
                long long newDist = dist[node] + weight;
                if (newDist < dist[neighbor]) {
                    dist[neighbor] = newDist;
                    pq.push({newDist, neighbor});
                }
            }
        }
        
        return dist;
    }
};
