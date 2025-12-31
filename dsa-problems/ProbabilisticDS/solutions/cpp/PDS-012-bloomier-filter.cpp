#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

class Solution {
public:
    pair<long long, double> bloomierStats(long long m, int r) {
        long long mem = m * r;
        double fpr = pow(2.0, -r);
        return {mem, fpr};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long m;
    int r;
    if (cin >> m >> r) {
        Solution solution;
        auto res = solution.bloomierStats(m, r);
        cout << res.first << " " << fixed << setprecision(6) << res.second << "\n";
    }
    return 0;
}
