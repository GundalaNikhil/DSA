#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution {
private:
    vector<int> parent;
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    void unionNodes(int x, int y) {
        int px = find(x);
        int py = find(y);
        if (px != py) {
            parent[px] = py;
        }
    }
    
public:
    vector<int> courseSchedule(int n, vector<pair<int,int>>& prerequisites, vector<pair<int,int>>& pairs) {
        parent.resize(n);
        for (int i = 0; i < n; i++) parent[i] = i;
        
        // Union pairs
        for (auto& [a, b] : pairs) {
            unionNodes(a, b);
        }
        
        // Build contracted graph
        unordered_map<int, vector<int>> contracted;
        unordered_map<int, int> inDegree;
        unordered_set<int> roots;
        
        for (int i = 0; i < n; i++) {
            roots.insert(find(i));
        }
        
        for (int root : roots) {
            inDegree[root] = 0;
        }
        
        for (auto& [u, v] : prerequisites) {
            int from = find(u);
            int to = find(v);
            if (from != to) {
                contracted[from].push_back(to);
                inDegree[to]++;
            }
        }
        
        // Topological sort
        queue<int> q;
        for (int root : roots) {
            if (inDegree[root] == 0) {
                q.push(root);
            }
        }
        
        vector<int> topoOrder;
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            topoOrder.push_back(node);
            
            for (int neighbor : contracted[node]) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        if (topoOrder.size() != roots.size()) {
            return {}; // Cycle detected
        }
        
        // Expand super-nodes
        vector<int> result;
        for (int superNode : topoOrder) {
            for (int i = 0; i < n; i++) {
                if (find(i) == superNode) {
                    result.push_back(i);
                }
            }
        }
        
        return result;
    }
};
