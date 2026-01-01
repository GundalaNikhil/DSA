#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestWildcardPalindrome(const string& s) {
        int n = s.length();
        if (n == 0) return 0;

        int maxLen = 1;

        // Expand around each center (character and between characters)
        // 2*n - 1 centers
        for (int i = 0; i < 2 * n - 1; i++) {
            int l = i / 2;
            int r = (i + 1) / 2;

            int tempMismatch = 0;

            while (l >= 0 && r < n) {
                if (s[l] != s[r]) {
                    tempMismatch++;
                }

                if (tempMismatch > 1) {
                    break;
                }

                int length = r - l + 1;
                if (length > maxLen) {
                    maxLen = length;
                }

                l--;
                r++;
            }
        }

        return maxLen;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        Solution solution;
        cout << solution.longestWildcardPalindrome(s) << "\n";
    }
    return 0;
}
