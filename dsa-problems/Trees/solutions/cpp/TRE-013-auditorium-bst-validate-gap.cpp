#include <iostream>
#include <vector>
#include <cmath>
#include <limits>

using namespace std;

class Solution {
    bool validate(int u, long long minVal, long long maxVal, const vector<long long>& values,
                  const vector<int>& left, const vector<int>& right, long long G) {
        if (u == -1) return true;

        long long val = values[u];
        if (val <= minVal || val >= maxVal) return false;

        if (left[u] != -1) {
            long long lVal = values[left[u]];
            if (abs(val - lVal) < G) return false;
            if (!validate(left[u], minVal, val, values, left, right, G)) return false;
        }

        if (right[u] != -1) {
            long long rVal = values[right[u]];
            if (abs(val - rVal) < G) return false;
            if (!validate(right[u], val, maxVal, values, left, right, G)) return false;
        }

        return true;
    }

public:
    bool validateBSTGap(int n, const vector<long long>& values,
                        const vector<int>& left, const vector<int>& right, long long G) {
        if (n == 0) return true;
        return validate(0, numeric_limits<long long>::min(), numeric_limits<long long>::max(), values, left, right, G);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> values(n);
    vector<int> left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> left[i] >> right[i];
    }
    long long G;
    cin >> G;

    Solution solution;
    cout << (solution.validateBSTGap(n, values, left, right, G) ? "true" : "false") << "\n";
    return 0;
}
