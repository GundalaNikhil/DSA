#include <iostream>
#include <iomanip>

using namespace std;

class Solution {
public:
    double solve(int n) {
        double h = 0.0;
        for (int i = 1; i <= n; i++) {
            h += 1.0 / i;
        }
        return h;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        Solution solution;
        cout << fixed << setprecision(6) << solution.solve(n) << "\n";
    }
    return 0;
}
