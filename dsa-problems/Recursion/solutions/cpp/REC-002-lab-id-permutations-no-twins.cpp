#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> generatePermutations(string s) {
        vector<string> result;
        sort(s.begin(), s.end());
        string current;
        vector<bool> used(s.length(), false);
        backtrack(s, used, current, result);
        return result;
    }

private:
    void backtrack(const string& s, vector<bool>& used, string& current, vector<string>& result) {
        if (current.length() == s.length()) {
            result.push_back(current);
            return;
        }

        for (int i = 0; i < s.length(); ++i) {
            if (used[i]) continue;

            // Skip duplicates
            if (i > 0 && s[i] == s[i - 1] && !used[i - 1]) continue;

            // Constraint: No adjacent twins
            if (!current.empty() && current.back() == s[i]) continue;

            used[i] = true;
            current.push_back(s[i]);
            backtrack(s, used, current, result);
            current.pop_back();
            used[i] = false;
        }
    }
};
