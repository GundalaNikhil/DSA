#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <stack>

using namespace std;

class Solution {
    int timer;
    vector<int> tin, low;
    vector<vector<int>> adj;
    set<int> articulationPoints;
    vector<vector<int>> bccs;
    stack<pair<int, int>> edgeStack;

    void dfs(int u, int p) {
        tin[u] = low[u] = timer++;
        int children = 0;

        for (int v : adj[u]) {
            if (v == p) continue;

            if (tin[v] != -1) {
                low[u] = min(low[u], tin[v]);
                if (tin[v] < tin[u]) {
                    edgeStack.push({u, v});
                }
            } else {
                edgeStack.push({u, v});
                children++;
                dfs(v, u);
                low[u] = min(low[u], low[v]);

                if ((p != -1 && low[v] >= tin[u]) || (p == -1 && children > 1)) {
                    articulationPoints.insert(u);
                }

                if (low[v] >= tin[u]) {
                    vector<int> bcc;
                    set<int> uniqueNodes;
                    while (true) {
                        pair<int, int> e = edgeStack.top();
                        edgeStack.pop();
                        uniqueNodes.insert(e.first);
                        uniqueNodes.insert(e.second);
                        if (e == make_pair(u, v)) break;
                    }
                    for (int node : uniqueNodes) bcc.push_back(node);
                    bccs.push_back(bcc);
                }
            }
        }
    }

public:
    pair<vector<int>, vector<vector<int>>> articulationAndBcc(int n, const vector<pair<int, int>>& edges) {
        adj.assign(n, vector<int>());
        for (const auto& e : edges) {
            adj[e.first].push_back(e.second);
            adj[e.second].push_back(e.first);
        }

        tin.assign(n, -1);
        low.assign(n, -1);
        articulationPoints.clear();
        bccs.clear();
        while (!edgeStack.empty()) edgeStack.pop();
        timer = 0;

        for (int i = 0; i < n; i++) {
            if (tin[i] == -1) {
                dfs(i, -1);
                if (!edgeStack.empty()) {
                    vector<int> bcc;
                    set<int> uniqueNodes;
                    while (!edgeStack.empty()) {
                        pair<int, int> e = edgeStack.top();
                        edgeStack.pop();
                        uniqueNodes.insert(e.first);
                        uniqueNodes.insert(e.second);
                    }
                    for (int node : uniqueNodes) bcc.push_back(node);
                    bccs.push_back(bcc);
                }
            }
        }

        vector<int> aps(articulationPoints.begin(), articulationPoints.end());
        return {aps, bccs};
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

    Solution solution;
    auto res = solution.articulationAndBcc(n, edges);
    const vector<int>& aps = res.first;
    const vector<vector<int>>& bccs = res.second;

    cout << aps.size();
    if (aps.size() > 0) {
        cout << "\n";
        for (int i = 0; i < (int)aps.size(); i++) {
            if (i) cout << ' ';
            cout << aps[i];
        }
    }
    cout << "\n" << bccs.size();
    for (const auto& bcc : bccs) {
        cout << "\n" << bcc.size();
        for (int v : bcc) cout << ' ' << v;
    }
    cout << "\n";
    return 0;
}
