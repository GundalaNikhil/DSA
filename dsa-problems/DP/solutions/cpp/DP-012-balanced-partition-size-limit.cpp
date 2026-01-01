#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <numeric>
#include <limits>
#include <cmath>
#include <cstring>
#include <utility>
using namespace std;

class Solution {
public:
    int minLargerGroupSize(const vector<int>& a, int D) {
        int n = (int)a.size();
        int total = accumulate(a.begin(), a.end(), 0);
        vector<unordered_set<int>> dp(n + 1);
        dp[0].insert(0);

        for (int x : a) {
            for (int k = n - 1; k >= 0; k--) {
                vector<int> cur(dp[k].begin(), dp[k].end());
                for (int s : cur) dp[k + 1].insert(s + x);
            }
        }

        int ans = INT_MAX;
        for (int k = 0; k <= n; k++) {
            for (int s : dp[k]) {
                if (abs(total - 2 * s) <= D) {
                    ans = min(ans, max(k, n - k));
                }
            }
        }
        return ans == INT_MAX ? -1 : ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, D;
    cin >> n >> D;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    Solution sol;
    cout << sol.minLargerGroupSize(a, D) << '\n';
    return 0;
}
