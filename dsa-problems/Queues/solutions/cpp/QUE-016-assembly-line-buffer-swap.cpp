#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> swapQueues(const vector<int>& q1, const vector<int>& q2) {
        return {q2, q1};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> remaining;
        int val;
        while (cin >> val) {
            remaining.push_back(val);
        }

        vector<int> q1, q2;

        // If we have exactly 2n values
        if ((int)remaining.size() == 2 * n) {
            q1.assign(remaining.begin(), remaining.begin() + n);
            q2.assign(remaining.begin() + n, remaining.end());
        } else if ((int)remaining.size() == n) {
            // Only n values - use as q1, create default q2
            q1.assign(remaining.begin(), remaining.end());
            q2.assign(n, 0);
        } else {
            // Fallback
            q1.assign(remaining.begin(), remaining.begin() + min(n, (int)remaining.size()));
            if ((int)remaining.size() > n) {
                q2.assign(remaining.begin() + n, remaining.end());
            }
            // Pad q2 with 0s if needed
            while ((int)q2.size() < n) {
                q2.push_back(0);
            }
        }

        Solution sol;
        vector<vector<int>> result = sol.swapQueues(q1, q2);
        for (const auto& resArr : result) {
            for (int i = 0; i < (int)resArr.size(); i++) {
                cout << (i ? " " : "") << resArr[i];
            }
            cout << endl;
        }
    }
    return 0;
}
