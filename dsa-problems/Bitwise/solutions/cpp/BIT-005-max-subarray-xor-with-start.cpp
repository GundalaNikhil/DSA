#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    long long maxSubarrayXorWithStart(vector<int>& a, int s) {
        long long currentXor = 0;
        long long maxXor = 0;
        bool first = true;
        
        for (int i = s; i < a.size(); i++) {
            currentXor ^= a[i];
            if (first) {
                maxXor = currentXor;
                first = false;
            } else {
                maxXor = max(maxXor, currentXor);
            }
        }
        return maxXor;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int s;
    cin >> s;
    
    Solution solution;
    cout << solution.maxSubarrayXorWithStart(a, s) << "\n";
    return 0;
}
