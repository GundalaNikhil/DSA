#include <iostream>
using namespace std;

class Solution {
public:
    long long bitwiseAndSkipMultiples(long long L, long long R, int m) {
        // Threshold: 2e6 is safe given 2s time limit (usually ~10^8 ops allowed)
        if (R - L <= 2000000) {
            long long ans = -1;
            bool found = false;
            for (long long i = L; i <= R; i++) {
                if (i % m != 0) {
                    ans &= i;
                    found = true;
                }
            }
            return found ? ans : -1;
        }
        
        long long lTemp = L;
        long long rTemp = R;
        int shift = 0;
        while (lTemp != rTemp) {
            lTemp >>= 1;
            rTemp >>= 1;
            shift++;
        }
        
        long long standardAnd = lTemp << shift;
        
        if (m == 2) {
            standardAnd |= 1;
        }
        
        return standardAnd;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    int m;
    if (!(cin >> L >> R >> m)) return 0;

    Solution solution;
    cout << solution.bitwiseAndSkipMultiples(L, R, m) << "\n";
    return 0;
}
