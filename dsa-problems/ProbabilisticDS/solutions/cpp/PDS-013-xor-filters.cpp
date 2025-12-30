#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

class Solution {
public:
    pair<long long, double> xorFilterStats(long long n, int b) {
        long long cells = (long long) ceil(1.23 * n);
        long long mem = cells * b;
        double fpr = pow(2.0, -b);
        return {mem, fpr};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int b;
    if (cin >> n >> b) {
        Solution solution;
        auto res = solution.xorFilterStats(n, b);
        cout << res.first << " " << fixed << setprecision(6) << res.second << "\n";
    }
    return 0;
}
