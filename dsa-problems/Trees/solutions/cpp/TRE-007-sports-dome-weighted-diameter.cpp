#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    long long maxDiameter = 0;

    long long dfs(int u, const vector<int>& left, const vector<int>& right,
                  const vector<long long>& lw, const vector<long long>& rw) {
        if (u == -1) return 0;

        long long lPath = 0;
        long long rPath = 0;

        if (left[u] != -1) {
            lPath = lw[u] + dfs(left[u], left, right, lw, rw);
        }
        if (right[u] != -1) {
            rPath = rw[u] + dfs(right[u], left, right, lw, rw);
        }

        maxDiameter = max(maxDiameter, lPath + rPath);

        return max(lPath, rPath);
    }

public:
    long long weightedDiameter(int n, const vector<int>& left, const vector<int>& right,
                               const vector<long long>& lw, const vector<long long>& rw) {
        if (n == 0) return 0;
        maxDiameter = 0;
        dfs(0, left, right, lw, rw);
        return maxDiameter;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> left(n), right(n);
    vector<long long> lw(n), rw(n);
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val >> left[i] >> right[i] >> lw[i] >> rw[i];
    }

    Solution solution;
    cout << solution.weightedDiameter(n, left, right, lw, rw) << "\n";
    return 0;
}
