#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <numeric>
#include <limits>
#include <cmath>
#include <cstring>
#include <utility>
using namespace std;

class Solution {
    static const int MOD = 1000000007;
public:
    int countPathsWithTurnLimit(int m, int n, int T) {
        if (m == 1 && n == 1) return 1;
        vector<vector<vector<int>>> dpR(m, vector<vector<int>>(n, vector<int>(T + 1, 0)));
        vector<vector<vector<int>>> dpD(m, vector<vector<int>>(n, vector<int>(T + 1, 0)));

        if (n >= 2) dpR[0][1][0] = 1;
        if (m >= 2) dpD[1][0][0] = 1;

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if ((r == 0 && c == 0) || (r == 0 && c == 1) || (r == 1 && c == 0)) continue;
                for (int t = 0; t <= T; t++) {
                    long long vR = 0;
                    if (c - 1 >= 0) {
                        vR += dpR[r][c - 1][t];
                        if (t - 1 >= 0) vR += dpD[r][c - 1][t - 1];
                    }
                    dpR[r][c][t] = (int)(vR % MOD);

                    long long vD = 0;
                    if (r - 1 >= 0) {
                        vD += dpD[r - 1][c][t];
                        if (t - 1 >= 0) vD += dpR[r - 1][c][t - 1];
                    }
                    dpD[r][c][t] = (int)(vD % MOD);
                }
            }
        }

        long long ans = 0;
        for (int t = 0; t <= T; t++) ans = (ans + dpR[m - 1][n - 1][t] + dpD[m - 1][n - 1][t]) % MOD;
        return (int)ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m, n, T;
    cin >> m >> n >> T;
    Solution sol;
    cout << sol.countPathsWithTurnLimit(m, n, T) << '\n';
    return 0;
}
