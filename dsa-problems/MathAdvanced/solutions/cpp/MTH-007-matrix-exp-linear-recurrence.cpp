#include <iostream>
#include <vector>
using namespace std;

class Solution {
    long long MOD;
    int K;

    vector<vector<long long>> multiply(const vector<vector<long long>>& A, const vector<vector<long long>>& B) {
        vector<vector<long long>> C(K, vector<long long>(K, 0));
        for (int i = 0; i < K; i++) {
            for (int k = 0; k < K; k++) {
                if (A[i][k] == 0) continue;
                for (int j = 0; j < K; j++) {
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD;
                }
            }
        }
        return C;
    }

    vector<vector<long long>> power(vector<vector<long long>> A, long long exp) {
        vector<vector<long long>> res(K, vector<long long>(K, 0));
        for (int i = 0; i < K; i++) res[i][i] = 1;
        while (exp > 0) {
            if (exp & 1) res = multiply(res, A);
            A = multiply(A, A);
            exp >>= 1;
        }
        return res;
    }

public:
    long long matrix_exp_linear_recurrence(int k, long long n, long long mod, vector<long long>& coeffs, vector<long long>& initial) {
        MOD = mod;
        K = k;

        if (n < k) return initial[n];

        vector<vector<long long>> T(k, vector<long long>(k, 0));
        for (int j = 0; j < k; j++) {
            T[0][j] = coeffs[j];
        }
        for (int i = 1; i < k; i++) {
            T[i][i - 1] = 1;
        }

        T = power(T, n - k + 1);

        long long ans = 0;
        for (int j = 0; j < k; j++) {
            ans = (ans + T[0][j] * initial[k - 1 - j]) % MOD;
        }

        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    long long n, MOD;
    if (!(cin >> k >> n >> MOD)) return 0;

    vector<long long> coeffs(k);
    for (int i = 0; i < k; i++) cin >> coeffs[i];

    vector<long long> initial(k);
    for (int i = 0; i < k; i++) cin >> initial[i];

    Solution solution;
    cout << solution.matrix_exp_linear_recurrence(k, n, MOD, coeffs, initial) << "\n";

    return 0;
}
