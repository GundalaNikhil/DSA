#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

class Solution {
public:
    pair<double, double> treapExpectations(int n) {
        double H = 0.0;
        for (int i = 1; i <= n; i++) {
            H += 1.0 / i;
        }
        
        double eDepth = 2 * H - 2;
        double ePath = 2 * (n + 1) * H - 4 * n;
        
        return {eDepth, ePath};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        Solution solution;
        auto res = solution.treapExpectations(n);
        cout << fixed << setprecision(6) << res.first << " " << res.second << "\n";
    }
    return 0;
}
