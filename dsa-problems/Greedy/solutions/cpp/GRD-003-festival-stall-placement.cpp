#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxStalls(vector<pair<int,int>>& stalls, int d) {
        // Sort by end time
        sort(stalls.begin(), stalls.end(), [](const pair<int,int>& a, const pair<int,int>& b) {
            return a.second < b.second;
        });
        
        int count = 0;
        long long lastEnd = -2e18; // Sufficiently small number
        
        for (const auto& stall : stalls) {
            if (stall.first - lastEnd >= d) {
                count++;
                lastEnd = stall.second;
            }
        }
        
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, d;
    if (!(cin >> n >> d)) return 0;

    vector<pair<int,int>> stalls(n);
    for (int i = 0; i < n; i++) {
        cin >> stalls[i].first >> stalls[i].second;
    }

    Solution solution;
    cout << solution.maxStalls(stalls, d) << "\n";

    return 0;
}
