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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; long long fee;
    if (!(cin >> n >> fee)) return 0;
    vector<int> prices(n);
    for (int i = 0; i < n; ++i) cin >> prices[i];
    cout << maxProfit(prices, fee) << '\n';
    return 0;
}
