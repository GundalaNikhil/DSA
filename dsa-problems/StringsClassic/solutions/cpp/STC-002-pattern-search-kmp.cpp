#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> findOccurrences(const string& p, const string& t) {
        int m = p.length();
        int n = t.length();
        if (m == 0) return {};
        
        // Compute prefix function
        vector<int> pi(m, 0);
        int j = 0;
        for (int i = 1; i < m; i++) {
            while (j > 0 && p[i] != p[j]) {
                j = pi[j - 1];
            }
            if (p[i] == p[j]) {
                j++;
            }
            pi[i] = j;
        }
        
        // Search
        vector<int> matches;
        j = 0;
        for (int i = 0; i < n; i++) {
            while (j > 0 && t[i] != p[j]) {
                j = pi[j - 1];
            }
            if (t[i] == p[j]) {
                j++;
            }
            if (j == m) {
                matches.push_back(i - m + 1);
                j = pi[j - 1];
            }
        }
        return matches;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string p, t;
    if (cin >> p >> t) {
        Solution solution;
        vector<int> result = solution.findOccurrences(p, t);
        for (int i = 0; i < (int)result.size(); i++) {
            if (i > 0) cout << " ";
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
