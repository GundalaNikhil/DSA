#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct Result {
    int height;
    long long weight;
    bool balanced;
};

class Solution {
    Result dfs(int u, const vector<long long>& weight, const vector<int>& left, const vector<int>& right, long long W) {
        if (u == -1) return {0, 0, true};

        Result l = dfs(left[u], weight, left, right, W);
        if (!l.balanced) return {0, 0, false};

        Result r = dfs(right[u], weight, left, right, W);
        if (!r.balanced) return {0, 0, false};

        bool hBal = abs(l.height - r.height) <= 1;
        bool wBal = abs(l.weight - r.weight) <= W;

        if (hBal && wBal) {
            return {max(l.height, r.height) + 1, l.weight + r.weight + weight[u], true};
        } else {
            return {0, 0, false};
        }
    }

public:
    bool isBalancedWeighted(int n, const vector<long long>& weight,
                            const vector<int>& left, const vector<int>& right, long long W) {
        if (n == 0) return true;
        return dfs(0, weight, left, right, W).balanced;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> weight(n);
    vector<int> left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> weight[i] >> left[i] >> right[i];
    }
    long long W;
    cin >> W;

    Solution solution;
    cout << (solution.isBalancedWeighted(n, weight, left, right, W) ? "true" : "false") << "\n";
    return 0;
}
