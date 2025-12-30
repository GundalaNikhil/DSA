#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    int minProctors(int n, int r, vector<pair<int,int>>& exams) {
        vector<pair<int,int>> events;
        events.reserve(2 * n);
        
        for (const auto& exam : exams) {
            events.push_back({exam.first, 1});  // Start
            events.push_back({exam.second, -1}); // End
        }
        
        // Sort: Time ascending. If times equal, Start (+1) before End (-1).
        // Since -1 < 1, default sort puts End before Start.
        // We want Start before End. So we need custom comparator.
        sort(events.begin(), events.end(), [](const pair<int,int>& a, const pair<int,int>& b) {
            if (a.first != b.first) return a.first < b.first;
            return a.second > b.second; // 1 > -1, so Start comes first
        });
        
        int maxOverlap = 0;
        int currentOverlap = 0;
        
        for (const auto& event : events) {
            currentOverlap += event.second;
            maxOverlap = max(maxOverlap, currentOverlap);
        }
        
        return (maxOverlap + r - 1) / r;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, r;
    if (!(cin >> n >> r)) return 0;
    
    vector<pair<int,int>> exams(n);
    for (int i = 0; i < n; i++) {
        cin >> exams[i].first >> exams[i].second;
    }
    
    Solution solution;
    cout << solution.minProctors(n, r, exams) << "\n";
    
    return 0;
}
