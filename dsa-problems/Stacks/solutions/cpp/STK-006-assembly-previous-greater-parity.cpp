#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
    int findNearestGreater(const vector<int>& stack, int val, const vector<int>& arr) {
        if (stack.empty()) return -1;
        
        int l = 0, r = stack.size() - 1;
        int ansIdx = -1;
        
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int idx = stack[mid];
            if (arr[idx] > val) {
                ansIdx = idx;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return ansIdx;
    }

public:
    vector<int> prevGreaterOppositeParity(vector<int>& arr) {
        int n = arr.size();
        vector<int> result(n, -1);
        
        vector<int> evenStack;
        vector<int> oddStack;
        
        for (int i = 0; i < n; i++) {
            int val = arr[i];
            
            if (val % 2 == 0) {
                // Look in Odd
                int idx = findNearestGreater(oddStack, val, arr);
                if (idx != -1) result[i] = arr[idx];
                
                // Update Even
                while (!evenStack.empty() && arr[evenStack.back()] <= val) {
                    evenStack.pop_back();
                }
                evenStack.push_back(i);
            } else {
                // Look in Even
                int idx = findNearestGreater(evenStack, val, arr);
                if (idx != -1) result[i] = arr[idx];
                
                // Update Odd
                while (!oddStack.empty() && arr[oddStack.back()] <= val) {
                    oddStack.pop_back();
                }
                oddStack.push_back(i);
            }
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
    
    Solution sol;
    vector<int> res = sol.prevGreaterOppositeParity(arr);
    
    for (int val : res) {
        cout << val << "\n";
    }
    
    return 0;
}
