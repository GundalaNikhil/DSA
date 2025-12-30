#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

class Solution {
public:
    double kmvEstimate(const vector<double>& hashes) {
        int k = hashes.size();
        if (k == 0) return 0.0;
        double hk = hashes.back();
        return (double)(k - 1) / hk;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (cin >> k) {
        vector<double> hashes(k);
        for (int i = 0; i < k; i++) cin >> hashes[i];
    
        Solution solution;
        cout << fixed << setprecision(6) << solution.kmvEstimate(hashes) << "\n";
    }
    return 0;
}
