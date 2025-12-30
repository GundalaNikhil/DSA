#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

class Solution {
public:
    pair<double, double> medianClt(int n) {
        double mean = 0.5;
        double variance = 1.0 / (4.0 * n);
        return {mean, variance};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        Solution solution;
        auto res = solution.medianClt(n);
        cout << fixed << setprecision(6) << res.first << " " << res.second << "\n";
    }
    return 0;
}
