#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool hasPairWithForbidden(vector<int>& arr, int target, unordered_set<int>& forbidden) {
        int left = 0;
        int right = arr.size() - 1;

        while (left < right) {
            if (forbidden.count(left)) {
                left++;
                continue;
            }
            if (forbidden.count(right)) {
                right--;
                continue;
            }

            long long sum = (long long)arr[left] + arr[right];

            if (sum == target) {
                return true;
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }

        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    int target, f;
    cin >> target >> f;

    unordered_set<int> forbidden;
    for (int i = 0; i < f; i++) {
        int idx;
        cin >> idx;
        forbidden.insert(idx);
    }

    Solution solution;
    cout << (solution.hasPairWithForbidden(arr, target, forbidden) ? "true" : "false") << "\n";
    return 0;
}
