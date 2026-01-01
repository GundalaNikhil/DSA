#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> spans(vector<int>& demand) {
        int n = demand.size();
        vector<int> result(n);
        stack<int> st; // Stores indices
        
        for (int i = 0; i < n; i++) {
            while (!st.empty() && demand[st.top()] < demand[i]) {
                st.pop();
            }
            
            if (st.empty()) {
                result[i] = i;
            } else if (demand[st.top()] == demand[i]) {
                result[i] = 0;
            } else {
                result[i] = i - st.top() - 1;
            }
            
            st.push(i);
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> demand(n);
    for (int i = 0; i < n; i++) {
        cin >> demand[i];
    }
    
    Solution sol;
    vector<int> res = sol.spans(demand);
    
    for (int val : res) {
        cout << val << "\n";
    }
    return 0;
}
