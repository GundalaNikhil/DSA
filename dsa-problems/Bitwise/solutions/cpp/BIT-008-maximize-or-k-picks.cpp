#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

class Solution {
public:
    long long maximizeOrWithKPicks(vector<int>& a, int k) {
        int n = a.size();
        if (k >= 30) {
            long long total = 0;
            for (int x : a) total |= x;
            return total;
        }
        
        long long currentOr = 0;
        vector<bool> used(n, false);
        
        for (int step = 0; step < k; step++) {
            long long bestOr = -1;
            int bestIdx = -1;
            
            for (int i = 0; i < n; i++) {
                if (!used[i]) {
                    long long newOr = currentOr | a[i];
                    if (newOr > bestOr) {
                        bestOr = newOr;
                        bestIdx = i;
                    }
                }
            }
            
            if (bestIdx != -1) {
                currentOr = bestOr;
                used[bestIdx] = true;
            }
        }
        return currentOr;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    int k;
    cin >> k;

    Solution solution;
    cout << solution.maximizeOrWithKPicks(a, k) << "\n";
    return 0;
}
