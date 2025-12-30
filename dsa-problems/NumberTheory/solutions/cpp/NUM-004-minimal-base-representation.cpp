#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
    long long getDigitSum(long long x, int b) {
        long long sum = 0;
        while (x > 0) {
            sum += x % b;
            x /= b;
        }
        return sum;
    }

public:
    pair<long long, long long> minimalBase(long long x) {
        long long minSum = LLONG_MAX;
        long long bestBase = 2;
        
        for (int b = 2; b <= 36; b++) {
            long long currentSum = getDigitSum(x, b);
            if (currentSum < minSum) {
                minSum = currentSum;
                bestBase = b;
            }
        }
        
        return {bestBase, minSum};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long x;
    if (cin >> x) {
        Solution solution;
        auto res = solution.minimalBase(x);
        cout << res.first << " " << res.second << "\n";
    }
    return 0;
}
