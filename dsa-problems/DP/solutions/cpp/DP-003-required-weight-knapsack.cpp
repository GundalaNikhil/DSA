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
    static constexpr long long NEG = (long long)-4e18;
public:
    long long maxValueWithRequiredWeight(int n, int W, int R,
                                         const vector<int>& w,
                                         const vector<long long>& v) {
        vector<long long> dp(W + 1, NEG);
        dp[0] = 0;

        for (int i = 0; i < n; i++) {
            for (int wt = W; wt >= w[i]; wt--) {
                if (dp[wt - w[i]] != NEG) {
                    dp[wt] = max(dp[wt], dp[wt - w[i]] + v[i]);
                }
            }
        }

        long long ans = NEG;
        for (int wt = R; wt <= W; wt++) ans = max(ans, dp[wt]);
        return ans == NEG ? -1 : ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, W, R;
    cin >> n >> W >> R;
    vector<int> w(n);
    vector<long long> v(n);
    for (int i = 0; i < n; i++) cin >> w[i] >> v[i];

    Solution sol;
    cout << sol.maxValueWithRequiredWeight(n, W, R, w, v) << '\n';
    return 0;
}
