#include <iostream>
#include <vector>

using namespace std;

class Solution {
    const int MOD = 1000000007;
public:
    int countWays(int n, const vector<int>& jumps) {
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        
        for (int i = 1; i <= n; i++) {
            for (int jump : jumps) {
                if (i >= jump) {
                    dp[i] = (dp[i] + dp[i - jump]) % MOD;
                }
            }
        }
        
        return dp[n];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (cin >> n >> m) {
        vector<int> jumps(m);
        for (int i = 0; i < m; i++) cin >> jumps[i];

        Solution solution;
        cout << solution.countWays(n, jumps) << "\n";
    }
    return 0;
}
