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

int n, K, F;
vector<int> color;
vector<vector<int>> adj;
vector<vector<array<long long, 2>>> dp;
long long answer = 0;

void dfs(int u, int p) {
    dp[u][0][color[u] == F ? 1 : 0] = 1;

    for (int v : adj[u]) {
        if (v == p) continue;
        dfs(v, u);

        // Save current dp[u] before merging
        vector<array<long long, 2>> temp(K + 1);
        for (int d = 0; d <= K; d++) {
            temp[d] = dp[u][d];
        }

        for (int d1 = 0; d1 < K; d1++) {
            for (int d2 = 0; d1 + d2 + 1 <= K; d2++) {
                for (int h1 = 0; h1 < 2; h1++) {
                    for (int h2 = 0; h2 < 2; h2++) {
                        if (d1 + d2 + 1 == K) {
                            // Count pairs only if path is clean
                            if (h1 == 0 && h2 == 0 && color[u] != F) {
                                answer += temp[d1][h1] * dp[v][d2][h2];
                            }
                        }

                        // Merge: path has forbidden if any segment has it or u has it
                        int newHas = h1 | h2 | (color[u] == F ? 1 : 0);
                        if (d1 + d2 + 1 <= K) {
                            dp[u][d1 + d2 + 1][newHas] += temp[d1][h1] * dp[v][d2][h2];
                        }
                    }
                }
            }
        }
    }
}

int main() {
    cin >> n >> K >> F;
    color.resize(n + 1);
    for (int i = 1; i <= n; i++) cin >> color[i];

    adj.resize(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    dp.assign(n + 1, vector<array<long long, 2>>(K + 1, {0, 0}));
    dfs(1, 0);
    cout << answer << "\n";
    return 0;
}
