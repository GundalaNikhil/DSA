#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> nextTallerWithin(vector<int>& h, int w) {
        int n = h.size();
        vector<int> result(n, -1);
        stack<int> st; // Indices
        
        for (int i = n - 1; i >= 0; i--) {
            while (!st.empty() && h[st.top()] <= h[i]) {
                st.pop();
            }
            
            if (!st.empty()) {
                int j = st.top();
                if (j - i <= w) {
                    result[i] = h[j];
                }
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
    
    vector<int> h(n);
    for (int i = 0; i < n; i++) {
        cin >> h[i];
    }
    
    int w;
    cin >> w;
    
    Solution sol;
    vector<int> res = sol.nextTallerWithin(h, w);
    
    for (int val : res) {
        cout << val << "\n";
    }
    
    return 0;
}
