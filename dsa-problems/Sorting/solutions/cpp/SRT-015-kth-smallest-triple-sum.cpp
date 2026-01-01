#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
    long long countLessEqual(const vector<int>& arr, long long target) {
        long long count = 0;
        int n = arr.size();
        for (int i = 0; i < n - 2; i++) {
            if ((long long)arr[i] + arr[i+1] + arr[i+2] > target) break;
            
            if ((long long)arr[i] + arr[n-2] + arr[n-1] <= target) {
                long long remaining = n - 1 - i;
                count += remaining * (remaining - 1) / 2;
                continue;
            }
            
            long long rem = target - arr[i];
            int l = i + 1;
            int r = n - 1;
            while (l < r) {
                if (arr[l] + arr[r] <= rem) {
                    count += (r - l);
                    l++;
                } else {
                    r--;
                }
            }
        }
        return count;
    }

public:
    long long kthTripleSum(vector<int>& arr, long long k) {
        int n = arr.size();
        sort(arr.begin(), arr.end());
        
        long long low = (long long)arr[0] + arr[1] + arr[2];
        long long high = (long long)arr[n-1] + arr[n-2] + arr[n-3];
        long long ans = high;
        
        while (low <= high) {
            long long mid = low + (high - low) / 2;
            if (countLessEqual(arr, mid) >= k) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution solution;
    cout << solution.kthTripleSum(arr, k) << "\n";
    return 0;
}
