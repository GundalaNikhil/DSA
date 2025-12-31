#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    void sortWithFixedOnes(vector<int>& arr) {
        int left = 0;
        int right = arr.size() - 1;

        while (left < right) {
            while (left < right && (arr[left] == 0 || arr[left] == 1)) {
                left++;
            }
            while (left < right && (arr[right] == 2 || arr[right] == 1)) {
                right--;
            }

            if (left < right) {
                swap(arr[left], arr[right]);
                left++;
                right--;
            }
        }
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
    solution.sortWithFixedOnes(arr);

    for (size_t i = 0; i < arr.size(); i++) {
        cout << arr[i] << (i == arr.size() - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
