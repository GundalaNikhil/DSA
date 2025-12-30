#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>

using namespace std;

class Solution {
    vector<vector<double>> invert(vector<vector<double>> A) {
        int n = A.size();
        vector<vector<double>> B(n, vector<double>(2 * n));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) B[i][j] = A[i][j];
            B[i][n + i] = 1;
        }

        for (int i = 0; i < n; i++) {
            int pivot = i;
            for (int j = i + 1; j < n; j++) {
                if (abs(B[j][i]) > abs(B[pivot][i])) pivot = j;
            }
            swap(B[i], B[pivot]);

            double div = B[i][i];
            for (int j = i; j < 2 * n; j++) B[i][j] /= div;

            for (int k = 0; k < n; k++) {
                if (k != i) {
                    double factor = B[k][i];
                    for (int j = i; j < 2 * n; j++) B[k][j] -= factor * B[i][j];
                }
            }
        }

        vector<vector<double>> res(n, vector<double>(n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) res[i][j] = B[i][n + j];
        }
        return res;
    }

public:
    vector<double> absorptionStats(const vector<vector<double>>& P, int s) {
        int n = P.size();
        vector<int> absorbing, transient;

        for (int i = 0; i < n; i++) {
            if (abs(P[i][i] - 1.0) < 1e-9) absorbing.push_back(i);
            else transient.push_back(i);
        }

        bool startIsAbsorbing = false;
        for (int idx : absorbing) if (idx == s) startIsAbsorbing = true;

        if (startIsAbsorbing) {
            vector<double> res;
            res.push_back(0.0);
            for (int idx : absorbing) res.push_back(idx == s ? 1.0 : 0.0);
            return res;
        }

        int tSize = transient.size();
        int aSize = absorbing.size();

        vector<vector<double>> Q(tSize, vector<double>(tSize));
        vector<vector<double>> R(tSize, vector<double>(aSize));

        for (int i = 0; i < tSize; i++) {
            int u = transient[i];
            for (int j = 0; j < tSize; j++) {
                int v = transient[j];
                Q[i][j] = P[u][v];
            }
            for (int j = 0; j < aSize; j++) {
                int v = absorbing[j];
                R[i][j] = P[u][v];
            }
        }

        vector<vector<double>> I_minus_Q(tSize, vector<double>(tSize));
        for (int i = 0; i < tSize; i++) {
            for (int j = 0; j < tSize; j++) {
                I_minus_Q[i][j] = (i == j ? 1.0 : 0.0) - Q[i][j];
            }
        }

        vector<vector<double>> N = invert(I_minus_Q);

        int sIdx = -1;
        for (int i = 0; i < tSize; i++) if (transient[i] == s) sIdx = i;

        double expectedSteps = 0;
        for (int j = 0; j < tSize; j++) expectedSteps += N[sIdx][j];

        vector<double> probs(aSize, 0.0);
        for (int j = 0; j < aSize; j++) {
            for (int k = 0; k < tSize; k++) {
                probs[j] += N[sIdx][k] * R[k][j];
            }
        }

        vector<double> result;
        result.push_back(expectedSteps);
        for (double p : probs) result.push_back(p);
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s;
    if (cin >> n >> s) {
        vector<vector<double>> P(n, vector<double>(n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) cin >> P[i][j];
        }

        Solution solution;
        vector<double> res = solution.absorptionStats(P, s);
        if (!res.empty()) {
            cout << fixed << setprecision(6) << res[0] << "\n";
            for (int i = 1; i < (int)res.size(); i++) {
                if (i > 1) cout << " ";
                cout << fixed << setprecision(6) << res[i];
            }
            cout << "\n";
        }
    }
    return 0;
}
