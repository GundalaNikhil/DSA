#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    bool sortWithSwaps(const vector<int>& arr, long long S) {
        int n = arr.size();
        int count0 = 0;
        int count1 = 0;
        for (int v : arr) {
            if (v == 0) {
                count0++;
            } else if (v == 1) {
                count1++;
            }
        }

        int misplaced = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] == 0 && i >= count0) {
                misplaced++;
            } else if (arr[i] == 1 && (i < count0 || i >= count0 + count1)) {
                misplaced++;
            } else if (arr[i] == 2 && i < count0 + count1) {
                misplaced++;
            }
        }

        long long swapsNeeded = misplaced / 2;
        return swapsNeeded <= S;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long s;
    if (!(cin >> n >> s)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution solution;
    bool ok = solution.sortWithSwaps(arr, s);
    cout << (ok ? "YES" : "NO") << "\n";
    return 0;
}
