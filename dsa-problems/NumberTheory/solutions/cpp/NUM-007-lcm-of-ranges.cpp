#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

class Solution {
    long long power(long long base, long long exp, long long mod) {
        long long res = 1;
        base %= mod;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp /= 2;
        }
        return res;
    }

public:
    long long lcmRange(const vector<int>& a, int l, int r, long long MOD) {
        map<int, int> maxExponents;
        
        for (int i = l; i <= r; i++) {
            int num = a[i];
            for (long long p = 2; p * p <= num; p++) {
                if (num % p == 0) {
                    int count = 0;
                    while (num % p == 0) {
                        num /= p;
                        count++;
                    }
                    if (maxExponents.find(p) == maxExponents.end() || count > maxExponents[p]) {
                        maxExponents[p] = count;
                    }
                }
            }
            if (num > 1) {
                if (maxExponents.find(num) == maxExponents.end() || 1 > maxExponents[num]) {
                    maxExponents[num] = 1;
                }
            }
        }
        
        long long ans = 1;
        for (auto const& [p, e] : maxExponents) {
            ans = (ans * power(p, e, MOD)) % MOD;
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    long long MOD;
    if (cin >> n >> q >> MOD) {
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];

        Solution solution;
        for (int i = 0; i < q; i++) {
            int l, r;
            cin >> l >> r;
            cout << solution.lcmRange(a, l, r, MOD) << "\n";
        }
    }
    return 0;
}
