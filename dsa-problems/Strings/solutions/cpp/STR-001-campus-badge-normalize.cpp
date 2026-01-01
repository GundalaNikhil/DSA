#include <iostream>
class Solution {
public:
    string normalizeBadge(string s) {
        if (s.empty()) return "";

        string result;
        result.reserve(s.size());
        bool lastWasAlnum = false;

        for (char c : s) {
            if (isalnum(c)) {
                result += tolower(c);
                lastWasAlnum = true;
            } else {
                // Non-alphanumeric character
                if (lastWasAlnum && !result.empty()) {
                    result += '-';
                    lastWasAlnum = false;
                }
            }
        }

        // Remove trailing hyphen if present
        if (!result.empty() && result.back() == '-') {
            result.pop_back();
        }

        return result;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; cin >> s;
    Solution sol;
    cout << sol.normalizeBadge(s) << endl;
    return 0;
}
