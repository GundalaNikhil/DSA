#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

class Solution {
    bool isVowel(char c) {
        return string("aeiou").find(c) != string::npos;
    }
public:
    pair<int, string> longestAlternatingVC(string s) {
        if (s.empty()) return {0, ""};

        int maxLen = 1;
        int bestStart = 0;
        int currentLen = 1;
        int start = 0;
        bool prevIsVowel = isVowel(s[0]);

        for (int i = 1; i < s.length(); i++) {
            bool currIsVowel = isVowel(s[i]);
            if (currIsVowel != prevIsVowel) {
                currentLen++;
                if (currentLen > maxLen) {
                    maxLen = currentLen;
                    bestStart = start;
                }
            } else {
                start = i;
                currentLen = 1;
            }
            prevIsVowel = currIsVowel;
        }

        return {maxLen, s.substr(bestStart, maxLen)};
    }
};











int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());
    while(!s.empty() && isspace(s.back())) s.pop_back();
    while(!s.empty() && isspace(s.front())) s.erase(0, 1);
    Solution sol;
    pair<int, string> res = sol.longestAlternatingVC(s); cout << res.first << endl; cout << res.second << endl;
    return 0;
}
