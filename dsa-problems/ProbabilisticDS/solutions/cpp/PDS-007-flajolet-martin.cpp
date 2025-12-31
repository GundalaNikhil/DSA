#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    double estimateDistinct(int R) {
        return pow(2.0, R) / 0.77351;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R;
    if (cin >> R) {
        Solution solution;
        cout << fixed << setprecision(6) << solution.estimateDistinct(R) << "\n";
    }
    return 0;
}
