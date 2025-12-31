#include <vector>
#include <cmath>
#include <climits>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> closestPairCircular(const vector<int>& arr, int target) {
        int n = arr.size();
        if (n == 0) return {};
        
        int pivot = 0;
        for (int i = 1; i < n; i++) {
            if (arr[i] < arr[pivot]) {
                pivot = i;
            }
        }
        
        int l = 0;
        int r = n - 1;
        long long minDiff = LLONG_MAX;
        int res1 = -1, res2 = -1;
        
        while (l < r) {
            int pL = (pivot + l) % n;
            int pR = (pivot + r) % n;
            
            long long sum = (long long)arr[pL] + arr[pR];
            long long diff = abs(sum - target);
            
            if (diff < minDiff) {
                minDiff = diff;
                res1 = arr[pL];
                res2 = arr[pR];
            }
            
            if (sum < target) {
                l++;
            } else {
                r--;
            }
        }
        
        return {res1, res2};
    }
};
