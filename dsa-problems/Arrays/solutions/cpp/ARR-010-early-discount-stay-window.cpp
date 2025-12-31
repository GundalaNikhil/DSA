#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxProfitWithConstraints(vector<int>& prices, int dMin, int dMax, int C) {
        int n = prices.size();
        deque<int> dq; // Stores indices
        int maxProfit = 0;

        for (int j = dMin; j < n; j++) {
            // Valid buy index entering window
            int buyCandidate = j - dMin;

            while (!dq.empty() && prices[dq.back()] >= prices[buyCandidate]) {
                dq.pop_back();
            }
            dq.push_back(buyCandidate);

            // Remove expired
            if (!dq.empty() && dq.front() < j - dMax) {
                dq.pop_front();
            }

            int minBuyPrice = prices[dq.front()];
            int sellPrice = min(prices[j], C);
            maxProfit = max(maxProfit, sellPrice - minBuyPrice);
        }

        return maxProfit;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> prices(n);
    for (int i = 0; i < n; i++) cin >> prices[i];

    int dMin, dMax, C;
    cin >> dMin >> dMax >> C;

    Solution solution;
    cout << solution.maxProfitWithConstraints(prices, dMin, dMax, C) << "\n";
    return 0;
}
