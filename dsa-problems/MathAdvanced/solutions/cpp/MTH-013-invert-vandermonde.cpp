#include <iostream>
#include <vector>
using namespace std;

class Solution {
    long long MOD;

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

    long long modInverse(long long n) {
        return power(n, MOD - 2);
    }

public:
    vector<vector<long long>> invert_vandermonde(int n, long long mod, vector<long long>& x) {
        MOD = mod;

        vector<long long> P(n + 1, 0);
        P[0] = 1;

        for (int k = 0; k < n; k++) {
            for (int i = k + 1; i >= 1; i--) {
                P[i] = (P[i - 1] - x[k] * P[i] % MOD + MOD) % MOD;
            }
            P[0] = (MOD - x[k] * P[0] % MOD) % MOD;
        }

        vector<vector<long long>> inv(n, vector<long long>(n));

        for (int i = 0; i < n; i++) {
            long long prod = 1;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                prod = (prod * (x[i] - x[j] + MOD)) % MOD;
            }
            long long w = modInverse(prod);

            long long q_k = 0;
            for (int k = n; k >= 1; k--) {
                long long val = (P[k] + x[i] * q_k) % MOD;
                q_k = val;
                inv[k - 1][i] = (val * w) % MOD;
            }
        }

        return inv;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long MOD;
    if (!(cin >> n >> MOD)) return 0;

    vector<long long> x(n);
    for (int i = 0; i < n; i++) cin >> x[i];

    Solution solution;
    vector<vector<long long>> res = solution.invert_vandermonde(n, MOD, x);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << res[i][j] << (j < n - 1 ? " " : "");
        }
        cout << "\n";
    }

    return 0;
}
