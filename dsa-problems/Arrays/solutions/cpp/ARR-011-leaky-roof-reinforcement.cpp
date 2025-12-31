#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <climits>
using namespace std;

class Solution {
public:
    long long minPlanksForRoof(vector<int>& height) {
        int n = height.size();
        if (n == 0) return 0;

        vector<long long> L(n), SumL(n);
        L[0] = height[0];
        SumL[0] = height[0];
        for (int i = 1; i < n; i++) {
            L[i] = max((long long)height[i], L[i - 1]);
            SumL[i] = SumL[i - 1] + L[i];
        }

        vector<long long> R(n), SumR(n);
        R[n - 1] = height[n - 1];
        SumR[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            R[i] = max((long long)height[i], R[i + 1]);
            SumR[i] = SumR[i + 1] + R[i];
        }

        long long minTotalHeight = LLONG_MAX;
        for (int i = 0; i < n; i++) {
            long long currentTotal = SumL[i] + SumR[i] - min(L[i], R[i]);
            minTotalHeight = min(minTotalHeight, currentTotal);
        }

        long long originalSum = 0;
        for (int h : height) originalSum += h;

        return minTotalHeight - originalSum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> height(n);
    for (int i = 0; i < n; i++) cin >> height[i];

    Solution solution;
    cout << solution.minPlanksForRoof(height) << "\n";
    return 0;
}
