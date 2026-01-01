#include <iostream>
#include <string>
#include <vector>

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

    string data((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());
    if (data.empty()) {
        return 0;
    }
    vector<string> lines;
    string cur;
    for (char ch : data) {
        if (ch == '\n') {
            lines.push_back(cur);
            cur.clear();
        } else if (ch != '\r') {
            cur.push_back(ch);
        }
    }
    lines.push_back(cur);

    string s;
    string cstr;
    if (lines.size() == 1) {
        s = "";
        cstr = lines[0];
    } else {
        s = lines[0];
        for (size_t i = 1; i < lines.size(); i++) {
            if (!lines[i].empty()) {
                cstr = lines[i];
                break;
            }
        }
        if (cstr.empty()) {
            cstr = lines[1];
        }
    }
    if (cstr.empty()) {
        return 0;
    }
    char c = cstr[0];
    Solution solution;
    cout << solution.longestPalindromicPrefix(s, c) << "\n";

    return 0;
}
