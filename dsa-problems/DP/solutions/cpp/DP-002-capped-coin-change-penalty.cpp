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
    static constexpr long long INF = (1LL<<62);
public:
    long long minCost(int k, int target, const vector<int>& d,
                      const vector<long long>& c, const vector<long long>& p) {
        vector<long long> dp(target + 1, INF);
        dp[0] = 0;

        for (int i = 0; i < k; i++) {
            int denom = d[i];
            int cap = (int)min<long long>(c[i], target / (long long)denom);
            int t = (int)min<long long>(c[i] / 2LL, cap);
            long long penalty = p[i];

            vector<long long> nxt(target + 1, INF);

            for (int r = 0; r < denom; r++) {
                int qMax = (target - r) / denom;
                if (qMax < 0) continue;

                int L1 = min(cap, t);
                deque<int> dqNo, dqPen;

                auto key = [&](int q) -> long long {
                    long long val = dp[r + q * denom];
                    return val - (long long)q;
                };

                for (int q = 0; q <= qMax; q++) {
                    int sQ = r + q * denom;

                    if (dp[sQ] < INF) {
                        long long kv = key(q);
                        while (!dqNo.empty() && kv <= key(dqNo.back())) dqNo.pop_back();
                        dqNo.push_back(q);
                    }

                    int minY = q - L1;
                    while (!dqNo.empty() && dqNo.front() < minY) dqNo.pop_front();

                    long long best = INF;
                    if (!dqNo.empty()) best = min(best, (long long)q + key(dqNo.front()));

                    if (cap > t) {
                        int yAdd = q - (t + 1);
                        if (yAdd >= 0) {
                            int sAdd = r + yAdd * denom;
                            if (dp[sAdd] < INF) {
                                long long kv = key(yAdd);
                                while (!dqPen.empty() && kv <= key(dqPen.back())) dqPen.pop_back();
                                dqPen.push_back(yAdd);
                            }
                        }

                        int minYPen = q - cap;
                        while (!dqPen.empty() && dqPen.front() < minYPen) dqPen.pop_front();

                        if (!dqPen.empty()) best = min(best, (long long)q + penalty + key(dqPen.front()));
                    }

                    int s = r + q * denom;
                    nxt[s] = min(nxt[s], best);
                }
            }

            dp.swap(nxt);
        }

        return dp[target] >= INF ? -1 : dp[target];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k, target;
    cin >> k >> target;
    vector<int> d(k);
    vector<long long> c(k), p(k);
    for (int i = 0; i < k; i++) cin >> d[i] >> c[i] >> p[i];

    Solution sol;
    cout << sol.minCost(k, target, d, c, p) << '\n';
    return 0;
}
