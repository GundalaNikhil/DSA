#include <iostream>
using namespace std;

class Solution {
public:
    long long minimalBitsFlipRange(long long x, long long y) {
        unsigned long long diff = x ^ y;
        if (diff == 0) return 0;
        
        if ((diff & (diff + 1)) == 0) {
            // Number of set bits.
            // For example 111 (7) -> 3.
            return __builtin_popcountll(diff);
        }
        
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long x, y;
    if (!(cin >> x >> y)) return 0;

    Solution solution;
    cout << solution.minimalBitsFlipRange(x, y) << "\n";
    return 0;
}
