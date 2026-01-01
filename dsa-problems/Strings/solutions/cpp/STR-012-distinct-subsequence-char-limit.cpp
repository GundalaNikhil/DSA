#include <iostream>
class Solution {
public:
    int countDistinctSubsequencesWithLimit(string s, int maxFreq, int MOD) {
        map<vector<int>, long long> dp;
        dp[vector<int>(26, 0)] = 1;

        for (char c : s) {
            int charIdx = c - 'a';
            map<vector<int>, long long> newDp;

            for (auto& [state, count] : dp) {
                // Don't include
                newDp[state] = (newDp[state] + count) % MOD;

                // Include if allowed
                if (state[charIdx] < maxFreq) {
                    vector<int> newState = state;
                    newState[charIdx]++;
                    newDp[newState] = (newDp[newState] + count) % MOD;
                }
            }

            dp = move(newDp);
        }

        long long total = 0;
        for (auto& [state, count] : dp) {
            total = (total + count) % MOD;
        }
        return total;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; cin >> s;
    int maxFreq; cin >> maxFreq;
    int MOD; cin >> MOD;
    Solution sol;
    cout << sol.countDistinctSubsequencesWithLimit(s, maxFreq, MOD) << endl;
    return 0;
}
