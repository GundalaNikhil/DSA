#include <bits/stdc++.h>
using namespace std;

class Solution {
    static const long long INF = (long long)4e18;
public:
    int minCostWithFreeCells(const vector<vector<int>>& cost, int f) {
        int m = cost.size(), n = cost[0].size();
        vector<vector<vector<long long>>> dp(m, vector<vector<long long>>(n, vector<long long>(f + 1, INF)));
        dp[0][0][0] = cost[0][0];
        if (f > 0) dp[0][0][1] = 0;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                for (int k = 0; k <= f; k++) {
                    long long cur = dp[r][c][k];
                    if (cur == INF) continue;
                    if (c + 1 < n) {
                        dp[r][c + 1][k] = min(dp[r][c + 1][k], cur + cost[r][c + 1]);
                        if (k + 1 <= f) dp[r][c + 1][k + 1] = min(dp[r][c + 1][k + 1], cur);
                    }
                    if (r + 1 < m) {
                        dp[r + 1][c][k] = min(dp[r + 1][c][k], cur + cost[r + 1][c]);
                        if (k + 1 <= f) dp[r + 1][c][k + 1] = min(dp[r + 1][c][k + 1], cur);
                    }
                }
            }
        }

        long long ans = INF;
        for (int k = 0; k <= f; k++) ans = min(ans, dp[m - 1][n - 1][k]);
        return (int)ans;
    }
};
