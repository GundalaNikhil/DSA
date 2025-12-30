#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string longestWildcardPalindrome(const string& s) {
        if (s.empty()) return "";
        
        string T = "^";
        for (char c : s) {
            T += "#";
            T += c;
        }
        T += "#$";
        
        int n = T.length();
        vector<int> P(n, 0);
        int C = 0, R = 0;
        
        for (int i = 1; i < n - 1; i++) {
            P[i] = (R > i) ? min(R - i, P[2 * C - i]) : 0;
            
            while (true) {
                char c1 = T[i + 1 + P[i]];
                char c2 = T[i - 1 - P[i]];
                
                bool match = false;
                if (c1 == '#' || c2 == '#') match = (c1 == c2);
                else if (c1 == '^' || c2 == '^' || c1 == '`' || c2 == '`') match = (c1 == c2);
                else match = (c1 == c2 || c1 == '?' || c2 == '?');
                
                if (match) P[i]++;
                else break;
            }
            
            if (i + P[i] > R) {
                C = i;
                R = i + P[i];
            }
        }
        
        int maxLen = 0;
        int centerIndex = 0;
        for (int i = 1; i < n - 1; i++) {
            if (P[i] > maxLen) {
                maxLen = P[i];
                centerIndex = i;
            }
        }
        
        int start = (centerIndex - maxLen) / 2;
        return s.substr(start, maxLen);
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
