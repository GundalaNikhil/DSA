#include <bits/stdc++.h>
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
