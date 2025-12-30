#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    long long MOD;
    long long G = 3;

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

    void ntt(vector<long long>& a, bool invert) {
        int n = a.size();
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            for (; j & bit; bit >>= 1) j ^= bit;
            j ^= bit;
            if (i < j) swap(a[i], a[j]);
        }
        for (int len = 2; len <= n; len <<= 1) {
            long long wlen = power(G, (MOD - 1) / len);
            if (invert) wlen = modInverse(wlen);
            for (int i = 0; i < n; i += len) {
                long long w = 1;
                for (int j = 0; j < len / 2; j++) {
                    long long u = a[i + j];
                    long long v = (a[i + j + len / 2] * w) % MOD;
                    a[i + j] = (u + v) % MOD;
                    a[i + j + len / 2] = (u - v + MOD) % MOD;
                    w = (w * wlen) % MOD;
                }
            }
        }
        if (invert) {
            long long nInv = modInverse(n);
            for (long long& x : a) x = (x * nInv) % MOD;
        }
    }

public:
    vector<long long> inversePolynomial(vector<long long>& P, int n, long long mod) {
        MOD = mod;
        vector<long long> b = {modInverse(P[0])};
        int len = 1;
        while (len < n) {
            len <<= 1;
            int limit = len << 1;
            
            vector<long long> copyA(limit, 0);
            vector<long long> copyB(limit, 0);
            
            for (int i = 0; i < min((int)P.size(), len); i++) copyA[i] = P[i];
            for (int i = 0; i < b.size(); i++) copyB[i] = b[i];
            
            ntt(copyA, false);
            ntt(copyB, false);
            
            for (int i = 0; i < limit; i++) {
                long long term = (copyA[i] * copyB[i]) % MOD;
                copyB[i] = (copyB[i] * (2 - term + MOD)) % MOD;
            }
            
            ntt(copyB, true);
            b.resize(len);
            for (int i = 0; i < len; i++) b[i] = copyB[i];
        }
        b.resize(n);
        return b;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k, n;
    if (!(cin >> k >> n)) return 0;
    vector<long long> P(k);
    for (int i = 0; i < k; i++) cin >> P[i];
    long long MOD;
    cin >> MOD;

    Solution solution;
    vector<long long> result = solution.inversePolynomial(P, n, MOD);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << (i < result.size() - 1 ? " " : "");
    }
    cout << "\n";

    return 0;
}
