#include <iostream>
class Solution {
private:
    string dfs(string current, int remaining, unordered_set<string>& substrings) {
        if (remaining == 0) {
            return substrings.count(current) ? "" : current;
        }

        for (char c = 'a'; c <= 'z'; c++) {
            current += c;
            string result = dfs(current, remaining - 1, substrings);
            if (!result.empty()) {
                return result;
            }
            current.pop_back(); // backtrack
        }

        return "";
    }

public:
    string smallestMissingSubstring(string s, int k) {
        // Extract all k-length substrings
        unordered_set<string> substrings;
        for (int i = 0; i <= (int)s.size() - k; i++) {
            substrings.insert(s.substr(i, k));
        }

        return dfs("", k, substrings);
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; cin >> s;
    int k; cin >> k;
    Solution sol;
    cout << sol.smallestMissingSubstring(s, k) << endl;
    return 0;
}
