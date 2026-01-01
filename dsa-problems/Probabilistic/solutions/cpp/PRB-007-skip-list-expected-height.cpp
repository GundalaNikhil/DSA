#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    double expectedHeight(int n, double p) {
        return log(n) / log(1.0 / p);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    double p;
    if (cin >> n >> p) {
        Solution solution;
        cout << fixed << setprecision(6) << solution.expectedHeight(n, p) << "\n";
    }
    return 0;
}
