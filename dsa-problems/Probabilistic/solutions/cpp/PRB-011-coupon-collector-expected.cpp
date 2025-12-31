#include <iostream>
#include <iomanip>

using namespace std;

class Solution {
public:
    double expectedDraws(int N) {
        double harmonicSum = 0.0;
        for (int i = 1; i <= N; i++) {
            harmonicSum += 1.0 / i;
        }
        return N * harmonicSum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (cin >> N) {
        Solution solution;
        cout << fixed << setprecision(6) << solution.expectedDraws(N) << "\n";
    }
    return 0;
}
