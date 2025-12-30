#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

class Solution {
public:
    double expectedComparisons(int n, int k) {
        // dp[i][j] stores E(i, j)
        vector<vector<double>> dp(n + 1, vector<double>(n + 1, 0.0));
        vector<vector<double>> colSum(n + 1, vector<double>(n + 1, 0.0));
        vector<vector<double>> diagSum(n + 1, vector<double>(n + 1, 0.0));
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                double total = 0.0;
                
                if (i - 1 >= j) {
                    total += colSum[j][i - 1] - colSum[j][j - 1];
                }
                
                int d = i - j;
                if (j > 1) {
                    total += diagSum[d][i - 1];
                }
                
                dp[i][j] = (i - 1) + total / i;
                
                colSum[j][i] = colSum[j][i - 1] + dp[i][j];
                diagSum[d][i] = diagSum[d][i - 1] + dp[i][j];
            }
        }
        
        return dp[n][k];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (cin >> n >> k) {
        Solution solution;
        cout << fixed << setprecision(6) << solution.expectedComparisons(n, k) << "\n";
    }
    return 0;
}
