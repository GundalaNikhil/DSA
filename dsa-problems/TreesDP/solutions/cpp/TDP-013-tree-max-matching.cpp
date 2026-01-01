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

int n;
vector<vector<int>> adj;
vector<array<int, 2>> dp;

void dfs(int u, int p) {
    dp[u][0] = 0;
    dp[u][1] = 0;
    int sum = 0;

    for (int v : adj[u]) {
        if (v == p) continue;
        dfs(v, u);
        sum += max(dp[v][0], dp[v][1]);
    }

    dp[u][0] = sum;

    for (int v : adj[u]) {
        if (v == p) continue;
        dp[u][1] = max(dp[u][1], 1 + dp[v][0] + sum - max(dp[v][0], dp[v][1]));
    }
}

int main() {
    cin >> n;
    adj.resize(n + 1);
    dp.resize(n + 1);

    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v); adj[v].push_back(u);
    }

    dfs(1, 0);
    cout << max(dp[1][0], dp[1][1]) << "\n";
    return 0;
}
