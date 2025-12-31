#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

typedef __int128_t int128;

string int128ToString(int128 n) {
    if (n == 0) return "0";
    string s = "";
    while (n > 0) {
        s += (char)('0' + (n % 10));
        n /= 10;
    }
    reverse(s.begin(), s.end());
    return s;
}

class Solution {
    int128 extendedGCD(int128 a, int128 b, int128 &x, int128 &y) {
        if (b == 0) {
            x = 1;
            y = 0;
            return a;
        }
        int128 x1, y1;
        int128 g = extendedGCD(b, a % b, x1, y1);
        x = y1;
        y = x1 - (a / b) * y1;
        return g;
    }

public:
    string crtSolve(const vector<long long>& a, const vector<long long>& m) {
        int128 curA = 0;
        int128 curM = 1;
        
        for (size_t i = 0; i < a.size(); ++i) {
            int128 A = a[i];
            int128 M = m[i];
            
            int128 rhs = (A - curA) % M;
            if (rhs < 0) rhs += M;
            
            int128 x, y;
            int128 g = extendedGCD(curM, M, x, y);
            
            if (rhs % g != 0) return "NO";
            
            int128 mod = M / g;
            int128 k = (rhs / g) % mod * (x % mod + mod) % mod;
            k %= mod;
            
            int128 newM = curM * (M / g);
            curA = (curA + k * curM) % newM;
            curM = newM;
        }
        return int128ToString(curA);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (cin >> k) {
        vector<long long> a(k), m(k);
        for (int i = 0; i < k; i++) {
            cin >> a[i] >> m[i];
        }

        Solution solution;
        string result = solution.crtSolve(a, m);
        cout << result << "\n";
    }
    return 0;
}
