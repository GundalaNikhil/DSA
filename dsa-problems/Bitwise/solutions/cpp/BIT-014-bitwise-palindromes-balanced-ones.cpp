#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
    long long makePalindrome(long long half, int len) {
        long long res = half;
        long long temp = half;
        if (len % 2 == 1) temp >>= 1;

        long long lower = 0;
        for (int i = 0; i < len / 2; i++) {
            lower = (lower << 1) | (temp & 1);
            temp >>= 1;
        }
        return (res << (len / 2)) | lower;
    }

    long long countForLen(long long N, int len, bool isLimit) {
        int halfLen = (len + 1) / 2;
        long long minHalf = 1LL << (halfLen - 1);
        long long maxHalf = (1LL << halfLen) - 1;

        if (isLimit) {
            long long prefix = N >> (len - halfLen);
            if (prefix < minHalf) return 0;
            maxHalf = min(maxHalf, prefix);
        }

        long long limitVal = maxHalf;
        long long validBelow = 0;

        if (limitVal > minHalf) {
            if (len % 2 == 0) {
                validBelow = limitVal - minHalf;
            } else {
                validBelow = (limitVal - minHalf + 1) / 2;
            }
        }

        bool checkBoundary = true;
        if (len % 2 == 1 && (limitVal % 2 != 0)) checkBoundary = false;

        if (checkBoundary) {
            long long p = makePalindrome(limitVal, len);
            if (!isLimit || p <= N) {
                validBelow++;
            }
        }

        return validBelow;
    }

    long long solve(long long N) {
        if (N < 0) return 0;
        if (N == 0) return 1;

        int L = 0;
        long long temp = N;
        while (temp > 0) { L++; temp >>= 1; }

        long long total = 1;

        for (int len = 1; len < L; len++) {
            total += countForLen(-1, len, false); // -1 is all 1s, essentially infinite
        }
        total += countForLen(N, L, true);
        return total;
    }

public:
    long long countBitwisePalindromesBalancedOnes(long long L, long long R) {
        return solve(R) - solve(L - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long L, R;
    if (!(cin >> L >> R)) return 0;

    Solution solution;
    cout << solution.countBitwisePalindromesBalancedOnes(L, R) << "\n";
    return 0;
}
