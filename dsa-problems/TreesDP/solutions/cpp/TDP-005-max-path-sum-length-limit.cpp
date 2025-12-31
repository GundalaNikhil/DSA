#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200005;
const long long NEG_INF = LLONG_MIN / 2;

vector<int> graph[MAXN];
long long value[MAXN];
long long dp[MAXN][505];
long long maxSum;
int n, L;

void dfs(int u, int parent) {
    dp[u][0] = value[u];
    maxSum = max(maxSum, value[u]);

    vector<vector<long long>> childPaths;

    for (int v : graph[u]) {
        if (v == parent) continue;

        dfs(v, u);

        vector<long long> childBest(L + 1, NEG_INF);

        for (int len = 0; len < L; len++) {
            if (dp[v][len] > NEG_INF) {
                long long extended = dp[v][len] + value[u];
                dp[u][len + 1] = max(dp[u][len + 1], extended);
                childBest[len] = dp[v][len];
            }
        }

        childPaths.push_back(childBest);
    }

    for (int len = 0; len <= L; len++) {
        maxSum = max(maxSum, dp[u][len]);
    }

    for (int i = 0; i < (int)childPaths.size(); i++) {
        for (int j = i + 1; j < (int)childPaths.size(); j++) {
            auto& path1 = childPaths[i];
            auto& path2 = childPaths[j];

            for (int len1 = 0; len1 <= L; len1++) {
                for (int len2 = 0; len2 <= L; len2++) {
                    // Total edges: len1 + 1 (to u) + 1 (from u) + len2
                    if (len1 + len2 + 2 > L) continue;
                    if (path1[len1] > NEG_INF && path2[len2] > NEG_INF) {
                        long long combined = path1[len1] + path2[len2] + value[u];
                        maxSum = max(maxSum, combined);
                    }
                }
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> L;

    for (int i = 1; i <= n; i++) {
        cin >> value[i];
    }

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= L; j++) {
            dp[i][j] = NEG_INF;
        }
    }

    maxSum = NEG_INF;

    dfs(1, -1);

    cout << maxSum << endl;

    return 0;
}
