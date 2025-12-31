#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxOrSubarrayLeqK(vector<int>& a, int K) {
        int n = a.size();
        vector<int> bitCounts(32, 0);
        int currentOr = 0;
        int left = 0;
        int maxLen = 0;
        
        for (int right = 0; right < n; right++) {
            int val = a[right];
            for (int i = 0; i < 31; i++) {
                if ((val >> i) & 1) {
                    bitCounts[i]++;
                    if (bitCounts[i] == 1) {
                        currentOr |= (1 << i);
                    }
                }
            }
            
            while (left <= right && currentOr > K) {
                int removeVal = a[left];
                for (int i = 0; i < 31; i++) {
                    if ((removeVal >> i) & 1) {
                        bitCounts[i]--;
                        if (bitCounts[i] == 0) {
                            currentOr &= ~(1 << i);
                        }
                    }
                }
                left++;
            }
            
            if (currentOr <= K) {
                maxLen = max(maxLen, right - left + 1);
            }
        }
        return maxLen;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    int K;
    cin >> K;
    
    Solution solution;
    cout << solution.maxOrSubarrayLeqK(a, K) << "\n";
    return 0;
}
