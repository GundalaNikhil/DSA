#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long MOD = 998244353;
const long long G = 3;

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

class Solution {
public:
    vector<long long> convolution(vector<long long>& A, vector<long long>& B) {
        int size = 1;
        while (size < A.size() + B.size()) size <<= 1;

        vector<long long> fa(A.begin(), A.end());
        fa.resize(size);
        vector<long long> fb(B.begin(), B.end());
        fb.resize(size);

        ntt(fa, false);
        ntt(fb, false);

        for (int i = 0; i < size; i++) {
            fa[i] = (fa[i] * fb[i]) % MOD;
        }

        ntt(fa, true);

        fa.resize(A.size() + B.size() - 1);
        return fa;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];

    int m;
    cin >> m;
    vector<long long> B(m);
    for (int i = 0; i < m; i++) cin >> B[i];

    Solution solution;
    vector<long long> result = solution.convolution(A, B);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << (i < result.size() - 1 ? " " : "");
    }
    cout << "\n";

    return 0;
}
