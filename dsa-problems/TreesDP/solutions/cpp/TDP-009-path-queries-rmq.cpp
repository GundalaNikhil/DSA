#include <bits/stdc++.h>
using namespace std;

int n, timer_val;
vector<vector<pair<int, int>>> adj;
vector<int> first_occ, depth_val, euler_tour;
vector<vector<int>> st;
int log_size;

void dfs(int u, int p, int d) {
    depth_val[u] = d;
    first_occ[u] = timer_val;
    euler_tour[timer_val++] = u;

    for (auto [v, w] : adj[u]) {
        if (v != p) {
            dfs(v, u, d + w);
            euler_tour[timer_val++] = u;
        }
    }
}

void build_sparse_table() {
    int size = timer_val;
    log_size = __lg(size) + 1;
    st.assign(size, vector<int>(log_size));

    for (int i = 0; i < size; i++) {
        st[i][0] = i;
    }

    for (int j = 1; j < log_size; j++) {
        for (int i = 0; i + (1 << j) <= size; i++) {
            int left = st[i][j - 1];
            int right = st[i + (1 << (j - 1))][j - 1];
            st[i][j] = (depth_val[euler_tour[left]] <= depth_val[euler_tour[right]]) ? left : right;
        }
    }
}

int query_lca(int u, int v) {
    int l = first_occ[u], r = first_occ[v];
    if (l > r) swap(l, r);

    int len = r - l + 1;
    int k = __lg(len);

    int left = st[l][k];
    int right = st[r - (1 << k) + 1][k];

    int lca_idx = (depth_val[euler_tour[left]] <= depth_val[euler_tour[right]]) ? left : right;
    return euler_tour[lca_idx];
}

int query_distance(int u, int v) {
    int lca = query_lca(u, v);
    return depth_val[u] + depth_val[v] - 2 * depth_val[lca];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    adj.resize(n + 1);
    first_occ.resize(n + 1);
    depth_val.resize(n + 1);
    euler_tour.resize(2 * n);

    for (int i = 0; i < n - 1; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    timer_val = 0;
    dfs(1, 0, 0);
    build_sparse_table();

    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        int u, v;
        cin >> u >> v;
        cout << query_distance(u, v) << "\n";
    }

    return 0;
}
