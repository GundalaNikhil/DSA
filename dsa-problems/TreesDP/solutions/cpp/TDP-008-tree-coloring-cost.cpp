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

int n, k;
vector<vector<int>> adj;
vector<vector<int>> cost;
vector<vector<long long>> dp;
vector<bool> visited;

void dfs(int u) {
    visited[u] = true;
    for (int c = 1; c <= k; c++) {
        dp[u][c] = cost[u][c];
    }

    for (int v : adj[u]) {
        if (!visited[v]) {
            dfs(v);

            long long min1 = LLONG_MAX, min2 = LLONG_MAX;
            int minColor = -1;
            for (int c = 1; c <= k; c++) {
                if (dp[v][c] < min1) {
                    min2 = min1;
                    min1 = dp[v][c];
                    minColor = c;
                } else if (dp[v][c] < min2) {
                    min2 = dp[v][c];
                }
            }

            for (int c = 1; c <= k; c++) {
                if (c == minColor) {
                    dp[u][c] += min2;
                } else {
                    dp[u][c] += min1;
                }
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> k;

    cost.assign(n + 1, vector<int>(k + 1));
    dp.assign(n + 1, vector<long long>(k + 1));
    adj.resize(n + 1);
    visited.assign(n + 1, false);

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= k; j++) {
            cin >> cost[i][j];
        }
    }

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dfs(1);

    long long result = LLONG_MAX;
    for (int c = 1; c <= k; c++) {
        result = min(result, dp[1][c]);
    }

    cout << result << "\n";
    return 0;
}
