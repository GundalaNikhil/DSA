#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

class Solution {
public:
    pair<double, double> cycleExpectations(int n, int k) {
        double expectedCyclesK = 1.0 / (double)k;
        double expectedLongest = (double)n * 0.624330;
        return {expectedCyclesK, expectedLongest};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (cin >> n >> k) {
        Solution solution;
        auto res = solution.cycleExpectations(n, k);
        cout << fixed << setprecision(6) << res.first << " " << res.second << "\n";
    }
    return 0;
}
