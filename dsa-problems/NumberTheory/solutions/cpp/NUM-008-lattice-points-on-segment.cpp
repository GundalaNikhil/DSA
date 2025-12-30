#include <iostream>
#include <numeric>
#include <cmath>

using namespace std;

class Solution {
    long long gcd(long long a, long long b) {
        while (b) {
            a %= b;
            swap(a, b);
        }
        return a;
    }

public:
    long long latticePoints(long long x1, long long y1, long long x2, long long y2) {
        long long dx = abs(x1 - x2);
        long long dy = abs(y1 - y2);
        return gcd(dx, dy) + 1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long x1, y1, x2, y2;
    if (cin >> x1 >> y1 >> x2 >> y2) {
        Solution solution;
        cout << solution.latticePoints(x1, y1, x2, y2) << "\n";
    }
    return 0;
}
