#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> zeroSlideWithLimit(vector<int>& arr, int m) {
        int n = arr.size();
        int writeIdx = 0;

        for (int readIdx = 0; readIdx < n; readIdx++) {
            if (arr[readIdx] != 0) {
                if (readIdx != writeIdx) {
                    if (m <= 0) break;

                    swap(arr[writeIdx], arr[readIdx]);
                    m--;
                }
                writeIdx++;
            }
        }
        return arr;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    int m;
    cin >> m;

    Solution solution;
    vector<int> result = solution.zeroSlideWithLimit(arr, m);

    for (int i = 0; i < n; i++) {
        cout << result[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
