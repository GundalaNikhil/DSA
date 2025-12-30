#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
    long long power(long long base, long long exp, long long mod) {
        long long res = 1;
        base %= mod;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp /= 2;
        }
        return res;
    }

    long long modInverse(long long n, long long mod) {
        return power(n, mod - 2, mod);
    }

    void ntt(vector<long long>& a, bool invert, long long mod, long long g) {
        int n = a.size();
        for (int i = 1, j = 0; i < n; i++) {
            int bit = n >> 1;
            for (; j & bit; bit >>= 1) j ^= bit;
            j ^= bit;
            if (i < j) swap(a[i], a[j]);
        }

        for (int len = 2; len <= n; len <<= 1) {
            long long wlen = power(g, (mod - 1) / len, mod);
            if (invert) wlen = modInverse(wlen, mod);
            for (int i = 0; i < n; i += len) {
                long long w = 1;
                for (int j = 0; j < len / 2; j++) {
                    long long u = a[i + j];
                    long long v = (a[i + j + len / 2] * w) % mod;
                    a[i + j] = (u + v) % mod;
                    a[i + j + len / 2] = (u - v + mod) % mod;
                    w = (w * wlen) % mod;
                }
            }
        }

        if (invert) {
            long long nInv = modInverse(n, mod);
            for (int i = 0; i < n; i++) a[i] = (a[i] * nInv) % mod;
        }
    }

    vector<long long> convolve(const vector<long long>& A, const vector<long long>& B, long long mod, long long g) {
        int size = 1;
        while (size < A.size() + B.size()) size <<= 1;
        vector<long long> fa(size), fb(size);
        for(int i=0; i<A.size(); i++) fa[i] = A[i];
        for(int i=0; i<B.size(); i++) fb[i] = B[i];

        ntt(fa, false, mod, g);
        ntt(fb, false, mod, g);
        for (int i = 0; i < size; i++) fa[i] = (fa[i] * fb[i]) % mod;
        ntt(fa, true, mod, g);
        return fa;
    }

public:
    vector<long long> convolution_multi_mod_crt(int n, int m, vector<long long>& A, vector<long long>& B, long long targetMod) {
        long long P1 = 998244353, G1 = 3;
        long long P2 = 1004535809, G2 = 3;
        long long P3 = 469762049, G3 = 3;

        vector<long long> c1 = convolve(A, B, P1, G1);
        vector<long long> c2 = convolve(A, B, P2, G2);
        vector<long long> c3 = convolve(A, B, P3, G3);

        int len = n + m - 1;
        vector<long long> res(len);

        long long P1_inv_P2 = modInverse(P1, P2);
        long long P1P2_inv_P3 = modInverse((P1 * P2) % P3, P3);

        for (int i = 0; i < len; i++) {
            long long a1 = c1[i];
            long long a2 = c2[i];
            long long a3 = c3[i];

            long long x1 = a1;
            long long x2 = ((a2 - x1 + P2) % P2 * P1_inv_P2) % P2;
            long long x3 = ((a3 - x1 - x2 * P1 % P3 + 2 * P3) % P3 * P1P2_inv_P3) % P3;

            long long ans = (x1 + x2 * P1) % targetMod;
            ans = (ans + (x3 * ((P1 * P2) % targetMod)) % targetMod) % targetMod;
            res[i] = ans;
        }

        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];

    vector<long long> B(m);
    for (int i = 0; i < m; i++) cin >> B[i];

    long long MOD;
    cin >> MOD;

    Solution solution;
    vector<long long> result = solution.convolution_multi_mod_crt(n, m, A, B, MOD);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << (i < result.size() - 1 ? " " : "");
    }
    cout << "\n";

    return 0;
}
