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
    string row1 = "qwertyuiop";
    string row2 = "asdfghjkl";
    string left = "qwertasdfgzxcvb";

    int row(char c) {
        if (row1.find(c) != string::npos) return 1;
        if (row2.find(c) != string::npos) return 2;
        return 3;
    }

    int hand(char c) {
        return left.find(c) != string::npos ? 0 : 1;
    }

    int repCost(char x, char y) {
        if (x == y) return 0;
        int rx = row(x), ry = row(y);
        if (rx == ry) return 1;
        return (hand(x) == hand(y)) ? 2 : 3;
    }

public:
    int minKeyboardEditCost(const string& a, const string& b) {
        int n = (int)a.size(), m = (int)b.size();
        vector<int> prev(m + 1), cur(m + 1);
        for (int j = 0; j <= m; j++) prev[j] = j;

        for (int i = 1; i <= n; i++) {
            cur[0] = i;
            char ca = a[i - 1];
            for (int j = 1; j <= m; j++) {
                char cb = b[j - 1];
                int del = prev[j] + 1;
                int ins = cur[j - 1] + 1;
                int rep = prev[j - 1] + repCost(ca, cb);
                cur[j] = min(del, min(ins, rep));
            }
            swap(prev, cur);
        }

        return prev[m];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    getline(cin, a);
    getline(cin, b);
    Solution sol;
    cout << sol.minKeyboardEditCost(a, b) << '\n';
    return 0;
}
