#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    double bloomFpr(double m, double k, double n) {
        double exponent = -k * n / m;
        double term = 1.0 - exp(exponent);
        return pow(term, k);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double m, k, n;
    if (cin >> m >> k >> n) {
        Solution solution;
        cout << fixed << setprecision(6) << solution.bloomFpr(m, k, n) << "\n";
    }
    return 0;
}
