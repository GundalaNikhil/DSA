#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

class Solution {
public:
    long long minSwapsToSort(const vector<int>& arr) {
        int n = arr.size();
        vector<pair<int, int>> pairs(n);
        for (int i = 0; i < n; i++) {
            pairs[i] = {arr[i], i};
        }
        
        sort(pairs.begin(), pairs.end());
        
        vector<bool> visited(n, false);
        long long swaps = 0;
        
        for (int i = 0; i < n; i++) {
            if (visited[i] || pairs[i].second == i) {
                continue;
            }
            
            int cycleSize = 0;
            int j = i;
            while (!visited[j]) {
                visited[j] = true;
                j = pairs[j].second;
                cycleSize++;
            }
            
            if (cycleSize > 0) {
                swaps += (cycleSize - 1);
            }
        }
        
        return swaps;
    }
};
