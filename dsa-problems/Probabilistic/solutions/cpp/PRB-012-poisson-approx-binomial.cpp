#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
    struct Result {
        double binomial;
        double approx;
        double error;
    };

    Result solve(int n, double p, int k) {
        double lambda = n * p;

        // 1. Exact Binomial: C(n, k) * p^k * (1-p)^(n-k)
        double binomialProb = 0.0;
        if (k <= n) {
            double logBinom = lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1);
            if (p > 0) logBinom += k * log(p);
            else if (k > 0) logBinom = -1e18; // -inf effectively

            if (p < 1) logBinom += (n - k) * log(1.0 - p);
            else if (n - k > 0) logBinom = -1e18;

            if (logBinom > -1e14) binomialProb = exp(logBinom);
            else binomialProb = 0.0;
        }

        // 2. Poisson Approx: e^-lambda * lambda^k / k!
        double approxProb = 0.0;
        if (lambda == 0) {
            approxProb = (k == 0) ? 1.0 : 0.0;
        } else {
            double logP = -lambda + k * log(lambda) - lgamma(k + 1);
            if (logP > -1e14) approxProb = exp(logP);
            else approxProb = 0.0;
        }

        double error = abs(binomialProb - approxProb);
        return {binomialProb, approxProb, error};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    double p;
    if (cin >> n >> p >> k) {
        Solution solution;
        auto res = solution.solve(n, p, k);
        // Output order: Approx Exact Error (matching Python print f"{approx} {binomial} {error}")
        cout << fixed << setprecision(9) 
             << res.approx << " " 
             << res.binomial << " " 
             << res.error << "\n";
    }
    return 0;
}
