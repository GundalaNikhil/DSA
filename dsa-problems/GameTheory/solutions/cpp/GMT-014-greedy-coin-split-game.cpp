#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
    int dp[105][105];
    bool visited[105][105];
    vector<int> prefixSum;

    int getSum(int i, int j) {
        return prefixSum[j + 1] - prefixSum[i];
    }

    int solve(int i, int j) {
        if (i == j) return 0;
        if (visited[i][j]) return dp[i][j];

        int maxDiff = INT_MIN;

        for (int k = i; k < j; k++) {
            int sumLeft = getSum(i, k);
            int sumRight = getSum(k + 1, j);

            int valTakeLeft = -sumLeft - solve(k + 1, j);
            int valTakeRight = -sumRight - solve(i, k);

            int outcome = min(valTakeLeft, valTakeRight);
            maxDiff = max(maxDiff, outcome);
        }

        visited[i][j] = true;
        return dp[i][j] = maxDiff;
    }

public:
    int coinSplit(int n, vector<int>& A) {
        prefixSum.assign(n + 1, 0);
        for (int i = 0; i < n; i++) prefixSum[i + 1] = prefixSum[i] + A[i];
        
        for(int i=0; i<n; ++i)
            for(int j=0; j<n; ++j)
                visited[i][j] = false;

        return solve(0, n - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<int> A(n);
        for (int i = 0; i < n; i++) {
            cin >> A[i];
        }
        
        Solution solution;
        cout << solution.coinSplit(n, A) << "\n";
    }
    return 0;
}
