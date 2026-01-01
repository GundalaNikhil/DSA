#include <iostream>
class Solution {
public:
    int countEqualDistinctSplits(string s) {
        int n = s.size();
        if (n < 2) return 0;

        // Build suffix distinct counts
        vector<int> suffixDistinct(n + 1, 0);
        unordered_set<char> charSet;
        for (int i = n - 1; i >= 0; i--) {
            charSet.insert(s[i]);
            suffixDistinct[i] = charSet.size();
        }

        // Scan left and compare
        unordered_set<char> leftSet;
        int count = 0;
        for (int i = 0; i < n - 1; i++) {
            leftSet.insert(s[i]);
            if ((int)leftSet.size() == suffixDistinct[i + 1]) {
                count++;
            }
        }

        return count;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s; cin >> s;
    Solution sol;
    cout << sol.countEqualDistinctSplits(s) << endl;
    return 0;
}
