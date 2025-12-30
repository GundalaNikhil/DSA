#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> shuttleShiftBlackout(vector<int>& arr, int k, unordered_set<int>& blackout) {
        vector<int> validIndices;
        vector<int> values;
        
        // Extract
        for (int i = 0; i < arr.size(); i++) {
            if (blackout.find(i) == blackout.end()) {
                validIndices.push_back(i);
                values.push_back(arr[i]);
            }
        }
        
        if (values.empty()) return arr;
        
        // Rotate
        int count = values.size();
        k %= count;
        // std::rotate performs left rotation
        rotate(values.begin(), values.begin() + k, values.end());
        
        // Write Back
        for (int i = 0; i < count; i++) {
            arr[validIndices[i]] = values[i];
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
    
    int k, b;
    cin >> k >> b;
    
    unordered_set<int> blackout;
    for (int i = 0; i < b; i++) {
        int idx;
        cin >> idx;
        blackout.insert(idx);
    }

    Solution solution;
    vector<int> result = solution.shuttleShiftBlackout(arr, k, blackout);
    
    for (int i = 0; i < n; i++) {
        cout << result[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
