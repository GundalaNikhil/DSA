#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 313;

public:
    int detectPeriod(string s) {
        int n = s.length();
        vector<long long> h(n + 1, 0), p(n + 1, 1);
        
        for (int i = 0; i < n; i++) {
            h[i + 1] = (h[i] * BASE + s[i]) % MOD;
            p[i + 1] = (p[i] * BASE) % MOD;
        }
        
        vector<int> divisors;
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                divisors.push_back(i);
                if (i * i != n) {
                    divisors.push_back(n / i);
                }
            }
        }
        sort(divisors.begin(), divisors.end());
        
        for (int len : divisors) {
            if (len == n) return n;
            
            long long h1 = getHash(h, p, 0, n - len - 1);
            long long h2 = getHash(h, p, len, n - 1);
            
            if (h1 == h2) return len;
        }
        
        return n;
    }
    
    long long getHash(const vector<long long>& h, const vector<long long>& p, int l, int r) {
        int len = r - l + 1;
        long long val = (h[r + 1] - (h[l] * p[len]) % MOD + MOD) % MOD;
        return val;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    if (getline(cin, s)) {
        Solution solution;
        cout << solution.detectPeriod(s) << "\n";
    }
    
    return 0;
}
