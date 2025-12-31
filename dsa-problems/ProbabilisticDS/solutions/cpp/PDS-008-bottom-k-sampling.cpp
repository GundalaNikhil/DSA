#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

class Solution {
public:
    double jaccardEstimate(const vector<double>& a, const vector<double>& b) {
        int matches = 0;
        for (size_t i = 0; i < a.size(); i++) {
            if (a[i] == b[i]) {
                matches++;
            }
        }
        return (double)matches / a.size();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (cin >> k) {
        vector<double> a(k), b(k);
        for (int i = 0; i < k; i++) cin >> a[i];
        for (int i = 0; i < k; i++) cin >> b[i];
    
        Solution solution;
        cout << fixed << setprecision(6) << solution.jaccardEstimate(a, b) << "\n";
    }
    return 0;
}
