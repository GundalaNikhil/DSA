#include <vector>
#include <cmath>
#include <climits>
#include <cstdlib>

using namespace std;

class Solution {
public:
    vector<int> closestPair(const vector<int>& arr, int target) {
        vector<int> sorted = arr;
        sort(sorted.begin(), sorted.end());
        int n = sorted.size();
        int left = 0;
        int right = n - 1;
        
        long long minDiff = LLONG_MAX;
        int resLeft = -1;
        int resRight = -1;
        
        while (left < right) {
            long long sum = (long long)sorted[left] + sorted[right];
            long long diff = abs(sum - target);
            
            if (diff < minDiff) {
                minDiff = diff;
                resLeft = sorted[left];
                resRight = sorted[right];
            }
            
            if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        
        return {resLeft, resRight};
    }
};
