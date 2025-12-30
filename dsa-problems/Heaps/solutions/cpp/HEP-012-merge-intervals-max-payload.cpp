#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> mergeIntervals(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};
        
        // Sort by start time
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        
        vector<vector<int>> merged;
        vector<int> current = intervals[0];
        
        for (size_t i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] <= current[1]) {
                current[1] = max(current[1], intervals[i][1]);
                current[2] = max(current[2], intervals[i][2]);
            } else {
                merged.push_back(current);
                current = intervals[i];
            }
        }
        merged.push_back(current);
        
        return merged;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<vector<int>> intervals(n, vector<int>(3));
        for (int i = 0; i < n; i++) {
            cin >> intervals[i][0] >> intervals[i][1] >> intervals[i][2];
        }
        
        Solution solution;
        vector<vector<int>> result = solution.mergeIntervals(intervals);
        cout << result.size() << "\n";
        for (const auto& row : result) {
            cout << row[0] << " " << row[1] << " " << row[2] << "\n";
        }
    }
    return 0;
}
