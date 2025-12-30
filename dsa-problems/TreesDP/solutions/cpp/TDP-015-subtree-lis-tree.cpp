#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> values, lis_len;
vector<vector<int>> adj;
vector<int> active;

void dfs(int u, int p) {
    int pos = lower_bound(active.begin(), active.end(), values[u]) - active.begin();
    int saved = (pos < active.size()) ? active[pos] : -1;

    if (pos < active.size()) {
        active[pos] = values[u];
    } else {
        active.push_back(values[u]);
    }

    lis_len[u] = active.size();

    for (int v : adj[u]) {
        if (v != p) dfs(v, u);
    }

    if (saved != -1) {
        active[pos] = saved;
    } else {
        active.pop_back();
    }
}

int main() {
    cin >> n;
    values.resize(n + 1);
    lis_len.resize(n + 1);
    adj.resize(n + 1);

    for (int i = 1; i <= n; i++) cin >> values[i];

    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v); adj[v].push_back(u);
    }

    dfs(1, 0);

    for (int i = 1; i <= n; i++) {
        cout << lis_len[i] << (i < n ? " " : "\n");
    }

    return 0;
}
