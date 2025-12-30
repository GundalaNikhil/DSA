#include <iostream>
#include <vector>
#include <random>
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

    vector<long long> berlekampMassey(const vector<long long>& s) {
        vector<long long> C = {1};
        vector<long long> B = {1};
        int L = 0;
        int b = 1;
        long long b_delta = 1;

        for (int i = 0; i < s.size(); i++) {
            long long delta = s[i];
            for (int j = 1; j < C.size(); j++) {
                delta = (delta + C[j] * s[i - j]) % MOD;
            }

            if (delta == 0) {
                b++;
                continue;
            }

            vector<long long> T = C;
            long long factor = (delta * modInverse(b_delta)) % MOD;

            if (C.size() < B.size() + b) C.resize(B.size() + b, 0);
            for (int j = 0; j < B.size(); j++) {
                long long val = (B[j] * factor) % MOD;
                int idx = j + b;
                C[idx] = (C[idx] - val + MOD) % MOD;
            }

            if (2 * L <= i) {
                L = i + 1 - L;
                B = T;
                b_delta = delta;
                b = 1;
            } else {
                b++;
            }
        }
        return C;
    }

public:
    vector<long long> minimal_polynomial_matrix(int n, long long mod, vector<vector<long long>>& matrix) {
        MOD = mod;

        vector<long long> u(n), v(n);
        mt19937 rng(12345);
        for (int i = 0; i < n; i++) {
            u[i] = rng() % MOD;
            v[i] = rng() % MOD;
        }

        vector<long long> seq;
        vector<long long> currV = v;

        for (int k = 0; k < 2 * n + 2; k++) {
            long long val = 0;
            for (int i = 0; i < n; i++) val = (val + u[i] * currV[i]) % MOD;
            seq.push_back(val);

            vector<long long> nextV(n, 0);
            for (int r = 0; r < n; r++) {
                for (int c = 0; c < n; c++) {
                    nextV[r] = (nextV[r] + matrix[r][c] * currV[c]) % MOD;
                }
            }
            currV = nextV;
        }

        vector<long long> C = berlekampMassey(seq);
        int d = C.size() - 1;
        vector<long long> res;
        res.push_back(d);
        for (int i = d; i >= 0; i--) {
            res.push_back(C[i]);
        }
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long MOD;
    if (!(cin >> n >> MOD)) return 0;

    vector<vector<long long>> matrix(n, vector<long long>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }

    Solution solution;
    vector<long long> result = solution.minimal_polynomial_matrix(n, MOD, matrix);

    cout << result[0] << "\n";
    for (int i = 1; i < result.size(); i++) {
        cout << result[i] << (i < result.size() - 1 ? " " : "");
    }
    cout << "\n";

    return 0;
}
