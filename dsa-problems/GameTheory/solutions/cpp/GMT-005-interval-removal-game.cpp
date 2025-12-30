#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string intervalRemovalGame(int n, vector<vector<int>>& intervals) {
        long long xorSum = 0;
        for (const auto& interval : intervals) {
            long long len = (long long)interval[1] - interval[0];
            xorSum ^= len;
        }
        return xorSum > 0 ? "First" : "Second";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (cin >> n) {
        vector<vector<int>> intervals(n, vector<int>(2));
        for (int i = 0; i < n; i++) {
            cin >> intervals[i][0] >> intervals[i][1];
        }
        
        Solution solution;
        cout << solution.intervalRemovalGame(n, intervals) << "\n";
    }
    return 0;
}
