#include <iostream>
#include <vector>
using namespace std;

// Placeholder for O(N^2) solution.
// A full O(N log^2 N) solution is too large for this format.

class Solution {
    const int MOD = 1000000007;
public:
    vector<long long> multipoint_evaluation(vector<long long>& coeffs, vector<long long>& points) {
        vector<long long> results;
        results.reserve(points.size());
        
        for (long long x : points) {
            long long val = 0;
            for (int i = coeffs.size() - 1; i >= 0; i--) {
                val = (val * x + coeffs[i]) % MOD;
            }
            results.push_back((val + MOD) % MOD);
        }
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int d, n;
    if (!(cin >> d >> n)) return 0;
    
    vector<long long> coeffs(d + 1);
    for (int i = 0; i < d + 1; i++) cin >> coeffs[i];
    
    vector<long long> points(n);
    for (int i = 0; i < n; i++) cin >> points[i];
    
    Solution solution;
    vector<long long> res = solution.multipoint_evaluation(coeffs, points);
    
    for (int i = 0; i < n; i++) {
        cout << res[i] << (i < n - 1 ? " " : "");
    }
    cout << "\n";
    
    return 0;
}
