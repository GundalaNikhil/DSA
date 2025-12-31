#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

struct Edge {
    int u, v, cost;
    bool operator<(const Edge& other) const {
        return cost < other.cost;
    }
};

struct DSU {
    vector<int> parent;
    DSU(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    bool unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
            return true;
        }
        return false;
    }
};

class Solution {
public:
    long long minCost(int n, vector<int>& heights, vector<pair<int,int>>& existingCables) {
        DSU dsu(n);
        
        for (auto& cable : existingCables) {
            dsu.unite(cable.first, cable.second);
        }
        
        vector<pair<int,int>> sortedBuildings(n);
        for (int i = 0; i < n; i++) {
            sortedBuildings[i] = {heights[i], i};
        }
        
        sort(sortedBuildings.begin(), sortedBuildings.end());
        
        vector<Edge> edges;
        for (int i = 0; i < n - 1; i++) {
            int u = sortedBuildings[i].second;
            int v = sortedBuildings[i+1].second;
            int cost = sortedBuildings[i+1].first - sortedBuildings[i].first;
            edges.push_back({u, v, cost});
        }
        
        sort(edges.begin(), edges.end());
        
        long long totalCost = 0;
        for (const auto& edge : edges) {
            if (dsu.unite(edge.u, edge.v)) {
                totalCost += edge.cost;
            }
        }
        
        return totalCost;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> heights(n);
    for (int i = 0; i < n; i++) cin >> heights[i];

    int m;
    if (!(cin >> m)) return 0; // Should not happen based on constraints but safe check

    vector<pair<int,int>> existingCables(m);
    for (int i = 0; i < m; i++) {
        cin >> existingCables[i].first >> existingCables[i].second;
    }

    Solution solution;
    cout << solution.minCost(n, heights, existingCables) << "\n";

    return 0;
}
