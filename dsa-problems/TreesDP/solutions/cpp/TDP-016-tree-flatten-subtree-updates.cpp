#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <cstring>
#include <climits>
using namespace std;

int n, timer_val;
vector<int> values, in_time, out_time;
vector<vector<int>> adj;
vector<long long> fenwick;

void dfs(int u, int p) {
    in_time[u] = ++timer_val;
    for (int v : adj[u]) {
        if (v != p) dfs(v, u);
    }
    out_time[u] = timer_val;
}

void update(int i, long long val) {
    while (i <= n) {
        fenwick[i] += val;
        i += i & (-i);
    }
}

long long query(int i) {
    long long sum = 0;
    while (i > 0) {
        sum += fenwick[i];
        i -= i & (-i);
    }
    return sum;
}

int main() {
    cin >> n;
    values.resize(n + 1);
    for (int i = 1; i <= n; i++) cin >> values[i];

    adj.resize(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v); adj[v].push_back(u);
    }

    in_time.resize(n + 1);
    out_time.resize(n + 1);
    fenwick.resize(n + 2);
    timer_val = 0;
    dfs(1, 0);

    for (int i = 1; i <= n; i++) {
        update(in_time[i], values[i]);
        update(in_time[i] + 1, -values[i]);
    }

    int q; cin >> q;
    while (q--) {
        int t; cin >> t;
        if (t == 1) {
            int u; long long val; cin >> u >> val;
            update(in_time[u], val);
            update(out_time[u] + 1, -val);
        } else {
            int u; cin >> u;
            cout << query(in_time[u]) << "\n";
        }
    }

    return 0;
}
