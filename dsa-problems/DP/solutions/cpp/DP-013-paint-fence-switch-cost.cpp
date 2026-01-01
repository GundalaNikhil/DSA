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

long long minCost(int n, int k, const vector<int>& s) {
    if (k == 1) return n <= 2 ? n : -1;
    const long long INF = (long long)4e18;
    vector<long long> dp1(k, 1), dp2(k, INF);
    for (int i = 1; i < n; ++i) {
        long long min1 = INF, min2 = INF;
        int c1 = -1;
        for (int c = 0; c < k; ++c) {
            long long v = min(dp1[c], dp2[c]);
            if (v < min1) { min2 = min1; min1 = v; c1 = c; }
            else if (v < min2) { min2 = v; }
        }
        vector<long long> ndp1(k, INF), ndp2(k, INF);
        for (int c = 0; c < k; ++c) {
            if (dp1[c] < INF) ndp2[c] = dp1[c] + 1;
            long long bestOther = (c == c1) ? min2 : min1;
            if (bestOther < INF) ndp1[c] = bestOther + 1 + s[i];
        }
        dp1.swap(ndp1);
        dp2.swap(ndp2);
    }
    long long ans = *min_element(dp1.begin(), dp1.end());
    ans = min(ans, *min_element(dp2.begin(), dp2.end()));
    return ans >= INF ? -1 : ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<int> s(n);
    for (int i = 0; i < n; ++i) cin >> s[i];
    cout << minCost(n, k, s) << '\n';
    return 0;
}
