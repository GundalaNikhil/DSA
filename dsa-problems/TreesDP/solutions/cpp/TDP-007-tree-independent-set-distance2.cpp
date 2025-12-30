#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200005;
vector<int> graph[MAXN];
long long weight[MAXN];
long long dp[MAXN][3];
int n;

void dfs(int u, int parent) {
    dp[u][0] = 0;
    dp[u][1] = 0;
    dp[u][2] = weight[u];

    long long sumWithoutSelected = 0;
    long long maxGain = LLONG_MIN;

    for (int v : graph[u]) {
        if (v == parent) continue;

        dfs(v, u);

        long long bestNotSelected = max(dp[v][0], dp[v][1]);
        sumWithoutSelected += bestNotSelected;

        long long gain = dp[v][2] - bestNotSelected;
        maxGain = max(maxGain, gain);

        dp[u][2] += dp[v][0];
    }

    dp[u][0] = sumWithoutSelected;

    if (maxGain > LLONG_MIN) {
        dp[u][1] = sumWithoutSelected + maxGain;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;

    for (int i = 1; i <= n; i++) {
        cin >> weight[i];
    }

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    dfs(1, -1);

    long long result = max({dp[1][0], dp[1][1], dp[1][2]});
    cout << result << endl;

    return 0;
}
