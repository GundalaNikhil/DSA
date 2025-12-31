#include <bits/stdc++.h>
using namespace std;

class Solution {
    static const int MOD = 1'000'000'007;
public:
    int countExpressions(const string& s, int M, int K, int L) {
        int n = (int)s.size();
        vector<vector<array<int,2>>> dp(n+1, vector<array<int,2>>(M, {0,0}));

        for (int len=1; len<=L && len<=n; len++) {
            if (s[0]=='0' && len>1) break;
            int val = stoi(s.substr(0,len)) % M;
            dp[len][val][0] = (dp[len][val][0] + 1) % MOD;
        }

        for (int pos=1; pos<n; pos++) {
            for (int rem=0; rem<M; rem++) {
                for (int used=0; used<=1; used++) {
                    int ways = dp[pos][rem][used];
                    if (!ways) continue;
                    for (int len=1; len<=L && pos+len<=n; len++) {
                        if (s[pos]=='0' && len>1) break;
                        int val = stoi(s.substr(pos,len));
                        int addRem = ((rem + val)%M + M)%M;
                        int subRem = ((rem - val)%M + M)%M;
                        dp[pos+len][addRem][used] = (dp[pos+len][addRem][used] + ways) % MOD;
                        dp[pos+len][subRem][1] = (dp[pos+len][subRem][1] + ways) % MOD;
                    }
                }
            }
        }
        return dp[n][K][1];
    }
};
