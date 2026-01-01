#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <sstream>

using namespace std;

// Matrix Inversion
vector<vector<double>> invert(vector<vector<double>>& A) {
    int n = A.size();
    vector<vector<double>> B(n, vector<double>(2 * n));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) B[i][j] = A[i][j];
        B[i][n + i] = 1.0;
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

struct Result {
    double expectedSteps;
    vector<double> probs;
};

Result absorptionStats(const vector<vector<double>>& P, int s) {
    int n = P.size();
    vector<int> absorbing;
    vector<int> transient;

    for (int i = 0; i < n; i++) {
        if (abs(P[i][i] - 1.0) < 1e-9) absorbing.push_back(i);
        else transient.push_back(i);
    }

    bool sIsAbsorbing = false;
    for (int idx : absorbing) if (idx == s) sIsAbsorbing = true;

    if (sIsAbsorbing) {
        vector<double> probs;
        for (int idx : absorbing) probs.push_back(idx == s ? 1.0 : 0.0);
        return {0.0, probs};
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
    for (int i = 0; i < tSize; i++) {
        if (transient[i] == s) {
            sIdx = i;
            break;
        }
    }

    double expectedSteps = 0;
    for (int j = 0; j < tSize; j++) expectedSteps += N[sIdx][j];

    vector<double> probs(aSize, 0.0);
    for (int j = 0; j < aSize; j++) {
        probs[j] = 0.0;
        for (int k = 0; k < tSize; k++) {
            probs[j] += N[sIdx][k] * R[k][j];
        }
    }

    return {expectedSteps, probs};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<vector<double>> P(n, vector<double>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) cin >> P[i][j];
    }

    int num_queries;
    cin >> num_queries;
    vector<int> query_states(num_queries);
    for (int i = 0; i < num_queries; i++) cin >> query_states[i];

    int num_absorbing;
    cin >> num_absorbing;
    vector<int> absorbing_indices(num_absorbing);
    for (int i = 0; i < num_absorbing; i++) cin >> absorbing_indices[i];

    vector<int> all_absorbing_states;
    for (int i = 0; i < n; i++) {
        if (abs(P[i][i] - 1.0) < 1e-9) all_absorbing_states.push_back(i);
    }

    vector<string> final_probs;
    vector<string> final_steps;

    cout << fixed << setprecision(6);

    for (int s : query_states) {
        Result res = absorptionStats(P, s);
        
        stringstream ssSteps;
        ssSteps << fixed << setprecision(6) << res.expectedSteps;
        final_steps.push_back(ssSteps.str());

        // Map probs back to requested indices
        // res.probs corresponds to 'absorbing' list in order
        // We need for each 'absorbing_indices'
        
        // Reconstruct absorbing list order used in function
        vector<int> func_absorbing;
        for (int i = 0; i < n; i++) {
            if (abs(P[i][i] - 1.0) < 1e-9) func_absorbing.push_back(i);
        }

        for (int a_idx : absorbing_indices) {
            // Find a_idx in func_absorbing
            auto it = find(func_absorbing.begin(), func_absorbing.end(), a_idx);
            if (it != func_absorbing.end()) {
                int pos = distance(func_absorbing.begin(), it);
                stringstream ssProb;
                ssProb << fixed << setprecision(6) << res.probs[pos];
                final_probs.push_back(ssProb.str());
            }
        }
    }

    for (int i = 0; i < final_probs.size(); i++) {
        cout << final_probs[i] << (i == final_probs.size() - 1 ? "" : " ");
    }
    cout << "\n";
    for (int i = 0; i < final_steps.size(); i++) {
        cout << final_steps[i] << (i == final_steps.size() - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}

