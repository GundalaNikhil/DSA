#include <bits/stdc++.h>
using namespace std;

long long maxProfit(const vector<int>& prices, long long fee) {
    int n = (int)prices.size();
    const long long NEG = (long long)-4e18;
    long long buyable = 0, hold = NEG, ans = 0;
    vector<long long> unlock(n + 8, NEG);
    for (int i = 0; i < n; ++i) {
        if (unlock[i] != NEG) buyable = max(buyable, unlock[i]);
        long long prevHold = hold;
        hold = max(hold, buyable - prices[i]);
        if (prevHold != NEG) {
            long long sellProfit = prevHold + prices[i] - fee;
            ans = max(ans, sellProfit);
            int nextMonday = i - (i % 7) + 7;
            if (nextMonday < (int)unlock.size()) {
                unlock[nextMonday] = max(unlock[nextMonday], sellProfit);
            }
        }
    }
    if (hold != NEG) ans = max(ans, hold + prices.back() - fee);
    ans = max(ans, buyable);
    for (int i = n; i < (int)unlock.size(); ++i) ans = max(ans, unlock[i]);
    return ans;
}
