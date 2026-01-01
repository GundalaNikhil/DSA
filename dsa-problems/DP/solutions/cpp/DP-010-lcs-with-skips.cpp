#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <numeric>
#include <limits>
#include <cmath>
#include <cstring>
#include <utility>
using namespace std;

class Solution {
public:
    int lcsWithSkipLimit(const string& a, const string& b, int s) {
        int n = (int)a.size(), m = (int)b.size();
        vector<int> prev(m + 1, 0), cur(m + 1, 0);

        for (int i = 1; i <= n; i++) {
            cur[0] = 0;
            char ai = a[i - 1];
            for (int j = 1; j <= m; j++) {
                if (ai == b[j - 1]) cur[j] = prev[j - 1] + 1;
                else cur[j] = max(prev[j], cur[j - 1]);
            }
            prev.swap(cur);
        }

        int L = prev[m];
        return (n - L <= s) ? L : -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    getline(cin, a);
    getline(cin, b);
    int s;
    cin >> s;
    Solution sol;
    cout << sol.lcsWithSkipLimit(a, b, s) << '\n';
    return 0;
}
