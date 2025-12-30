#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    void benchFlipLockedEnds(vector<int>& arr) {
        int n = arr.size();
        if (n < 3) return;
        
        int left = 1;
        int right = n - 2;
        
        while (left < right) {
            swap(arr[left], arr[right]);
            left++;
            right--;
        }
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
    solution.benchFlipLockedEnds(arr);
    
    for (int i = 0; i < n; i++) {
        cout << arr[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
    return 0;
}
