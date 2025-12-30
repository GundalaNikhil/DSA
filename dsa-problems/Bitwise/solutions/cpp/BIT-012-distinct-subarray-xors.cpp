#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    long long distinctSubarrayXors(vector<int>& a) {
        int n = a.size();
        long long size = (long long)n * (n + 1) / 2;
        vector<int> results;
        results.reserve(size);
        
        for (int i = 0; i < n; i++) {
            int currentXor = 0;
            for (int j = i; j < n; j++) {
                currentXor ^= a[j];
                results.push_back(currentXor);
            }
        }
        
        sort(results.begin(), results.end());
        
        // Count unique
        if (results.empty()) return 0;
        long long count = 1;
        for (size_t i = 1; i < results.size(); i++) {
            if (results[i] != results[i-1]) {
                count++;
            }
        }
        return count;
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
    cout << solution.distinctSubarrayXors(a) << "\n";
    return 0;
}
