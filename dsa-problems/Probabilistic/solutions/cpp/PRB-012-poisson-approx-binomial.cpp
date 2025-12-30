#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
    pair<double, double> poissonApprox(int n, double p, int k) {
        double lambda = n * p;
        double pApprox;
        
        if (lambda == 0) {
            pApprox = (k == 0) ? 1.0 : 0.0;
        } else {
            // ln(P) = -lambda + k * ln(lambda) - lgamma(k+1)
            double logP = -lambda + k * log(lambda) - lgamma(k + 1);
            pApprox = exp(logP);
        }
        
        double err = min(1.0, 2.0 * n * p * p);
        
        return {pApprox, err};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    double p;
    if (cin >> n >> p >> k) {
        Solution solution;
        auto res = solution.poissonApprox(n, p, k);
        cout << fixed << setprecision(6) << res.first << " " << res.second << "\n";
    }
    return 0;
}
