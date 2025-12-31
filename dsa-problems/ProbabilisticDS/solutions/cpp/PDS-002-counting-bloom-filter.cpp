#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    double overflowProbability(int m, int k, int c, int n) {
        double lambda = (double)k * n / m;
        long long maxVal = (1LL << c) - 1;
        
        double term = exp(-lambda);
        double sum = term;
        
        for (int i = 1; i <= maxVal; i++) {
            term *= (lambda / i);
            sum += term;
        }
        
        return 1.0 - sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m, k, c, n;
    if (cin >> m >> k >> c >> n) {
        Solution solution;
        cout << fixed << setprecision(15) << solution.overflowProbability(m, k, c, n) << "\n";
    }
    return 0;
}
