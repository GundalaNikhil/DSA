#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long minOvertimeCost(int n, long long H, vector<pair<int,int>>& shifts) {
        long long totalStandard = 0;
        int minRate = 2e9; // Initialize with a large value
        
        for (const auto& shift : shifts) {
            totalStandard += shift.first;
            if (shift.second < minRate) {
                minRate = shift.second;
            }
        }
        
        if (totalStandard >= H) {
            return 0;
        }
        
        long long needed = H - totalStandard;
        return needed * minRate;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long H;
    if (!(cin >> n >> H)) return 0;

    vector<pair<int,int>> shifts(n);
    for (int i = 0; i < n; i++) {
        cin >> shifts[i].first >> shifts[i].second;
    }

    Solution solution;
    cout << solution.minOvertimeCost(n, H, shifts) << "\n";

    return 0;
}
