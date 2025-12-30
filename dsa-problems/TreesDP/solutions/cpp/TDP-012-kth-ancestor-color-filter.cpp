#include <bits/stdc++.h>
using namespace std;

int n, LOG = 20;
vector<int> color;
vector<vector<int>> up, adj;

void dfs(int u, int p) {
    up[u][0] = p;
    for (int i = 1; i < LOG; i++) {
        up[u][i] = up[up[u][i - 1]][i - 1];
    }
    for (int v : adj[u]) {
        if (v != p) dfs(v, u);
    }
}

int findKth(int v, int c, int k) {
    int count = 0;
    while (v != 0) {
        if (color[v] == c) {
            count++;
            if (count == k) return v;
        }
        v = up[v][0];
    }
    return -1;
}

int main() {
    cin >> n;
    color.resize(n + 1);
    for (int i = 1; i <= n; i++) cin >> color[i];

    adj.resize(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v); adj[v].push_back(u);
    }

    up.assign(n + 1, vector<int>(LOG));
    dfs(1, 0);

    int q; cin >> q;
    while (q--) {
        int v, c, k; cin >> v >> c >> k;
        cout << findKth(v, c, k) << "\n";
    }
    return 0;
}
