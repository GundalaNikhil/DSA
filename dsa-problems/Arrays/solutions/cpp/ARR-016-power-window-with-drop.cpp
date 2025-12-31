#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    long long maxWindowSumWithDrop(vector<int>& arr, int k) {
        int n = arr.size();
        if (n < k) return 0;
        
        long long currentSum = 0;
        for (int i = 0; i < k; i++) {
            currentSum += arr[i];
        }
        
        long long maxTotal = currentSum;
        
        for (int i = k; i < n; i++) {
            currentSum += arr[i];
            currentSum -= arr[i - k];
            maxTotal = max(maxTotal, currentSum);
        }
        
        return maxTotal;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    
    int k;
    cin >> k;

    Solution solution;
    cout << solution.maxWindowSumWithDrop(arr, k) << "\n";
    return 0;
}
