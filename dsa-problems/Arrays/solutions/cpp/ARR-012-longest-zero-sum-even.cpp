#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestZeroSumEvenLength(vector<int>& arr) {
        // sum -> pair<first_even_idx, first_odd_idx>
        // Use -2 to signify "not seen" (since -1 is used for base case)
        unordered_map<long long, pair<int, int>> map;

        // Base case: Sum 0 at index -1 (odd)
        map[0] = {-2, -1};

        long long currentSum = 0;
        int maxLen = 0;

        for (int i = 0; i < arr.size(); i++) {
            currentSum += arr[i];
            int parity = i & 1;

            if (map.find(currentSum) == map.end()) {
                map[currentSum] = {-2, -2};
            }

            pair<int, int>& firstSeen = map[currentSum];
            int prevIdx = (parity == 0) ? firstSeen.first : firstSeen.second;

            if (prevIdx != -2) {
                maxLen = max(maxLen, i - prevIdx);
            } else {
                if (parity == 0) firstSeen.first = i;
                else firstSeen.second = i;
            }
        }

        return maxLen;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    Solution solution;
    cout << solution.longestZeroSumEvenLength(arr) << "\n";
    return 0;
}
