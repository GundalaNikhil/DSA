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
    long long maxSumGapThree(const vector<long long>& a) {
        long long dp_i_3 = 0, dp_i_2 = 0, dp_i_1 = 0;
        for (long long x : a) {
            long long cur = max(dp_i_1, x + dp_i_3);
            dp_i_3 = dp_i_2;
            dp_i_2 = dp_i_1;
            dp_i_1 = cur;
        }
        return dp_i_1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    Solution sol;
    cout << sol.maxSumGapThree(a) << '\n';
    return 0;
}
