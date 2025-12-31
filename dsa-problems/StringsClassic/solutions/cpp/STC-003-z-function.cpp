#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> zFunction(const string& s) {
        int n = s.length();
        if (n == 0) return {};
        vector<int> z(n);
        z[0] = n;
        
        int l = 0, r = 0;
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
        return z;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (cin >> s) {
        Solution solution;
        vector<int> z = solution.zFunction(s);
        for (int i = 0; i < (int)z.size(); i++) {
            if (i > 0) cout << " ";
            cout << z[i];
        }
        cout << "\n";
    }
    return 0;
}
