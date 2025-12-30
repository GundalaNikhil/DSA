#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    long long minTrials(long long n, double C) {
        double p = 1.0 / ((double)n * n);
        
        double num = log(1.0 - C);
        double den = log(1.0 - p);
        
        return (long long) ceil(num / den);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    double C;
    if (cin >> n >> C) {
        Solution solution;
        cout << solution.minTrials(n, C) << "\n";
    }
    return 0;
}
