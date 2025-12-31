#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    double decayedDistinct(int T, double lambda, const vector<int>& times) {
        double sum = 0.0;
        for (int t : times) {
            sum += exp(-lambda * (T - t));
        }
        return sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T, m;
    double lambda;
    if (cin >> T >> lambda >> m) {
        vector<int> times(m);
        for (int i = 0; i < m; i++) cin >> times[i];
    
        Solution solution;
        cout << fixed << setprecision(6) << solution.decayedDistinct(T, lambda, times) << "\n";
    }
    return 0;
}
