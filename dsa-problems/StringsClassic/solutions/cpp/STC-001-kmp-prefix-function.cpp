#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> prefixFunction(const string& s) {
        int n = s.length();
        vector<int> pi(n, 0);
        int j = 0; // length of the previous longest prefix
        
        for (int i = 1; i < n; i++) {
            // Backtrack
            while (j > 0 && s[i] != s[j]) {
                j = pi[j - 1];
            }
            // Extend
            if (s[i] == s[j]) {
                j++;
            }
            pi[i] = j;
        }
        return pi;
    }
};

int main() {
    // Fast I/O
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        Solution solution;
        vector<int> pi = solution.prefixFunction(s);
        
        for (int i = 0; i < (int)pi.size(); i++) {
            if (i > 0) cout << " ";
            cout << pi[i];
        }
        cout << "\n";
    }
    return 0;
}
