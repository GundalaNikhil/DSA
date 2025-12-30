#include <iostream>
#include <vector>

using namespace std;

class Solution {
    const int MOD = 1000000007;

    long long power(long long base, long long exp) {
        long long res = 1;
        base %= MOD;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp /= 2;
        }
        return res;
    }

public:
    long long countSurjections(int n, int k) {
        if (k > n) return 0;

        vector<vector<long long>> C(k + 1, vector<long long>(k + 1));
        for (int i = 0; i <= k; i++) {
            C[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
            }
        }

        long long ans = 0;
        for (int i = 0; i <= k; i++) {
            long long term = (C[k][i] * power(k - i, n)) % MOD;
            if (i % 2 == 1) {
                ans = (ans - term + MOD) % MOD;
            } else {
                ans = (ans + term) % MOD;
            }
        }

        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (cin >> n >> k) {
        Solution solution;
        cout << solution.countSurjections(n, k) << "\n";
    }
    return 0;
}
