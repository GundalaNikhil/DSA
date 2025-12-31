#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxGapAfterRemovals(vector<int>& seats, vector<int>& removeIndices) {
        int n = seats.size();
        vector<bool> removed(n, false);
        
        for (int idx : removeIndices) {
            removed[idx] = true;
        }
        
        int maxGap = 0;
        int lastPos = -1;
        bool first = true;
        
        for (int i = 0; i < n; i++) {
            if (!removed[i]) {
                if (!first) {
                    maxGap = max(maxGap, seats[i] - lastPos);
                }
                lastPos = seats[i];
                first = false;
            }
        }
        
        return maxGap;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> seats(n);
    for (int i = 0; i < n; i++) cin >> seats[i];
    
    int r;
    cin >> r;
    vector<int> removeIndices(r);
    for (int i = 0; i < r; i++) cin >> removeIndices[i];

    Solution solution;
    cout << solution.maxGapAfterRemovals(seats, removeIndices) << "\n";
    return 0;
}
