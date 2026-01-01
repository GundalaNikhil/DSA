#include <vector>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> closestPair(const vector<int>& arr, int target) {
        vector<int> sorted = arr;
        sort(sorted.begin(), sorted.end());
        int n = sorted.size();
        int left = 0;
        int right = n - 1;
        
        long long minDiff = LLONG_MAX;
        int resLeft = -1;
        int resRight = -1;
        
        while (left < right) {
            long long sum = (long long)sorted[left] + sorted[right];
            long long diff = abs(sum - target);
            
            if (diff < minDiff) {
                minDiff = diff;
                resLeft = sorted[left];
                resRight = sorted[right];
            }
            
            if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        
        return {resLeft, resRight};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, target;
    if (!(cin >> n >> target)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution solution;
    vector<int> result = solution.closestPair(arr, target);
    if (result.size() >= 2) {
        cout << result[0] << " " << result[1] << "\n";
    }
    return 0;
}
