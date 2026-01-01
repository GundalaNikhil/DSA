#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> mergeQueues(const vector<int>& a, const vector<int>& b) {
        int n = a.size();
        int m = b.size();
        vector<int> result;
        result.reserve(n + m);
        
        int i = 0, j = 0;
        while (i < n && j < m) {
            if (a[i] <= b[j]) {
                result.push_back(a[i++]);
            } else {
                result.push_back(b[j++]);
            }
        }
        
        while (i < n) result.push_back(a[i++]);
        while (j < m) result.push_back(b[j++]);
        
        return result;
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

        vector<int> a, b;

        // If we have exactly 2n values, split them in half
        if ((int)remaining.size() == 2 * n) {
            a.assign(remaining.begin(), remaining.begin() + n);
            b.assign(remaining.begin() + n, remaining.end());
        } else if ((int)remaining.size() == n) {
            // Only n values - use as a, create empty b
            a.assign(remaining.begin(), remaining.end());
            b.clear();
        } else if ((int)remaining.size() > n) {
            // First value is m (size of b), rest split
            int m = remaining[0];
            if ((int)remaining.size() >= n + m) {
                a.assign(remaining.begin() + 1, remaining.begin() + n + 1);
                b.assign(remaining.begin() + n + 1, remaining.begin() + n + 1 + m);
            } else {
                a.assign(remaining.begin() + 1, remaining.begin() + min(n + 1, (int)remaining.size()));
                b.assign(remaining.begin() + min(n + 1, (int)remaining.size()), remaining.end());
            }
        } else {
            // Fallback
            a.assign(remaining.begin(), remaining.end());
            b.clear();
        }

        Solution solution;
        vector<int> result = solution.mergeQueues(a, b);
        for (int i = 0; i < (int)result.size(); i++) {
            if (i) cout << ' ';
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
