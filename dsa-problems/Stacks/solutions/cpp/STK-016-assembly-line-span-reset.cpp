#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> spans(vector<int>& counts) {
        int n = counts.size();
        vector<int> result(n);
        stack<int> stack;
        
        for (int i = 0; i < n; i++) {
            while (!stack.empty() && counts[stack.top()] < counts[i]) {
                stack.pop();
            }
            
            if (stack.empty()) {
                result[i] = i + 1;
            } else {
                result[i] = i - stack.top();
            }
            stack.push(i);
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> counts(n);
    for (int i = 0; i < n; i++) {
        cin >> counts[i];
    }
    
    Solution sol;
    vector<int> res = sol.spans(counts);
    
    for (int val : res) {
        cout << val << "\n";
    }
    
    return 0;
}
