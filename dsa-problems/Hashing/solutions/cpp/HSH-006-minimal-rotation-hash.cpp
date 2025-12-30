#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
    const long long MOD = 1e9 + 7;
    const long long BASE = 313;

public:
    string minimalRotation(string s) {
        int n = s.length();
        string doubled = s + s;
        int m = doubled.length();
        
        vector<long long> h(m + 1, 0), p(m + 1, 1);
        
        for (int i = 0; i < m; i++) {
            h[i + 1] = (h[i] * BASE + doubled[i]) % MOD;
            p[i + 1] = (p[i] * BASE) % MOD;
        }
        
        int best = 0;
        for (int curr = 1; curr < n; curr++) {
            int lcp = getLCP(h, p, best, curr, n);
            if (lcp < n) {
                if (doubled[curr + lcp] < doubled[best + lcp]) {
                    best = curr;
                }
            }
        }
        
        return doubled.substr(best, n);
    }
    
    int getLCP(const vector<long long>& h, const vector<long long>& p, int i, int j, int maxLen) {
        int low = 0, high = maxLen;
        int ans = 0;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (mid == 0) {
                low = mid + 1;
                continue;
            }
            
            long long h1 = getHash(h, p, i, i + mid - 1);
            long long h2 = getHash(h, p, j, j + mid - 1);
            
            if (h1 == h2) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
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
        cout << solution.minimalRotation(s) << "\n";
    }
    
    return 0;
}
