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
    long long determinant_gaussian(int n, long long mod, vector<vector<long long>>& matrix) {
        MOD = mod;
        long long det = 1;

        for (int i = 0; i < n; i++) {
            int pivot = i;
            while (pivot < n && matrix[pivot][i] == 0) pivot++;

            if (pivot == n) return 0;

            if (pivot != i) {
                swap(matrix[i], matrix[pivot]);
                det = (MOD - det) % MOD;
            }

            det = (det * matrix[i][i]) % MOD;
            long long inv = modInverse(matrix[i][i]);

            for (int j = i + 1; j < n; j++) {
                if (matrix[j][i] != 0) {
                    long long factor = (matrix[j][i] * inv) % MOD;
                    for (int k = i; k < n; k++) {
                        long long sub = (factor * matrix[i][k]) % MOD;
                        matrix[j][k] = (matrix[j][k] - sub + MOD) % MOD;
                    }
                }
            }
        }

        return det;
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
    cout << solution.determinant_gaussian(n, MOD, matrix) << "\n";

    return 0;
}
