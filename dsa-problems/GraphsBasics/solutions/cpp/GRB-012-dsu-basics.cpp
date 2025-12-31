#include <iostream>
#include <vector>
#include <string>
#include <numeric>

using namespace std;

class DSU {
    vector<int> parent;
    vector<int> rank;
public:
    DSU(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
        rank.assign(n, 0);
    }
    int find(int i) {
        if (parent[i] != i)
            parent[i] = find(parent[i]);
        return parent[i];
    }
    void unite(int i, int j) {
        int rootI = find(i);
        int rootJ = find(j);
        if (rootI != rootJ) {
            if (rank[rootI] < rank[rootJ])
                parent[rootI] = rootJ;
            else if (rank[rootI] > rank[rootJ])
                parent[rootJ] = rootI;
            else {
                parent[rootI] = rootJ;
                rank[rootJ]++;
            }
        }
    }
};

class Solution {
public:
    vector<bool> processQueries(int n, const vector<string>& type,
                                const vector<int>& u, const vector<int>& v) {
        DSU dsu(n);
        vector<bool> results;
        for (size_t i = 0; i < type.size(); ++i) {
            if (type[i] == "union") {
                dsu.unite(u[i], v[i]);
            } else {
                results.push_back(dsu.find(u[i]) == dsu.find(v[i]));
            }
        }
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<string> type(q);
    vector<int> u(q), v(q);
    for (int i = 0; i < q; i++) {
        cin >> type[i] >> u[i] >> v[i];
    }

    Solution solution;
    vector<bool> ans = solution.processQueries(n, type, u, v);
    for (int i = 0; i < (int)ans.size(); i++) {
        cout << (ans[i] ? "true" : "false");
        if (i + 1 < (int)ans.size()) cout << "\n";
    }
    return 0;
}
