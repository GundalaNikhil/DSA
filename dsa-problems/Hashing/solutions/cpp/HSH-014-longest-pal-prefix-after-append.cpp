#include <iostream>
#include <string>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 313;

public:
    int longestPalindromicPrefix(string s, char c) {
        string T = s + c;
        int n = T.length();

        long long fwdHash = 0;
        long long revHash = 0;
        long long power = 1;

        int maxLen = 0;

        for (int i = 0; i < n; i++) {
            long long val = T[i];

            fwdHash = (fwdHash * BASE + val) % MOD;
            revHash = (revHash + val * power) % MOD;

            if (fwdHash == revHash) {
                maxLen = i + 1;
            }

            power = (power * BASE) % MOD;
        }

        return maxLen;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    char c;
    if (getline(cin, s) && cin >> c) {
        Solution solution;
        cout << solution.longestPalindromicPrefix(s, c) << "\n";
    }

    return 0;
}
