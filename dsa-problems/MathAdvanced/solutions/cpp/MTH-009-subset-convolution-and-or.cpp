#include <iostream>
#include <vector>
using namespace std;

class Solution {
    long long MOD = 1000000007;

    void fzt_or(vector<long long>& a, int n, bool invert) {
        int size = 1 << n;
        for (int i = 0; i < n; i++) {
            for (int mask = 0; mask < size; mask++) {
                if (mask & (1 << i)) {
                    long long u = a[mask];
                    long long v = a[mask ^ (1 << i)];
                    if (!invert) {
                        a[mask] = (u + v) % MOD;
                    } else {
                        a[mask] = (u - v + MOD) % MOD;
                    }
                }
            }
        }
    }

    void fzt_and(vector<long long>& a, int n, bool invert) {
        int size = 1 << n;
        for (int i = 0; i < n; i++) {
            for (int mask = 0; mask < size; mask++) {
                if (!(mask & (1 << i))) {
                    long long u = a[mask];
                    long long v = a[mask ^ (1 << i)];
                    if (!invert) {
                        a[mask] = (u + v) % MOD;
                    } else {
                        a[mask] = (u - v + MOD) % MOD;
                    }
                }
            }
        }
    }

public:
    vector<long long> subset_convolution_and_or(int n, int op, vector<long long>& A, vector<long long>& B) {
        int size = 1 << n;
        
        if (op == 1) { // OR
            fzt_or(A, n, false);
            fzt_or(B, n, false);
        } else { // AND
            fzt_and(A, n, false);
            fzt_and(B, n, false);
        }

        vector<long long> C(size);
        for (int i = 0; i < size; i++) {
            C[i] = (A[i] * B[i]) % MOD;
        }

        if (op == 1) { // OR
            fzt_or(C, n, true);
        } else { // AND
            fzt_and(C, n, true);
        }

        return C;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, op;
    if (!(cin >> n >> op)) return 0;
    int size = 1 << n;

    vector<long long> A(size);
    for (int i = 0; i < size; i++) cin >> A[i];

    vector<long long> B(size);
    for (int i = 0; i < size; i++) cin >> B[i];

    Solution solution;
    vector<long long> result = solution.subset_convolution_and_or(n, op, A, B);

    for (int i = 0; i < size; i++) {
        cout << result[i] << (i < size - 1 ? " " : "");
    }
    cout << "\n";

    return 0;
}
