#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    double expectedSteps(int a, int b, double p) {
        if (abs(p - 0.5) < 1e-9) {
            return (double)a * b;
        }

        double q = 1.0 - p;
        double r = q / p;
        double M = a + b;
        double z = b;

        double term1 = z / (q - p);
        double term2 = (M / (q - p)) * ((1.0 - pow(r, z)) / (1.0 - pow(r, M)));

        return term1 - term2;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b;
    double p;
    if (cin >> a >> b >> p) {
        Solution solution;
        cout << fixed << setprecision(6) << solution.expectedSteps(a, b, p) << "\n";
    }
    return 0;
}
