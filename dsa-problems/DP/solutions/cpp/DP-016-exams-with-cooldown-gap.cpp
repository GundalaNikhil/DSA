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

struct Exam { long long s, e, w; };

long long maxScore(vector<Exam>& exams, long long g) {
    sort(exams.begin(), exams.end(), [](const Exam& a, const Exam& b){ return a.e < b.e; });
    int n = exams.size();
    vector<long long> ends(n);
    for (int i = 0; i < n; ++i) ends[i] = exams[i].e;
    vector<long long> dp(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        const auto& ex = exams[i - 1];
        int j = upper_bound(ends.begin(), ends.end(), ex.s - g) - ends.begin();
        dp[i] = max(dp[i - 1], dp[j] + ex.w);
    }
    return dp[n];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; long long g;
    if (!(cin >> n >> g)) return 0;
    vector<Exam> exams(n);
    for (int i = 0; i < n; ++i) cin >> exams[i].s >> exams[i].e >> exams[i].w;
    cout << maxScore(exams, g) << '\n';
    return 0;
}
