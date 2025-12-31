#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

class Solution {
    const long long MOD1 = 1e9 + 7;
    const long long BASE1 = 313;
    const long long MOD2 = 1e9 + 9;
    const long long BASE2 = 317;

public:
    long long countPairs(string s, int L) {
        int n = s.length();
        if (L > n) return 0;
        
        map<pair<long long, long long>, int> counts;
        
        long long h1 = 0, h2 = 0;
        long long p1 = 1, p2 = 1;
        
        for (int i = 0; i < L - 1; i++) {
            p1 = (p1 * BASE1) % MOD1;
            p2 = (p2 * BASE2) % MOD2;
        }
        
        for (int i = 0; i < L; i++) {
            h1 = (h1 * BASE1 + s[i]) % MOD1;
            h2 = (h2 * BASE2 + s[i]) % MOD2;
        }
        
        counts[{h1, h2}]++;
        
        for (int i = 1; i <= n - L; i++) {
            long long remove1 = (s[i - 1] * p1) % MOD1;
            h1 = (h1 - remove1 + MOD1) % MOD1;
            h1 = (h1 * BASE1 + s[i + L - 1]) % MOD1;
            
            long long remove2 = (s[i - 1] * p2) % MOD2;
            h2 = (h2 - remove2 + MOD2) % MOD2;
            h2 = (h2 * BASE2 + s[i + L - 1]) % MOD2;
            
            counts[{h1, h2}]++;
        }
        
        long long ans = 0;
        for (auto const& [key, count] : counts) {
            ans += (long long)count * (count - 1) / 2;
        }
        
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    int L;
    if (getline(cin, s) && cin >> L) {
        Solution solution;
        cout << solution.countPairs(s, L) << "\n";
    }
    
    return 0;
}
