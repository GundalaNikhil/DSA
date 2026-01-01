#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

const int MAXN = 100005;
const int LOG = 20;

int up[MAXN][LOG];
int depth[MAXN];
vector<int> tree[MAXN];

void dfs(int node, int parent, int d) {
    up[node][0] = parent;
    depth[node] = d;
    for (int child : tree[node]) {
        if (child != parent) {
            dfs(child, node, d + 1);
        }
    }
}

void preprocess(int root, int n) {
    memset(up, -1, sizeof(up));
    memset(depth, 0, sizeof(depth));
    
    // DFS to compute depths and immediate parents
    dfs(root, -1, 0);
    
    // Binary lifting preprocessing
    for (int j = 1; j < LOG; j++) {
        for (int i = 1; i <= n; i++) {
            if (up[i][j - 1] != -1) {
                up[i][j] = up[up[i][j - 1]][j - 1];
            }
        }
    }
}

int lca(int u, int v) {
    // Make u deeper
    if (depth[u] < depth[v]) {
        swap(u, v);
    }
    
    // Lift u to same level as v
    int diff = depth[u] - depth[v];
    for (int j = 0; j < LOG; j++) {
        if ((diff >> j) & 1) {
            u = up[u][j];
        }
    }
    
    if (u == v) return u;
    
    // Lift both simultaneously
    for (int j = LOG - 1; j >= 0; j--) {
        if (up[u][j] != -1 && up[u][j] != up[v][j]) {
            u = up[u][j];
            v = up[v][j];
        }
    }
    
    return up[u][0];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, q;
    cin >> n >> q;
    
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }
    
    preprocess(1, n);
    
    for (int i = 0; i < q; i++) {
        int u, v;
        cin >> u >> v;
        cout << lca(u, v) << "\n";
    }
    
    return 0;
}
