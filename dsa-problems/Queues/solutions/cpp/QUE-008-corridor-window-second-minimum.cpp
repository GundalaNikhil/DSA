#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    vector<int> secondMinimums(const vector<int>& values, int k) {
        int n = values.size();
        vector<int> result;
        multiset<int> window;
        
        for (int i = 0; i < n; i++) {
            window.insert(values[i]);
            if (i >= k) {
                window.erase(window.find(values[i - k]));
            }
            
            if (i >= k - 1) {
                if (k == 1) {
                    result.push_back(*window.begin());
                } else {
                    auto it = window.begin();
                    it++; // Move to second
                    result.push_back(*it);
                }
            }
        }
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

        vector<int> values;
        int k = 2;  // Default

        // If we have exactly n values
        if ((int)remaining.size() == n) {
            values.assign(remaining.begin(), remaining.end());
            k = 2;
        } else if ((int)remaining.size() == n + 1) {
            // First is k, rest are values
            k = remaining[0];
            values.assign(remaining.begin() + 1, remaining.begin() + n + 1);
        } else {
            // Fallback
            k = !remaining.empty() ? remaining[0] : 2;
            for (int i = 1; i <= n && i < (int)remaining.size(); i++) {
                values.push_back(remaining[i]);
            }
        }

        Solution solution;
        vector<int> result = solution.secondMinimums(values, k);
        for (int i = 0; i < (int)result.size(); i++) {
            if (i) cout << ' ';
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
