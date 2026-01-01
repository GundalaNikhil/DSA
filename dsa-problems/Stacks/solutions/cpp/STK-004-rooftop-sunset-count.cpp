#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    int countVisible(vector<long long>& h) {
        int n = h.size();
        stack<int> st; // Stores indices
        int count = 0;
        
        for (int i = n - 1; i >= 0; i--) {
            while (!st.empty() && h[st.top()] < h[i]) {
                st.pop();
            }
            
            if (st.empty()) {
                count++;
            }
            
            st.push(i);
        }
        return count;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<long long> h(n);
    for (int i = 0; i < n; i++) {
        cin >> h[i];
    }
    
    Solution sol;
    cout << sol.countVisible(h) << endl;
    
    return 0;
}
