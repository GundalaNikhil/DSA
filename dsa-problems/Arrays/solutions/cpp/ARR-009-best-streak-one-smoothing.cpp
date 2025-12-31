#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <climits>
using namespace std;

class Solution {
public:
    long long bestStreakWithSmoothing(vector<long long>& a) {
        int n = a.size();
        if (n < 3) return 0;

        vector<long long> maxEndingAt(n);
        vector<long long> globalMaxPrefix(n);

        maxEndingAt[0] = a[0];
        globalMaxPrefix[0] = a[0];
        for (int i = 1; i < n; i++) {
            maxEndingAt[i] = max((long long)a[i], maxEndingAt[i - 1] + a[i]);
            globalMaxPrefix[i] = max(globalMaxPrefix[i - 1], maxEndingAt[i]);
        }

        vector<long long> maxStartingAt(n);
        vector<long long> globalMaxSuffix(n);

        maxStartingAt[n - 1] = a[n - 1];
        globalMaxSuffix[n - 1] = a[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            maxStartingAt[i] = max((long long)a[i], maxStartingAt[i + 1] + a[i]);
            globalMaxSuffix[i] = max(globalMaxSuffix[i + 1], maxStartingAt[i]);
        }

        long long ans = LLONG_MIN;

        for (int i = 1; i < n - 1; i++) {
            long long smoothedVal = (long long)floor((double)(a[i - 1] + a[i] + a[i + 1]) / 3.0);

            long long leftPart = max(0LL, maxEndingAt[i - 1]);
            long long rightPart = max(0LL, maxStartingAt[i + 1]);
            long long crossSum = leftPart + smoothedVal + rightPart;

            long long globalLeft = globalMaxPrefix[i - 1];
            long long globalRight = globalMaxSuffix[i + 1];

            long long currentBest = max({crossSum, globalLeft, globalRight});
            ans = max(ans, currentBest);
        }

        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    Solution solution;
    cout << solution.bestStreakWithSmoothing(a) << "\n";
    return 0;
}
