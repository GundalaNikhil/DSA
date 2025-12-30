#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    long long subsetAndEqualsX(vector<int>& a, int X) {
        vector<int> candidates;
        for (int v : a) {
            if ((v & X) == X) {
                candidates.push_back(v);
            }
        }
        
        int n = candidates.size();
        long long count = 0;
        int limit = 1 << n;
        
        for (int mask = 1; mask < limit; mask++) {
            int currentAnd = -1;
            bool first = true;
            
            for (int i = 0; i < n; i++) {
                if ((mask >> i) & 1) {
                    if (first) {
                        currentAnd = candidates[i];
                        first = false;
                    } else {
                        currentAnd &= candidates[i];
                    }
                }
            }
            if (!first && currentAnd == X) {
                count++;
            }
        }
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    int X;
    cin >> X;
    
    Solution solution;
    cout << solution.subsetAndEqualsX(a, X) << "\n";
    return 0;
}
