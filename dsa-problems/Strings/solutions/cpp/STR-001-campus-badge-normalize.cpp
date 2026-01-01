#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
using namespace std;

#include <algorithm>
#include <string>
#include <vector>
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
    string s((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());
    while(!s.empty() && isspace(s.back())) s.pop_back();
    while(!s.empty() && isspace(s.front())) s.erase(0, 1);
    Solution sol;
    cout << sol.normalizeBadge(s) << endl;
    return 0;
}
