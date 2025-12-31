#include <iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <numeric>

using namespace std;

class DSU {
    vector<int> parent;
public:
    DSU(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int rootI = find(i);
        int rootJ = find(j);
        if (rootI != rootJ) parent[rootI] = rootJ;
    }
};

class Solution {
public:
    long long mstKruskal(int n, vector<array<int, 3>>& edges) {
        sort(edges.begin(), edges.end(), [](const array<int, 3>& a, const array<int, 3>& b) {
            return a[2] < b[2];
        });

        DSU dsu(n);
        long long mstWeight = 0;
        int edgesCount = 0;

        for (const auto& edge : edges) {
            if (dsu.find(edge[0]) != dsu.find(edge[1])) {
                dsu.unite(edge[0], edge[1]);
                mstWeight += edge[2];
                edgesCount++;
            }
        }
        return mstWeight;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    cout << solution.mstKruskal(n, edges) << "\n";
    return 0;
}
