#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <climits>

using namespace std;

class Solution {
    long long maxDiff = 0;

    void dfs(int u, int depth, int minE, int maxE, int minO, int maxO,
             const vector<int>& values, const vector<int>& left, const vector<int>& right) {
        if (u == -1) return;

        int val = values[u];

        if (depth % 2 == 0) {
            // Even
            if (minO != INT_MAX) {
                maxDiff = max(maxDiff, (long long)abs(val - minO));
                maxDiff = max(maxDiff, (long long)abs(val - maxO));
            }
            minE = min(minE, val);
            maxE = max(maxE, val);
        } else {
            // Odd
            if (minE != INT_MAX) {
                maxDiff = max(maxDiff, (long long)abs(val - minE));
                maxDiff = max(maxDiff, (long long)abs(val - maxE));
            }
            minO = min(minO, val);
            maxO = max(maxO, val);
        }

        if (left[u] != -1) dfs(left[u], depth + 1, minE, maxE, minO, maxO, values, left, right);
        if (right[u] != -1) dfs(right[u], depth + 1, minE, maxE, minO, maxO, values, left, right);
    }

public:
    long long maxOppositeParityGap(int n, const vector<int>& values,
                                   const vector<int>& left, const vector<int>& right) {
        if (n == 0) return 0;
        maxDiff = 0;
        // Root is depth 0 (Even).
        dfs(0, 0, values[0], values[0], INT_MAX, INT_MIN, values, left, right);
        return maxDiff;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> left[i] >> right[i];
    }

    Solution solution;
    cout << solution.maxOppositeParityGap(n, values, left, right) << "\n";
    return 0;
}
