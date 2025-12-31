#include <iostream>
#include <vector>
#include <numeric>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
    int gcd(int a, int b) {
        while (b) {
            a %= b;
            swap(a, b);
        }
        return a;
    }

public:
    vector<int> prefixGcds(const vector<int>& a) {
        int n = a.size();
        if (n == 0) return {};
        
        vector<int> pref(n);
        pref[0] = abs(a[0]);
        
        for (int i = 1; i < n; i++) {
            pref[i] = gcd(pref[i - 1], abs(a[i]));
        }
        
        return pref;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    Solution solution;
    vector<int> pref = solution.prefixGcds(a);
    
    for (int i = 0; i < q; i++) {
        int r;
        cin >> r;
        cout << pref[r] << "\n";
    }
    return 0;
}
