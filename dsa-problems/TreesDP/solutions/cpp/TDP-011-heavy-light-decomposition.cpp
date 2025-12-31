#include <bits/stdc++.h>
using namespace std;

int n, timer_val;
vector<vector<int>> adj;
vector<int> parent, depth, heavy, head, pos, values;
vector<long long> segTree;

int dfs1(int u, int p) {
    int size = 1, maxSize = 0;
    parent[u] = p;
    depth[u] = (p == 0) ? 0 : depth[p] + 1;

    for (int v : adj[u]) {
        if (v == p) continue;
        int subtreeSize = dfs1(v, u);
        size += subtreeSize;
        if (subtreeSize > maxSize) {
            maxSize = subtreeSize;
            heavy[u] = v;
        }
    }
    return size;
}

void dfs2(int u, int h) {
    head[u] = h;
    pos[u] = timer_val++;

    if (heavy[u] != -1) dfs2(heavy[u], h);

    for (int v : adj[u]) {
        if (v != parent[u] && v != heavy[u]) {
            dfs2(v, v);
        }
    }
}

void build(int node, int l, int r, vector<int>& posToVal) {
    if (l == r) {
        segTree[node] = posToVal[l];
        return;
    }
    int mid = (l + r) / 2;
    build(2 * node, l, mid, posToVal);
    build(2 * node + 1, mid + 1, r, posToVal);
    segTree[node] = segTree[2 * node] + segTree[2 * node + 1];
}

long long query(int node, int l, int r, int ql, int qr) {
    if (ql > r || qr < l) return 0;
    if (ql <= l && r <= qr) return segTree[node];
    int mid = (l + r) / 2;
    return query(2 * node, l, mid, ql, qr) + query(2 * node + 1, mid + 1, r, ql, qr);
}

long long queryPath(int u, int v) {
    long long result = 0;
    while (head[u] != head[v]) {
        if (depth[head[u]] < depth[head[v]]) swap(u, v);
        result += query(1, 0, n - 1, pos[head[u]], pos[u]);
        u = parent[head[u]];
    }
    if (depth[u] > depth[v]) swap(u, v);
    result += query(1, 0, n - 1, pos[u], pos[v]);
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    values.resize(n + 1);
    for (int i = 1; i <= n; i++) cin >> values[i];

    adj.resize(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    parent.resize(n + 1);
    depth.resize(n + 1);
    heavy.assign(n + 1, -1);
    head.resize(n + 1);
    pos.resize(n + 1);
    segTree.resize(4 * n);

    dfs1(1, 0);
    timer_val = 0;
    dfs2(1, 1);

    vector<int> posToVal(n);
    for (int i = 1; i <= n; i++) {
        posToVal[pos[i]] = values[i];
    }
    build(1, 0, n - 1, posToVal);

    int q; cin >> q;
    for (int i = 0; i < q; i++) {
        int u, v; cin >> u >> v;
        cout << queryPath(u, v) << "\n";
    }

    return 0;
}
