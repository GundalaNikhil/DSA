#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>

using namespace std;

class Solution {
public:
    pair<double, double> estimatePi(long long N, long long C) {
        double pHat = (double)C / N;
        double piHat = 4.0 * pHat;

        double stdErrP = sqrt(pHat * (1.0 - pHat) / N);
        double error = 1.96 * stdErrP * 4.0;

        return {piHat, error};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, C;
    if (cin >> N >> C) {
        Solution solution;
        auto res = solution.estimatePi(N, C);
        cout << fixed << setprecision(6) << res.first << " " << res.second << "\n";
    }
    return 0;
}
