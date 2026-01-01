#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool canRotateToPalindrome(string s) {
        if (s.empty()) return true;
        int n = s.length();
        string doubled = s + s;
        
        for (int i = 0; i < n; i++) {
            // Check substring of length n starting at i
            string rotated = doubled.substr(i, n);
            string reversed = rotated;
            reverse(reversed.begin(), reversed.end());
            if (rotated == reversed) {
                return true;
            }
        }
        return false;
    }
};








int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    string s((istreambuf_iterator<char>(cin)), istreambuf_iterator<char>());
    while(!s.empty() && isspace(s.back())) s.pop_back();
    while(!s.empty() && isspace(s.front())) s.erase(0, 1);
    Solution sol;
    cout << (sol.canRotateToPalindrome(s) ? "true" : "false") << endl;
    return 0;
}
