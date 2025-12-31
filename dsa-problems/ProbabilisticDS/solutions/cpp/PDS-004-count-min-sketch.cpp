#include <iostream>
#include <cmath>

using namespace std;

class Solution {
public:
    pair<long long, long long> cmsParams(double epsilon, double delta) {
        long long w = (long long) ceil(exp(1.0) / epsilon);
        long long d = (long long) ceil(log(1.0 / delta));
        return {w, d};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    double epsilon, delta;
    if (cin >> epsilon >> delta) {
        Solution solution;
        auto res = solution.cmsParams(epsilon, delta);
        cout << res.first << " " << res.second << "\n";
    }
    return 0;
}
