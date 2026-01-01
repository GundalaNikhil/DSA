#include <vector>
#include <algorithm>
#include <utility>

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
