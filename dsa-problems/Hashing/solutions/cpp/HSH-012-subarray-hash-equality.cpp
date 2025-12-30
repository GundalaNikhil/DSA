#include <iostream>
#include <vector>

using namespace std;

class Solution {
    const long long MOD1 = 1e9 + 7;
    const long long BASE1 = 100003;
    const long long MOD2 = 1e9 + 9;
    const long long BASE2 = 100019;

public:
    vector<bool> checkSubarrayEquality(vector<int>& arr, vector<vector<int>>& queries) {
        int n = arr.size();
        
        vector<long long> h1(n + 1, 0), p1(n + 1, 1);
        vector<long long> h2(n + 1, 0), p2(n + 1, 1);
        
        for (int i = 0; i < n; i++) {
            long long val = arr[i];
            
            h1[i + 1] = (h1[i] * BASE1 + val) % MOD1;
            if (h1[i + 1] < 0) h1[i + 1] += MOD1;
            p1[i + 1] = (p1[i] * BASE1) % MOD1;
            
            h2[i + 1] = (h2[i] * BASE2 + val) % MOD2;
            if (h2[i + 1] < 0) h2[i + 1] += MOD2;
            p2[i + 1] = (p2[i] * BASE2) % MOD2;
        }
        
        vector<bool> results;
        results.reserve(queries.size());
        
        for (const auto& q : queries) {
            int l1 = q[0], r1 = q[1], l2 = q[2], r2 = q[3];
            
            if (r1 - l1 != r2 - l2) {
                results.push_back(false);
                continue;
            }
            
            long long hash1_s1 = getHash(h1, p1, l1, r1, MOD1);
            long long hash1_s2 = getHash(h1, p1, l2, r2, MOD1);
            
            if (hash1_s1 != hash1_s2) {
                results.push_back(false);
                continue;
            }
            
            long long hash2_s1 = getHash(h2, p2, l1, r1, MOD2);
            long long hash2_s2 = getHash(h2, p2, l2, r2, MOD2);
            
            results.push_back(hash2_s1 == hash2_s2);
        }
        
        return results;
    }
    
    long long getHash(const vector<long long>& h, const vector<long long>& p, int l, int r, long long mod) {
        int len = r - l + 1;
        long long val = (h[r + 1] - (h[l] * p[len]) % mod + mod) % mod;
        return val;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    int q;
    if (!(cin >> q)) return 0;
    
    vector<vector<int>> queries(q, vector<int>(4));
    for (int i = 0; i < q; i++) {
        cin >> queries[i][0] >> queries[i][1] >> queries[i][2] >> queries[i][3];
    }
    
    Solution solution;
    vector<bool> result = solution.checkSubarrayEquality(arr, queries);
    
    for (bool ans : result) {
        cout << (ans ? "true" : "false") << "\n";
    }
    
    return 0;
}
