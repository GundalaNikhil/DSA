#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> findOccurrences(const string& p, const string& t) {
        string s = p + "#" + t;
        int n = s.length();
        vector<int> z(n);
        int l = 0, r = 0;
        
        // Compute Z-array
        for (int i = 1; i < n; i++) {
            if (i <= r) {
                z[i] = min(r - i + 1, z[i - l]);
            }
            while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
                z[i]++;
            }
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
        
        // Collect matches
        vector<int> matches;
        int pLen = p.length();
        for (int i = pLen + 1; i < n; i++) {
            if (z[i] == pLen) {
                matches.push_back(i - (pLen + 1));
            }
        }
        return matches;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string t, p;
    if (cin >> t >> p) {
        Solution solution;
        vector<int> result = solution.findOccurrences(p, t);
        if (result.empty()) {
            cout << "-1\n";
        } else {
            for (int i = 0; i < (int)result.size(); i++) {
                if (i > 0) cout << " ";
                cout << result[i];
            }
            cout << "\n";
        }
    }
    return 0;
}
