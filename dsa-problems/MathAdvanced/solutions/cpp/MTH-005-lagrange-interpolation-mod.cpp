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
    long long lagrange_interpolation_mod(int k, long long X, long long mod, vector<pair<long long, long long>>& points) {
        MOD = mod;
        long long ans = 0;

        for (int i = 0; i < k; i++) {
            long long xi = points[i].first;
            long long yi = points[i].second;

            long long num = 1;
            long long den = 1;

            for (int j = 0; j < k; j++) {
                if (i == j) continue;
                long long xj = points[j].first;

                num = (num * (X - xj + MOD)) % MOD;
                den = (den * (xi - xj + MOD)) % MOD;
            }

            long long term = (yi * num) % MOD;
            term = (term * modInverse(den)) % MOD;
            ans = (ans + term) % MOD;
        }

        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    long long X, MOD;
    if (!(cin >> k >> X >> MOD)) return 0;

    vector<pair<long long, long long>> points(k);
    for (int i = 0; i < k; i++) {
        cin >> points[i].first >> points[i].second;
    }

    Solution solution;
    cout << solution.lagrange_interpolation_mod(k, X, MOD, points) << "\n";

    return 0;
}
