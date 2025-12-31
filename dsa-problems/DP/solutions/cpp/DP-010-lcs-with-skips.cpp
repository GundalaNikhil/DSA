#include <bits/stdc++.h>
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
