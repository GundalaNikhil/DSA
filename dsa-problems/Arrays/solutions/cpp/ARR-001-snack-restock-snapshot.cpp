#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> prefixAverages(vector<int>& arr) {
        int n = arr.size();
        vector<int> result(n);
        long long sum = 0;  // Use long long to prevent overflow

        for (int i = 0; i < n; i++) {
            sum += arr[i];
            result[i] = sum / (i + 1);  // Integer division by default
        }

        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    Solution solution;
    vector<int> result = solution.prefixAverages(arr);
    
    for (int i = 0; i < n; i++) {
        cout << result[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
