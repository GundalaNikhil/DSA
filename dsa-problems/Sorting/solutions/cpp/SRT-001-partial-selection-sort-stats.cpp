#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> partialSelectionSort(vector<int> arr, int k) {
        int n = arr.size();
        for (int i = 0; i < k; i++) {
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            swap(arr[i], arr[minIndex]);
        }
        return arr;
    }
};
