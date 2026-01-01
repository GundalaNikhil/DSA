#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int countEvenIndices(const vector<int>& arr, int x) {
        for (int i = 0; i < (int)arr.size(); i++) {
            if (arr[i] == x) {
                return i;
            }
        }
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, x;
    if (!(cin >> n >> x)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution solution;
    cout << solution.countEvenIndices(arr, x) << "\n";
    return 0;
}
