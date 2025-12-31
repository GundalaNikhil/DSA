#include <iostream>
#include <vector>
#include <numeric>
#include <unordered_set>
#include <algorithm>
#include <sstream>

using namespace std;

class DSU {
public:
    vector<int> parent;
    vector<int> size;
    
    DSU(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
        size.assign(n, 1);
    }
    
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            size[root_j] += size[root_i];
        }
    }
};

class Solution {
public:
    int maxComponentSize(int n, vector<pair<int, int>>& edges, unordered_set<int>& vips) {
        DSU dsu(n);
        
        // 1. Union Non-VIP to Non-VIP
        for (const auto& edge : edges) {
            if (vips.find(edge.first) == vips.end() && vips.find(edge.second) == vips.end()) {
                dsu.unite(edge.first, edge.second);
            }
        }
        
        int max_comp = 0;
        // 2. Purely neutral
        for (int i = 0; i < n; i++) {
            if (vips.find(i) == vips.end() && dsu.parent[i] == i) {
                max_comp = max(max_comp, dsu.size[i]);
            }
        }
        
        if (vips.empty()) return max_comp;
        
        // 3. VIP augmented
        // Use vector of sets or similar. Since N is 10^5, map might be slow? 
        // But VIPs are subset of N.
        // Let's use adjacency list for VIPs -> roots
        vector<vector<int>> vip_adj(n); 
        
        for (const auto& edge : edges) {
            int u = edge.first;
            int v = edge.second;
            bool u_vip = vips.count(u);
            bool v_vip = vips.count(v);
            
            if (u_vip && !v_vip) {
                vip_adj[u].push_back(dsu.find(v));
            } else if (!u_vip && v_vip) {
                vip_adj[v].push_back(dsu.find(u));
            }
        }
        
        for (int i = 0; i < n; i++) {
            if (vips.count(i)) {
                int current_size = 1;
                sort(vip_adj[i].begin(), vip_adj[i].end());
                vip_adj[i].erase(unique(vip_adj[i].begin(), vip_adj[i].end()), vip_adj[i].end());
                
                for (int root : vip_adj[i]) {
                    current_size += dsu.size[root];
                }
                max_comp = max(max_comp, current_size);
            }
        }
        
        return max_comp;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    if (!(cin >> n >> m)) return 0;
    
    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].first >> edges[i].second;
    }
    
    unordered_set<int> vips;
    string line;
    getline(cin >> ws, line); // consume rest of line and read next
    stringstream ss(line);
    int vip;
    while (ss >> vip) {
        vips.insert(vip);
    }
    
    Solution solution;
    cout << solution.maxComponentSize(n, edges, vips) << "\n";
    
    return 0;
}
