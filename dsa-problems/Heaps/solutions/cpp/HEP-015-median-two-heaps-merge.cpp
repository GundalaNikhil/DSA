#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    double findMedian(const vector<int>& maxHeap, const vector<int>& minHeap) {
        vector<int> all;
        all.reserve(maxHeap.size() + minHeap.size());
        all.insert(all.end(), maxHeap.begin(), maxHeap.end());
        all.insert(all.end(), minHeap.begin(), minHeap.end());
        
        if (all.empty()) return 0.0;
        
        // Use nth_element for O(N) performance
        int n = all.size();
        if (n % 2 == 1) {
            auto mid = all.begin() + n / 2;
            nth_element(all.begin(), mid, all.end());
            return (double)*mid;
        } else {
            auto mid1 = all.begin() + n / 2 - 1;
            auto mid2 = all.begin() + n / 2;
            nth_element(all.begin(), mid2, all.end()); // Fixes mid2
            // Now find max of first half for mid1
            int val2 = *mid2;
            int val1 = *max_element(all.begin(), mid2);
            return (double)((long long)val1 + val2) / 2.0;
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    if (cin >> n >> m) {
        vector<int> maxHeap(n), minHeap(m);
        for (int i = 0; i < n; i++) cin >> maxHeap[i];
        for (int i = 0; i < m; i++) cin >> minHeap[i];
        
        Solution solution;
        double res = solution.findMedian(maxHeap, minHeap);
        if (res == (long long)res) {
            cout << (long long)res << "\n";
        } else {
            cout << res << "\n";
        }
    }
    return 0;
}
