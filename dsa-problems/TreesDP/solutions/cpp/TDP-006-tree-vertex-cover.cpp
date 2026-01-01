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

const int MAXN = 200005;
vector<int> graph[MAXN];
int dp[MAXN][2];
int n;

void dfs(int u, int parent) {
    dp[u][0] = 0;  // Not including u
    dp[u][1] = 1;  // Including u

    for (int v : graph[u]) {
        if (v == parent) continue;

        dfs(v, u);

        // If u not included, all children must be included
        dp[u][0] += dp[v][1];

        // If u included, take minimum for each child
        dp[u][1] += min(dp[v][0], dp[v][1]);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    dfs(1, -1);

    int result = min(dp[1][0], dp[1][1]);
    cout << result << endl;

    return 0;
}
