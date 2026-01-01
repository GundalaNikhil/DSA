#include <vector>

using namespace std;

class Solution {
public:
    int findPeak(const vector<int>& arr, int qLimit) {
        int n = arr.size();
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 0;
        }
        if (arr[0] > arr[1]) {
            return 0;
        }
        for (int i = 1; i < n - 1; i++) {
            if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
                return i;
            }
        }
        if (arr[n - 1] > arr[n - 2]) {
            return n - 1;
        }
        return 0;
    }
};
