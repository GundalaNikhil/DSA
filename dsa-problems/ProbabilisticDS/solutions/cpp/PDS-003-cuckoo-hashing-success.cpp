#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    double successProbability(long long m, double alpha) {
        double val = 1.0 - alpha;
        double exponent = -(val * val * (double)m) / 2.0;
        double pFail = exp(exponent);
        return 1.0 - pFail;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long m;
    double alpha;
    if (cin >> m >> alpha) {
        Solution solution;
        cout << fixed << setprecision(6) << solution.successProbability(m, alpha) << "\n";
    }
    return 0;
}
