#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    double streakProbability(int n, int k) {
        if (k > n) return 0.0;

        // Use long long for counts. 2^60 fits in long long (signed is up to 2^63-1).
        vector<long long> dp(n + 1);

        for (int i = 0; i < k; i++) {
            dp[i] = 1LL << i;
        }
        dp[k] = (1LL << k) - 1;

        for (int i = k + 1; i <= n; i++) {
            dp[i] = 2 * dp[i - 1] - dp[i - k - 1];
        }

        long long total = 1LL << n;
        return 1.0 - (double)dp[n] / total;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (cin >> n >> k) {
        Solution solution;
        cout << solution.streakProbability(n, k) << "\n";
    }
    return 0;
}
