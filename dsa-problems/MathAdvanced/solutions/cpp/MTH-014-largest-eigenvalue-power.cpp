#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

class Solution {
public:
    double largest_eigenvalue_power(int n, int maxIter, vector<vector<double>>& matrix, double epsilon) {
        vector<double> v(n, 1.0);
        double lambda = 0.0;

        for (int iter = 0; iter < maxIter; iter++) {
            vector<double> w(n, 0.0);
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    w[i] += matrix[i][j] * v[j];
                }
            }

            double num = 0.0;
            double den = 0.0;
            for (int i = 0; i < n; i++) {
                num += v[i] * w[i];
                den += v[i] * v[i];
            }

            double newLambda = (den == 0) ? 0 : num / den;

            if (abs(newLambda - lambda) < epsilon) {
                return newLambda;
            }
            lambda = newLambda;

            double maxVal = 0.0;
            for (double val : w) maxVal = max(maxVal, abs(val));

            if (maxVal < 1e-9) break;

            for (int i = 0; i < n; i++) {
                v[i] = w[i] / maxVal;
            }
        }

        return lambda;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, maxIter;
    if (!(cin >> n >> maxIter)) return 0;

    vector<vector<double>> matrix(n, vector<double>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }

    double epsilon;
    cin >> epsilon;

    Solution solution;
    double res = solution.largest_eigenvalue_power(n, maxIter, matrix, epsilon);

    cout << fixed << setprecision(6) << res << "\n";

    return 0;
}
