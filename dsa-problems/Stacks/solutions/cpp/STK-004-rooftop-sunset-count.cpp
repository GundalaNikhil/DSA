#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <sstream>

using namespace std;

class Solution {
    bool isSmaller(const string& a, const string& b) {
        if (a.length() != b.length()) {
            return a.length() < b.length();
        }
        return a < b;
    }

public:
    int countVisible(vector<string>& h) {
        int n = h.size();
        stack<int> st; // Stores indices
        int count = 0;
        
        for (int i = n - 1; i >= 0; i--) {
            while (!st.empty() && isSmaller(h[st.top()], h[i])) {
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
    
    string line;
    // Read N (line 1)
    if (!getline(cin, line)) return 0;
    
    // Read Array (line 2)
    if (!getline(cin, line)) return 0;
    
    stringstream ss(line);
    string val;
    vector<string> h;
    while (ss >> val) {
        h.push_back(val);
    }
    
    Solution sol;
    cout << sol.countVisible(h) << endl;
    
    return 0;
}
