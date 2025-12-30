#include <iostream>
#include <string>

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
    long long modExpStream(long long a, long long m, const string& e) {
        long long ans = 1;
        
        for (char c : e) {
            int d = c - '0';
            ans = power(ans, 10, m);
            long long term = power(a, d, m);
            ans = (ans * term) % m;
        }
        
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, m;
    string e;
    if (cin >> a >> m >> e) {
        Solution solution;
        cout << solution.modExpStream(a, m, e) << "\n";
    }
    return 0;
}
