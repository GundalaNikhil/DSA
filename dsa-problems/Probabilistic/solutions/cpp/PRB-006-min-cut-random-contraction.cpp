#include <iostream>
#include <cmath>

using namespace std;

class Solution {
public:
    long long minTrials(long long n, double P) {
        if (n < 2) return 0;
        
        double pSuccess = 2.0 / (n * (n - 1.0));
        
        double numerator = log(1.0 - P);
        double denominator = log(1.0 - pSuccess);
        
        return (long long)ceil(numerator / denominator);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    double P;
    if (cin >> n >> P) {
        Solution solution;
        cout << solution.minTrials(n, P) << "\n";
    }
    return 0;
}
