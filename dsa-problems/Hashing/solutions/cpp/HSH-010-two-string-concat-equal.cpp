#include <iostream>
#include <string>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 313;

public:
    bool checkConcatenationEqual(string a, string b, string c, string d) {
        if (a.length() + b.length() != c.length() + d.length()) {
            return false;
        }

        long long hA = computeHash(a);
        long long hB = computeHash(b);
        long long hC = computeHash(c);
        long long hD = computeHash(d);

        long long combinedAB = combine(hA, hB, b.length());
        long long combinedCD = combine(hC, hD, d.length());

        return combinedAB == combinedCD;
    }

    long long computeHash(const string& s) {
        long long h = 0;
        for (char ch : s) {
            h = (h * BASE + ch) % MOD;
        }
        return h;
    }

    long long combine(long long h1, long long h2, int len2) {
        long long p = 1;
        long long b = BASE;
        int exp = len2;
        while (exp > 0) {
            if (exp & 1) p = (p * b) % MOD;
            b = (b * b) % MOD;
            exp >>= 1;
        }
        return (h1 * p + h2) % MOD;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b, c, d;
    if (getline(cin, a) && getline(cin, b) && getline(cin, c) && getline(cin, d)) {
        Solution solution;
        cout << (solution.checkConcatenationEqual(a, b, c, d) ? "true" : "false") << "\n";
    }

    return 0;
}
