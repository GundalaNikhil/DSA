#include <vector>
using namespace std;

class Solution {
public:
    int findPeak(const vector<int>& arr, int qLimit) {
        int n = arr.size();
        int low = 0;
        int high = n - 1;
        
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] < arr[mid+1]) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
};
