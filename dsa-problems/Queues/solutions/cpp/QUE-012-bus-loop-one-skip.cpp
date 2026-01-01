#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findStart(vector<int>& gain, const vector<int>& cost) {
        int n = gain.size();
        
        // 1. Find min gain
        int minGainIdx = 0;
        for (int i = 1; i < n; i++) {
            if (gain[i] < gain[minGainIdx]) {
                minGainIdx = i;
            }
        }
        
        // 2. Skip it
        int original = gain[minGainIdx];
        gain[minGainIdx] = 0;
        
        // 3. Standard Greedy
        long long totalTank = 0;
        long long currTank = 0;
        int start = 0;
        
        for (int i = 0; i < n; i++) {
            int net = gain[i] - cost[i];
            totalTank += net;
            currTank += net;
            if (currTank < 0) {
                start = i + 1;
                currTank = 0;
            }
        }
        
        gain[minGainIdx] = original;
        
        return totalTank >= 0 ? start % n : -1;
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

        vector<int> gain, cost;

        // If we have exactly 2n values
        if ((int)remaining.size() == 2 * n) {
            gain.assign(remaining.begin(), remaining.begin() + n);
            cost.assign(remaining.begin() + n, remaining.end());
        } else if ((int)remaining.size() == n) {
            // Only n values - use as gain, create default cost of 1s
            gain.assign(remaining.begin(), remaining.end());
            cost.assign(n, 1);
        } else {
            // Fallback
            gain.assign(remaining.begin(), remaining.begin() + min(n, (int)remaining.size()));
            if ((int)remaining.size() > n) {
                cost.assign(remaining.begin() + n, remaining.end());
            }
            // Pad with 1s if needed
            while ((int)cost.size() < n) {
                cost.push_back(1);
            }
        }

        Solution solution;
        cout << solution.findStart(gain, cost) << "\n";
    }
    return 0;
}
