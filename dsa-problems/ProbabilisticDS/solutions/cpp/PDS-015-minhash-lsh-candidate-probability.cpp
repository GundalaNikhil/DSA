#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    double lshCandidateProb(int b, int r, double s) {
        double probBandMatch = pow(s, r);
        double probAllBandsMismatch = pow(1.0 - probBandMatch, b);
        return 1.0 - probAllBandsMismatch;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int b, r;
    double s;
    if (cin >> b >> r >> s) {
        Solution solution;
        cout << fixed << setprecision(6) << solution.lshCandidateProb(b, r, s) << "\n";
    }
    return 0;
}
