#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 313;

public:
    vector<bool> checkPalindromes(string s, vector<pair<int,int>>& queries) {
        int n = s.length();
        string revS = s;
        reverse(revS.begin(), revS.end());
        
        vector<long long> hFwd(n + 1, 0), hRev(n + 1, 0), power(n + 1, 1);
        
        for (int i = 0; i < n; i++) {
            hFwd[i + 1] = (hFwd[i] * BASE + s[i]) % MOD;
            hRev[i + 1] = (hRev[i] * BASE + revS[i]) % MOD;
            power[i + 1] = (power[i] * BASE) % MOD;
        }
        
        vector<bool> results;
        results.reserve(queries.size());
        
        for (const auto& q : queries) {
            int l = q.first;
            int r = q.second;
            
            long long fwdHash = getHash(hFwd, power, l, r);
            
            int revL = n - 1 - r;
            int revR = n - 1 - l;
            long long revHash = getHash(hRev, power, revL, revR);
            
            results.push_back(fwdHash == revHash);
        }
        
        return results;
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
    if (!(cin >> s)) return 0;
    
    int q;
    if (!(cin >> q)) return 0;
    
    vector<pair<int,int>> queries(q);
    for (int i = 0; i < q; i++) {
        cin >> queries[i].first >> queries[i].second;
    }
    
    Solution solution;
    vector<bool> result = solution.checkPalindromes(s, queries);
    
    for (bool ans : result) {
        cout << (ans ? "true" : "false") << "\n";
    }
    
    return 0;
}
