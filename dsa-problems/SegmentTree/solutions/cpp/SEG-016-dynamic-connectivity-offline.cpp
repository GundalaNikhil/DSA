#include <vector>
#include <string>
#include <map>
#include <stack>
#include <algorithm>
#include <iostream>

using namespace std;

struct Edge {
    int u, v;
};

struct DSU {
    vector<int> parent;
    vector<int> rank;
    struct RollbackInfo {
        int child, parent;
    };
    stack<RollbackInfo> history;

    DSU(int n) {
        parent.resize(n + 1);
        rank.resize(n + 1, 1);
        for (int i = 1; i <= n; i++) parent[i] = i;
    }

    int find(int i) {
        if (parent[i] == i) return i;
        return find(parent[i]);
    }

    void unite(int i, int j) {
        int rootI = find(i);
        int rootJ = find(j);
        if (rootI != rootJ) {
            if (rank[rootI] < rank[rootJ]) swap(rootI, rootJ);
            parent[rootJ] = rootI;
            rank[rootI] += rank[rootJ];
            history.push({rootJ, rootI});
        } else {
            history.push({-1, -1});
        }
    }

    void rollback() {
        RollbackInfo op = history.top();
        history.pop();
        if (op.child != -1) {
            parent[op.child] = op.child;
            rank[op.parent] -= rank[op.child];
        }
    }

    bool connected(int i, int j) {
        return find(i) == find(j);
    }
};

class Solution {
    vector<vector<Edge>> tree;
    vector<pair<int, int>> queries;
    vector<string> results;

    void addEdge(int node, int start, int end, int l, int r, Edge e) {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            tree[node].push_back(e);
            return;
        }
        int mid = (start + end) / 2;
        addEdge(2 * node + 1, start, mid, l, r, e);
        addEdge(2 * node + 2, mid + 1, end, l, r, e);
    }

    void dfs(int node, int start, int end, DSU& dsu) {
        for (const auto& e : tree[node]) {
            dsu.unite(e.u, e.v);
        }

        if (start == end) {
            if (queries[start].first != -1) {
                results.push_back(dsu.connected(queries[start].first, queries[start].second) ? "true" : "false");
            }
        } else {
            int mid = (start + end) / 2;
            dfs(2 * node + 1, start, mid, dsu);
            dfs(2 * node + 2, mid + 1, end, dsu);
        }

        for (size_t i = 0; i < tree[node].size(); i++) {
            dsu.rollback();
        }
    }

public:
    vector<string> process(int n, const vector<vector<string>>& events) {
        int m = events.size();
        tree.resize(4 * m);
        queries.assign(m, {-1, -1});
        
        map<pair<int, int>, int> activeEdges;
        
        for (int i = 0; i < m; i++) {
            string type = events[i][0];
            int u = stoi(events[i][1]);
            int v = stoi(events[i][2]);
            if (u > v) swap(u, v);
            
            if (type == "ADD") {
                activeEdges[{u, v}] = i;
            } else if (type == "REMOVE") {
                if (activeEdges.count({u, v})) {
                    int start = activeEdges[{u, v}];
                    activeEdges.erase({u, v});
                    addEdge(0, 0, m - 1, start, i - 1, {u, v});
                }
            } else {
                queries[i] = {u, v};
            }
        }
        
        for (auto const& [edge, start] : activeEdges) {
            addEdge(0, 0, m - 1, start, m - 1, {edge.first, edge.second});
        }
        
        DSU dsu(n);
        dfs(0, 0, m - 1, dsu);
        
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<string>> events(m);
    for (int i = 0; i < m; i++) {
        string type, u, v;
        cin >> type >> u >> v;
        events[i] = {type, u, v};
    }
    Solution sol;
    vector<string> results = sol.process(n, events);
    for (const string& res : results) {
        cout << res << "\n";
    }
    return 0;
}
