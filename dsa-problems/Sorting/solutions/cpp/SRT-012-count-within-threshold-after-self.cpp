#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<long long> countWithinThreshold(const vector<int>& arr, long long T) {
        int n = arr.size();
        vector<long long> counts(n, 0);

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if ((long long)arr[j] - (long long)arr[i] <= T) {
                    counts[i]++;
                }
            }
        }

        return counts;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long t;
    if (!(cin >> n >> t)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution solution;
    vector<long long> result = solution.countWithinThreshold(arr, t);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << ' ';
        cout << result[i];
    }
    cout << "\n";
    return 0;
}
