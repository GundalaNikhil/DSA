#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    long long solve(const vector<int>& arr) {
        if (arr.empty()) {
            return 0;
        }

        // Find first negative
        int firstNegIdx = -1;
        int firstNegVal = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] < 0) {
                firstNegIdx = i;
                firstNegVal = arr[i];
                break;
            }
        }

        if (firstNegIdx == -1) {
            // No negative found - return sum modulo 100
            long long sum = 0;
            for (int val : arr) {
                sum += val;
            }
            return sum % 100;
        }

        // With first negative found
        // Compute: sum of elements up to first negative + first negative value
        long long prefixSum = 0;
        for (int i = 0; i < firstNegIdx; i++) {
            prefixSum += arr[i];
        }
        return prefixSum + firstNegVal;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        Solution solution;
        long long result = solution.solve(arr);
        cout << result << "\n";
    }
    return 0;
}
