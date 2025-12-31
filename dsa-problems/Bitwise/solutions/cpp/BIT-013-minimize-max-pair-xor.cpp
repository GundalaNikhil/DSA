#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

class Solution {
    int memo[1 << 16];
    int n;
    vector<int> a;

    int solve(int mask) {
        if (mask == (1 << n) - 1) return 0;
        if (memo[mask] != -1) return memo[mask];

        int res = 2e9;
        
        // Find first unset
        int i = 0;
        while ((mask >> i) & 1) i++;
        
        for (int j = i + 1; j < n; j++) {
            if (!((mask >> j) & 1)) {
                int val = a[i] ^ a[j];
                int sub = solve(mask | (1 << i) | (1 << j));
                res = min(res, max(val, sub));
            }
        }
        return memo[mask] = res;
    }

public:
    int minimizeMaxPairXor(vector<int>& a) {
        this->a = a;
        this->n = a.size();
        memset(memo, -1, sizeof(memo));
        return solve(0);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    Solution solution;
    cout << solution.minimizeMaxPairXor(a) << "\n";
    return 0;
}
