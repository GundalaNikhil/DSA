#include <vector>
#include <cstdlib>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> closestPairCircular(const vector<int>& arr, int target) {
        int n = arr.size();
        if (n == 0) {
            return {};
        }
        if (n == 1) {
            return {0, 0};
        }

        int minIdx = 0;
        int minDiff = abs(arr[0] - arr[1]);
        for (int i = 0; i < n; i++) {
            int next = (i + 1) % n;
            int diff = abs(arr[i] - arr[next]);
            if (diff < minDiff) {
                minDiff = diff;
                minIdx = i;
            }
        }

        int a = minIdx;
        int b = (minIdx + 1) % n;
        if (a > b) {
            int tmp = a;
            a = b;
            b = tmp;
        }
        return {a, b};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution solution;
    vector<int> result = solution.closestPairCircular(arr, 0);
    if (result.size() >= 2) {
        cout << result[0] << " " << result[1] << "\n";
    }
    return 0;
}
