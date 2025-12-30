#include <vector>
#include <algorithm>
#include <map>

using namespace std;

class Solution {
    vector<int> bit;
    int m;

    void update(int idx, int val) {
        for (; idx <= m; idx += idx & -idx) bit[idx] += val;
    }

    int query(int idx) {
        int sum = 0;
        for (; idx > 0; idx -= idx & -idx) sum += bit[idx];
        return sum;
    }

public:
    long long minInversionsAfterSwap(const vector<int>& arr) {
        int n = arr.size();
        vector<int> sorted = arr;
        sort(sorted.begin(), sorted.end());
        sorted.erase(unique(sorted.begin(), sorted.end()), sorted.end());
        
        m = sorted.size();
        bit.assign(m + 2, 0);
        
        long long initialInversions = 0;
        for (int i = n - 1; i >= 0; i--) {
            int rk = lower_bound(sorted.begin(), sorted.end(), arr[i]) - sorted.begin() + 1;
            initialInversions += query(rk - 1);
            update(rk, 1);
        }
        
        long long maxReduction = 0;
        for (int i = 0; i < n - 1; i++) {
            if (arr[i] > arr[i+1]) {
                maxReduction = max(maxReduction, 1LL);
            }
        }
        
        return initialInversions - maxReduction;
    }
};
