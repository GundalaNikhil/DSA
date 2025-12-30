#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findStart(int n, vector<int>& gain, vector<int>& cost) {
        long long totalGain = 0;
        long long totalCost = 0;
        int maxCostVal = -1;
        int maxCostIdx = -1;
        
        for (int i = 0; i < n; i++) {
            totalGain += gain[i];
            totalCost += cost[i];
            if (cost[i] > maxCostVal) {
                maxCostVal = cost[i];
                maxCostIdx = i;
            }
        }
        
        if (totalGain < totalCost - maxCostVal) {
            return -1;
        }
        
        long long currentTank = 0;
        int start = 0;
        
        for (int i = 0; i < n; i++) {
            long long currentCost = (i == maxCostIdx) ? 0 : cost[i];
            currentTank += gain[i] - currentCost;
            
            if (currentTank < 0) {
                start = i + 1;
                currentTank = 0;
            }
        }
        
        return start;
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
