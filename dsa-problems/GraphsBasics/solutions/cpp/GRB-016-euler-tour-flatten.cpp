#include <iostream>
#include <vector>

using namespace std;

class Solution {
    int timer;
    vector<int> tin, tout;

    void dfs(int u, int p, const vector<vector<int>>& adj) {
        tin[u] = timer++;
        for (int v : adj[u]) {
            if (v != p) {
                dfs(v, u, adj);
                timer++;
            }
        }
        tout[u] = timer;
    }

public:
    pair<vector<int>, vector<int>> eulerTour(int n, const vector<vector<int>>& adj, int root) {
        tin.assign(n, 0);
        tout.assign(n, 0);
        timer = 0;
        dfs(root, -1, adj);
        return {tin, tout};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<vector<int>> adj(n);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    int root;
    cin >> root;

    Solution solution;
    auto res = solution.eulerTour(n, adj, root);
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << res.first[i];
    }
    cout << "\n";
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << res.second[i];
    }
    return 0;
}
