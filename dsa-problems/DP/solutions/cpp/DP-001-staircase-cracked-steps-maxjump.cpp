#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    static const int MOD = 1000000007;

    int countWays(int n, int J, const vector<bool>& cracked) {
        if (cracked[n]) return 0;

        vector<long long> dp(n + 1, 0);
        dp[0] = 1;
        long long windowSum = 1;

        for (int i = 1; i <= n; i++) {
            dp[i] = cracked[i] ? 0 : windowSum;
            windowSum = (windowSum + dp[i]) % MOD;
            int out = i - J;
            if (out >= 0) {
                windowSum = (windowSum - dp[out]) % MOD;
                if (windowSum < 0) windowSum += MOD;
            }
        }
        return (int)(dp[n] % MOD);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, J;
    cin >> n >> J;
    int m;
    cin >> m;
    vector<bool> cracked(n + 1, false);
    for (int i = 0; i < m; i++) {
        int x;
        cin >> x;
        if (1 <= x && x <= n) cracked[x] = true;
    }

    Solution sol;
    cout << sol.countWays(n, J, cracked) << "\n";
    return 0;
}
