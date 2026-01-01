#include <vector>
#include <algorithm>
#include <utility>
#include <iostream>

using namespace std;

class Solution {
public:
    long long minSwapsToSort(const vector<int>& arr, int k) {
        int n = arr.size();
        vector<pair<int, int>> pairs(n);
        for (int i = 0; i < n; i++) {
            pairs[i] = {arr[i], i};
        }

        stable_sort(pairs.begin(), pairs.end(),
                    [](const pair<int, int>& a, const pair<int, int>& b) {
                        return a.first < b.first;
                    });

        long long violations = 0;
        for (int targetIdx = 0; targetIdx < n; targetIdx++) {
            int originalIdx = pairs[targetIdx].second;
            if (abs(targetIdx - originalIdx) > k) {
                violations++;
            }
        }

        return violations / 2;
    }

    long long minSwapsToSort(const vector<int>& arr) {
        return minSwapsToSort(arr, 0);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution solution;
    cout << solution.minSwapsToSort(arr, k) << "\n";
    return 0;
}
