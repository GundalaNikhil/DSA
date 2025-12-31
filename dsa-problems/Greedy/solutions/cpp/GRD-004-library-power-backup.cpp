#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    int minBatterySwaps(int n, long long T, vector<long long>& capacities) {
        long long totalCapacity = 0;
        for (long long c : capacities) {
            totalCapacity += c;
        }
        
        if (totalCapacity < T) {
            return -1;
        }
        
        // Sort descending
        sort(capacities.rbegin(), capacities.rend());
        
        long long currentSum = 0;
        int count = 0;
        
        for (long long c : capacities) {
            currentSum += c;
            count++;
            if (currentSum >= T) {
                return count - 1;
            }
        }
        
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long T;
    if (!(cin >> n >> T)) return 0;

    vector<long long> capacities(n);
    for (int i = 0; i < n; i++) {
        cin >> capacities[i];
    }

    Solution solution;
    cout << solution.minBatterySwaps(n, T, capacities) << "\n";

    return 0;
}
