#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestAfterChange(const vector<int>& arr) {
        int n = arr.size();
        if (n <= 1) return n;
        
        vector<int> L(n, 1);
        for (int i = 1; i < n; i++) {
            if (arr[i] > arr[i-1]) L[i] = L[i-1] + 1;
        }
        
        vector<int> R(n, 1);
        for (int i = n - 2; i >= 0; i--) {
            if (arr[i] < arr[i+1]) R[i] = R[i+1] + 1;
        }
        
        int maxLen = 1;
        for (int len : L) maxLen = max(maxLen, len);
        
        for (int i = 0; i < n; i++) {
            // Extend left
            if (i > 0) maxLen = max(maxLen, L[i-1] + 1);
            
            // Extend right
            if (i < n - 1) maxLen = max(maxLen, R[i+1] + 1);
            
            // Bridge
            if (i > 0 && i < n - 1 && (long long)arr[i+1] - arr[i-1] >= 2) {
                maxLen = max(maxLen, L[i-1] + 1 + R[i+1]);
            }
        }
        
        return maxLen;
    }
};
