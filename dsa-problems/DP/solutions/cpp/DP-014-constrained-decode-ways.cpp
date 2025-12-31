#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1'000'000'007LL;

long long decodeWays(const string& s) {
    int n = s.size();
    if (n == 0 || s[0] == '0') return 0;
    long long prev2 = 1, prev1 = 1;
    for (int i = 1; i < n; ++i) {
        int pair = (s[i - 1] - '0') * 10 + (s[i] - '0');
        long long cur = 0;
        if (s[i] != '0') {
            cur = (cur + prev1) % MOD;
            if (pair == 20 || (pair > 10 && pair <= 26)) cur = (cur + prev2) % MOD;
        } else {
            if (pair == 20) cur = (cur + prev2) % MOD;
        }
        prev2 = prev1;
        prev1 = cur;
    }
    return prev1 % MOD;
}
