#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool checkStart(int n, vector<int>& gain, vector<int>& cost, int startIdx) {
        long long fuel = 0;
        long long maxC = 0;
        bool used = false;

        for (int i = 0; i < n; i++) {
            int idx = (startIdx + i) % n;
            fuel += gain[idx];
            maxC = max(maxC, (long long)cost[idx]);
            fuel -= cost[idx];

            if (fuel < 0) {
                if (!used) {
                    fuel += maxC;
                    used = true;
                    if (fuel < 0) return false;
                } else {
                    return false;
                }
            }
        }

        return true;
    }

    int findStart(int n, vector<int>& gain, vector<int>& cost) {
        long long totalGain = 0;
        long long totalCost = 0;
        long long maxCost = 0;

        for (int i = 0; i < n; i++) {
            totalGain += gain[i];
            totalCost += cost[i];
            maxCost = max(maxCost, (long long)cost[i]);
        }

        // If even with refund we can't make it, return -1
        if (totalGain < totalCost - maxCost) {
            return -1;
        }

        // Total gain + max cost must be >= total cost
        if (totalGain + maxCost < totalCost) {
            return -1;
        }

        // Check classic gas station start first
        vector<long long> diff(n);
        for (int i = 0; i < n; i++) {
            diff[i] = gain[i] - cost[i];
        }

        long long curr = 0;
        long long minSum = 0;
        int startCand = 0;

        for (int i = 0; i < n; i++) {
            curr += diff[i];
            if (curr < minSum) {
                minSum = curr;
                startCand = (i + 1) % n;
            }
        }

        if (checkStart(n, gain, cost, startCand)) {
            return startCand;
        }

        // If not, try all
        for (int i = 0; i < n; i++) {
            if (checkStart(n, gain, cost, i)) {
                return i;
            }
        }

        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> gain(n), cost(n);
    for (int i = 0; i < n; i++) cin >> gain[i];
    for (int i = 0; i < n; i++) cin >> cost[i];

    Solution solution;
    cout << solution.findStart(n, gain, cost) << "\n";

    return 0;
}
