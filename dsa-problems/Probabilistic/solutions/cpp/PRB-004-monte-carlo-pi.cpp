#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>

using namespace std;

class Solution {
public:
    class LCG {
        unsigned int state;
    public:
        LCG(unsigned int seed) : state(seed) {}
        double nextFloat() {
            state = (state * 1664525 + 1013904223);
            return state / 4294967296.0;
        }
    };

    pair<double, double> estimatePi(long long N, long long seed) {
        LCG rng(seed);
        long long count_inside = 0;
        
        for (long long i = 0; i < N; i++) {
            double x = rng.nextFloat();
            double y = rng.nextFloat();
            if (x * x + y * y <= 1.0) {
                count_inside++;
            }
        }
        
        double pHat = (double)count_inside / N;
        double piHat = 4.0 * pHat;
        
        double error = 0.0;
        if (N > 0) {
            double stdErrP = sqrt(pHat * (1.0 - pHat) / N);
            error = 1.96 * stdErrP * 4.0;
        }
        return {piHat, error};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, C;
    if (cin >> N >> C) {
        Solution solution;
        auto res = solution.estimatePi(N, C);
        cout << fixed << setprecision(6) << res.first << " " << res.second << "\n";
    }
    return 0;
}
