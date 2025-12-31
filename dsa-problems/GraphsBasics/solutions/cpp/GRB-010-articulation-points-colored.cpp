#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <array>

using namespace std;

class Solution {
    int timer;
    vector<int> disc, low, subRed, subBlue;
    int totalRed, totalBlue;
    set<int> critical;
    vector<vector<pair<int, int>>> adj;

    void dfs(int u, int p) {
        disc[u] = low[u] = ++timer;
        int children = 0;

        for (auto& edge : adj[u]) {
            int v = edge.first;
            int color = edge.second;

            if (v == p) continue;

            if (disc[v] != -1) {
                low[u] = min(low[u], disc[v]);
                if (disc[v] < disc[u]) {
                    if (color == 0) subRed[u]++;
                    else subBlue[u]++;
                }
            } else {
                children++;
                dfs(v, u);

                int branchRed = subRed[v] + (color == 0 ? 1 : 0);
                int branchBlue = subBlue[v] + (color == 1 ? 1 : 0);

                subRed[u] += branchRed;
                subBlue[u] += branchBlue;

                low[u] = min(low[u], low[v]);

                if (low[v] >= disc[u]) {
                    // When u is removed, edge (u,v) is also removed.
                    // Component v has only internal edges (subRed[v], subBlue[v]).
                    int vRed = subRed[v];
                    int vBlue = subBlue[v];

                    // Rest of graph minus v's subtree and the edge (u,v)
                    int restRed = totalRed - vRed - (color == 0 ? 1 : 0);
                    int restBlue = totalBlue - vBlue - (color == 1 ? 1 : 0);

                    if ((vRed > 0 && restBlue > 0) || (vBlue > 0 && restRed > 0)) {
                        critical.insert(u);
                    }
                }
            }
        }

        if (p == -1 && children < 2) {
            critical.erase(u);
        }
    }

public:
    vector<int> criticalNodes(int n, const vector<array<int, 3>>& edges) {
        adj.assign(n, vector<pair<int, int>>());
        totalRed = 0;
        totalBlue = 0;

        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
            if (e[2] == 0) totalRed++;
            else totalBlue++;
        }

        disc.assign(n, -1);
        low.assign(n, -1);
        subRed.assign(n, 0);
        subBlue.assign(n, 0);
        critical.clear();
        timer = 0;

        for (int i = 0; i < n; i++) {
            if (disc[i] == -1) {
                dfs(i, -1);
            }
        }

        return vector<int>(critical.begin(), critical.end());
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<array<int, 3>> edges;
    edges.reserve(m);
    for (int i = 0; i < m; i++) {
        int u, v; char c;
        cin >> u >> v >> c;
        edges.push_back({u, v, c == 'R' ? 0 : 1});
    }

    Solution solution;
    vector<int> ans = solution.criticalNodes(n, edges);
    cout << ans.size() << "\n";
    for (int i = 0; i < (int)ans.size(); i++) {
        if (i) cout << ' ';
        cout << ans[i];
    }
    cout << "\n";
    return 0;
}
