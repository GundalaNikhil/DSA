#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <stack>

using namespace std;

struct DSU {
    vector<int> parent;
    vector<int> sz;
    stack<pair<int, int>> history;

    DSU(int n) {
        parent.resize(n);
        sz.assign(n, 1);
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    int find(int i) {
        while (i != parent[i]) i = parent[i];
        return i;
    }

    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            if (sz[root_i] < sz[root_j]) swap(root_i, root_j);
            parent[root_j] = root_i;
            sz[root_i] += sz[root_j];
            history.push({root_j, root_i});
            return true;
        }
        return false;
    }

    void rollback() {
        auto top = history.top(); history.pop();
        int child = top.first;
        int par = top.second;
        parent[child] = child;
        sz[par] -= sz[child];
    }
};

class Solution {
    vector<vector<int>> adj;
    vector<int> depth;
    vector<vector<int>> up;
    int LOG = 20;
    vector<vector<pair<int, int>>> seg;

    void dfsLCA(int u, int p, int d) {
        depth[u] = d;
        up[u][0] = p;
        for (int i = 1; i < LOG; i++) {
            if (up[u][i-1] != -1) up[u][i] = up[up[u][i-1]][i-1];
            else up[u][i] = -1;
        }
        for (int v : adj[u]) {
            if (v != p) dfsLCA(v, u, d + 1);
        }
    }

    int getLCA(int u, int v) {
        if (depth[u] < depth[v]) swap(u, v);
        for (int i = LOG - 1; i >= 0; i--) {
            if (depth[u] - (1 << i) >= depth[v]) u = up[u][i];
        }
        if (u == v) return u;
        for (int i = LOG - 1; i >= 0; i--) {
            if (up[u][i] != up[v][i]) {
                u = up[u][i];
                v = up[v][i];
            }
        }
        return up[u][0];
    }

    void addRange(int node, int start, int end, int l, int r, int u, int v) {
        if (r < start || end < l) return;
        if (l <= start && end <= r) {
            seg[node].push_back({u, v});
            return;
        }
        int mid = (start + end) / 2;
        addRange(node * 2, start, mid, l, r, u, v);
        addRange(node * 2 + 1, mid + 1, end, l, r, u, v);
    }

    void solve(int node, int start, int end, DSU& dsu, const vector<pair<int, int>>& queries, vector<int>& results) {
        int ops = 0;
        for (auto& edge : seg[node]) {
            if (dsu.unite(edge.first, edge.second)) ops++;
        }

        if (start == end) {
            if (start < queries.size() && queries[start].first != -1) {
                int u = queries[start].first;
                int v = queries[start].second;
                if (dsu.find(u) == dsu.find(v)) {
                    results[start] = getLCA(u, v);
                } else {
                    results[start] = -1;
                }
            }
        } else {
            int mid = (start + end) / 2;
            solve(node * 2, start, mid, dsu, queries, results);
            solve(node * 2 + 1, mid + 1, end, dsu, queries, results);
        }

        while (ops--) dsu.rollback();
    }

public:
    vector<int> offlineLca(int n, const vector<pair<int, int>>& edges,
                           const vector<string>& type, const vector<pair<int, int>>& args) {
        adj.assign(n, vector<int>());
        for (auto& e : edges) {
            adj[e.first].push_back(e.second);
            adj[e.second].push_back(e.first);
        }

        depth.assign(n, 0);
        up.assign(n, vector<int>(LOG, -1));
        dfsLCA(0, -1, 0);

        map<pair<int, int>, int> edgeStart;
        for (auto& e : edges) {
            int u = min(e.first, e.second);
            int v = max(e.first, e.second);
            edgeStart[{u, v}] = 0;
        }

        int q = type.size();
        seg.resize(4 * (q + 1));

        // Store queries indexed by time. -1 if not a query.
        vector<pair<int, int>> queries(q, {-1, -1});
        vector<int> queryIndices;

        for (int i = 0; i < q; i++) {
            int u = args[i].first;
            int v = args[i].second;
            if (u > v) swap(u, v);

            if (type[i] == "cut") {
                if (edgeStart.count({u, v})) {
                    int start = edgeStart[{u, v}];
                    // Cut at i removes the edge before later queries, so active range is [start, i-1].
                    edgeStart.erase({u, v});
                    addRange(1, 0, q, start, i - 1, u, v);
                }
            } else if (type[i] == "link") {
                edgeStart[{u, v}] = i + 1; // Active from next operation.
                // Or active immediately?
                // "link 1 3"
                // "query ..."
                // The query is a separate operation.
                // So link at i makes edge active for all j > i.
                // What if query is AT i? No, operations are distinct lines.
                // So query is at index k.
                // So link at i means active for [i+1, ...].
                // Edge active during query k if it exists.
                // If link is op i, it exists for op i+1.
                // So start = i + 1.
                // Initial edges start = 0.
            } else {
                queries[i] = {args[i].first, args[i].second}; // Use original args
                queryIndices.push_back(i);
            }
        }

        for (auto& p : edgeStart) {
            addRange(1, 0, q, p.second, q, p.first.first, p.first.second);
        }

        DSU dsu(n);
        vector<int> results(q, -2); // -2 sentinel
        solve(1, 0, q, dsu, queries, results);

        vector<int> finalOut;
        for (int idx : queryIndices) {
            finalOut.push_back(results[idx]);
        }
        return finalOut;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<pair<int, int>> edges(n - 1);
    for (int i = 0; i < n - 1; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    int q;
    cin >> q;
    vector<string> type(q);
    vector<pair<int, int>> args(q);
    for (int i = 0; i < q; i++) {
        cin >> type[i] >> args[i].first >> args[i].second;
    }

    Solution solution;
    vector<int> out = solution.offlineLca(n, edges, type, args);
    for (int i = 0; i < (int)out.size(); i++) {
        if (i) cout << "\n";
        cout << out[i];
    }
    return 0;
}
