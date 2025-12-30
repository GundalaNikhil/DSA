#include <iostream>
#include <vector>
using namespace std;

class Solution {
    long long MOD = 1000000007;

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

    void fwht(vector<long long>& a, bool invert) {
        int n = a.size();
        for (int len = 1; len < n; len <<= 1) {
            for (int i = 0; i < n; i += 2 * len) {
                for (int j = 0; j < len; j++) {
                    long long u = a[i + j];
                    long long v = a[i + j + len];
                    a[i + j] = (u + v) % MOD;
                    a[i + j + len] = (u - v + MOD) % MOD;
                }
            }
        }

        if (invert) {
            long long invN = modInverse(n);
            for (int i = 0; i < n; i++) {
                a[i] = (a[i] * invN) % MOD;
            }
        }
    }

public:
    vector<long long> fwht_xor_convolution(int k, vector<long long>& A, vector<long long>& B) {
        fwht(A, false);
        fwht(B, false);

        int n = A.size();
        vector<long long> C(n);
        for (int i = 0; i < n; i++) {
            C[i] = (A[i] * B[i]) % MOD;
        }

        fwht(C, true);
        return C;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k)) return 0;
    int n = 1 << k;

    vector<long long> A(n);
    for (int i = 0; i < n; i++) cin >> A[i];

    vector<long long> B(n);
    for (int i = 0; i < n; i++) cin >> B[i];

    Solution solution;
    vector<long long> result = solution.fwht_xor_convolution(k, A, B);

    for (int i = 0; i < n; i++) {
        cout << result[i] << (i < n - 1 ? " " : "");
    }
    cout << "\n";

    return 0;
}
