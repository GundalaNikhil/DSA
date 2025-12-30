#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>

using namespace std;

class Solution {
public:
    double hllUnionEstimate(int m, const vector<int>& a, const vector<int>& b) {
        double alpha;
        if (m == 16) alpha = 0.673;
        else if (m == 32) alpha = 0.697;
        else if (m == 64) alpha = 0.709;
        else alpha = 0.7213 / (1.0 + 1.079 / (double)m);
        
        double sum = 0.0;
        for (int i = 0; i < m; i++) {
            int val = max(a[i], b[i]);
            sum += pow(2.0, -val);
        }
        
        return alpha * (double)m * m / sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    if (cin >> m) {
        vector<int> a(m), b(m);
        for (int i = 0; i < m; i++) cin >> a[i];
        for (int i = 0; i < m; i++) cin >> b[i];
    
        Solution solution;
        cout << fixed << setprecision(6) << solution.hllUnionEstimate(m, a, b) << "\n";
    }
    return 0;
}
