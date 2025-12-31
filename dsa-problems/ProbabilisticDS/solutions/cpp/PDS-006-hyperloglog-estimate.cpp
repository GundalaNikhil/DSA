#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    double hllEstimate(int m, const vector<int>& registers) {
        double alpha;
        if (m == 16) alpha = 0.673;
        else if (m == 32) alpha = 0.697;
        else if (m == 64) alpha = 0.709;
        else alpha = 0.7213 / (1.0 + 1.079 / (double)m);
        
        double sum = 0.0;
        int zeros = 0;
        for (int val : registers) {
            sum += pow(2.0, -val);
            if (val == 0) zeros++;
        }
        
        double E = alpha * (double)m * m / sum;
        
        if (E <= 2.5 * m) {
            if (zeros > 0) {
                E = (double)m * log((double)m / zeros);
            }
        }
        
        return E;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    if (cin >> m) {
        vector<int> registers(m);
        for (int i = 0; i < m; i++) cin >> registers[i];
    
        Solution solution;
        cout << fixed << setprecision(6) << solution.hllEstimate(m, registers) << "\n";
    }
    return 0;
}
