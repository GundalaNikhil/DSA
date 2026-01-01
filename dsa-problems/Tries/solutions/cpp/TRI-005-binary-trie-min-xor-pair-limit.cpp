#include <iostream>
#include <vector>
#include <climits>

using namespace std;

class Solution {
public:
    int minXORPairUnderLimit(const vector<int>& arr, int L) {
        int n = static_cast<int>(arr.size());
        int minXor = INT_MAX;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int xorVal = arr[i] ^ arr[j];
                if (xorVal <= L) {
                    if (xorVal < minXor) {
                        minXor = xorVal;
                    }
                }
            }
        }

        return minXor == INT_MAX ? -1 : minXor;
    }
};

int main() {
    int n, L;
    if (!(cin >> n >> L)) {
        return 0;
    }
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    Solution solution;
    int result = solution.minXORPairUnderLimit(arr, L);

    cout << result << '\n';
    return 0;
}
