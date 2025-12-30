#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    int findNearestGreater(const vector<int>& stack, const vector<int>& arr, int val) {
        if (stack.empty()) return -1;
        
        int l = 0, r = stack.size() - 1;
        int ansIdx = -1;
        
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (arr[stack[mid]] > val) {
                ansIdx = stack[mid];
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return ansIdx;
    }

public:
    vector<int> prevGreaterOppositeParity(const vector<int>& arr) {
        int n = arr.size();
        vector<int> result(n, -1);
        vector<int> evenStack;
        vector<int> oddStack;
        
        for (int i = 0; i < n; i++) {
            int val = arr[i];
            
            if (val % 2 == 0) {
                int idx = findNearestGreater(oddStack, arr, val);
                if (idx != -1) result[i] = arr[idx];
                
                while (!evenStack.empty() && arr[evenStack.back()] <= val) {
                    evenStack.pop_back();
                }
                evenStack.push_back(i);
            } else {
                int idx = findNearestGreater(evenStack, arr, val);
                if (idx != -1) result[i] = arr[idx];
                
                while (!oddStack.empty() && arr[oddStack.back()] <= val) {
                    oddStack.pop_back();
                }
                oddStack.push_back(i);
            }
        }
        return result;
    }
};
