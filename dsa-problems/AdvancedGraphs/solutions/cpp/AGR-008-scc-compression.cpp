#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <set>
#include <tuple>

using namespace std;

class Solution {
    int timer;
    vector<int> tin, low;
    vector<bool> onStack;
    stack<int> st;
    vector<vector<int>> sccs;

    void dfs(int u, const vector<vector<int>>& adj) {
        tin[u] = low[u] = timer++;
        st.push(u);
        onStack[u] = true;

        for (int v : adj[u]) {
            if (tin[v] == -1) {
                dfs(v, adj);
                low[u] = min(low[u], low[v]);
            } else if (onStack[v]) {
                low[u] = min(low[u], tin[v]);
            }
        }

        if (low[u] == tin[u]) {
            vector<int> component;
            while (true) {
                int v = st.top();
                st.pop();
                onStack[v] = false;
                component.push_back(v);
                if (u == v) break;
            }
            sccs.push_back(component);
        }
    }

public:
    tuple<int, vector<int>, vector<pair<int, int>>> sccCompress(int n, const vector<vector<int>>& adj) {
        tin.assign(n, -1);
        low.assign(n, -1);
        onStack.assign(n, false);
        while (!st.empty()) st.pop();
        sccs.clear();
        timer = 0;

        for (int i = 0; i < n; i++) {
            if (tin[i] == -1) {
                dfs(i, adj);
            }
        }

        int k = sccs.size();
        vector<int> comp(n);
        for (int i = 0; i < k; i++) {
            for (int node : sccs[i]) {
                comp[node] = i;
            }
        }

        set<pair<int, int>> dagEdges;
        for (int u = 0; u < n; u++) {
            for (int v : adj[u]) {
                if (comp[u] != comp[v]) {
                    dagEdges.insert({comp[u], comp[v]});
                }
            }
        }

        return {k, comp, vector<pair<int, int>>(dagEdges.begin(), dagEdges.end())};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
    }

    Solution solution;
    auto [k, comp, edges] = solution.sccCompress(n, adj);

    cout << k << "\n";
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << comp[i];
    }
    cout << "\n" << edges.size() << "\n";
    for (auto& e : edges) {
        cout << e.first << ' ' << e.second << "\n";
    }
    return 0;
}
