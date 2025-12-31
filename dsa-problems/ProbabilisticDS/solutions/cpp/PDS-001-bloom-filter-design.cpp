#include <iostream>
#include <cmath>
#include <iomanip>
#include <tuple>

using namespace std;

class Solution {
public:
    tuple<long long, long long, double> designBloom(long long n, double f) {
        double ln2 = log(2);
        
        double mDouble = -(n * log(f)) / (ln2 * ln2);
        long long m = (long long) ceil(mDouble);
        
        double kDouble = (m / (double)n) * ln2;
        long long k = (long long) round(kDouble);
        
        double exponent = -((double)k * n) / m;
        double fpr = pow(1.0 - exp(exponent), k);
        
        return make_tuple(m, k, fpr);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    double f;
    if (cin >> n >> f) {
        Solution solution;
        auto res = solution.designBloom(n, f);
        cout << get<0>(res) << " " << get<1>(res) << " " << fixed << setprecision(6) << get<2>(res) << "\n";
    }
    return 0;
}
