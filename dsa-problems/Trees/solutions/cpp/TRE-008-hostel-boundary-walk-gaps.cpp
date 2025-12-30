#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    void addLeaves(int u, const vector<int>& values, const vector<int>& left, const vector<int>& right, vector<int>& result) {
        if (u == -1) return;
        if (left[u] == -1 && right[u] == -1) {
            if (values[u] >= 0) result.push_back(values[u]);
            return;
        }
        addLeaves(left[u], values, left, right, result);
        addLeaves(right[u], values, left, right, result);
    }

public:
    vector<int> boundaryWithGaps(int n, const vector<int>& values,
                                 const vector<int>& left, const vector<int>& right) {
        vector<int> result;
        if (n == 0) return result;

        if (values[0] >= 0) result.push_back(values[0]);
        if (left[0] == -1 && right[0] == -1) return result;

        // Left Boundary
        int curr = left[0];
        while (curr != -1) {
            if (left[curr] == -1 && right[curr] == -1) break;
            if (values[curr] >= 0) result.push_back(values[curr]);
            if (left[curr] != -1) curr = left[curr];
            else curr = right[curr];
        }

        // Leaves
        addLeaves(0, values, left, right, result);

        // Right Boundary
        vector<int> rightBound;
        curr = right[0];
        while (curr != -1) {
            if (left[curr] == -1 && right[curr] == -1) break;
            if (values[curr] >= 0) rightBound.push_back(values[curr]);
            if (right[curr] != -1) curr = right[curr];
            else curr = left[curr];
        }
        reverse(rightBound.begin(), rightBound.end());
        result.insert(result.end(), rightBound.begin(), rightBound.end());

        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> left[i] >> right[i];
    }

    Solution solution;
    vector<int> ans = solution.boundaryWithGaps(n, values, left, right);
    for (int i = 0; i < (int)ans.size(); i++) {
        if (i) cout << ' ';
        cout << ans[i];
    }
    return 0;
}
