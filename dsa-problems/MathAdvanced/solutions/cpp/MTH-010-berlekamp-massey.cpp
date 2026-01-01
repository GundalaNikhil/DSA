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

    vector<long long> combine(const vector<long long>& A, const vector<long long>& B, const vector<long long>& Rec) {
        int K = Rec.size();
        vector<long long> prod(2 * K, 0);
        for (int i = 0; i < A.size(); i++) {
            for (int j = 0; j < B.size(); j++) {
                prod[i + j] = (prod[i + j] + A[i] * B[j]) % MOD;
            }
        }

        for (int i = prod.size() - 1; i >= K; i--) {
            long long factor = prod[i];
            if (factor == 0) continue;
            for (int j = 0; j < K; j++) {
                int target = i - 1 - j;
                prod[target] = (prod[target] + factor * Rec[j]) % MOD;
            }
        }
        prod.resize(K);
        return prod;
    }

public:
    long long berlekamp_massey(int m, long long n, long long mod, vector<long long>& S) {
        MOD = mod;
        vector<long long> C = {1};
        vector<long long> B = {1};
        int L = 0;
        int b = 1;
        long long b_delta = 1;

        for (int i = 0; i < m; i++) {
            long long delta = S[i];
            for (int j = 1; j < C.size(); j++) {
                delta = (delta + C[j] * S[i - j]) % MOD;
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

        int K = C.size() - 1;
        if (K == 0) return 0;

        vector<long long> Rec(K);
        for (int i = 0; i < K; i++) {
            Rec[i] = (MOD - C[i + 1]) % MOD;
        }

        if (n < m) return S[n];

        vector<long long> res(K, 0);
        res[0] = 1;
        vector<long long> base(K, 0);
        if (K > 1) base[1] = 1;
        else base[0] = Rec[0];

        long long exp = n;
        while (exp > 0) {
            if (exp & 1) res = combine(res, base, Rec);
            base = combine(base, base, Rec);
            exp >>= 1;
        }

        long long ans = 0;
        for (int i = 0; i < K; i++) {
            ans = (ans + res[i] * S[i]) % MOD;
        }

        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    long long n, MOD;
    if (!(cin >> m >> n)) return 0;
    vector<long long> S(m);
    for (int i = 0; i < m; i++) cin >> S[i];
    cin >> MOD;

    Solution solution;
    cout << solution.berlekamp_massey(m, n, MOD, S) << "\n";

    return 0;
}
