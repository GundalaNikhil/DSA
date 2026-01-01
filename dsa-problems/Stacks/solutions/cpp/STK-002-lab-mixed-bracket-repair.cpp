#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    int countChanges(string s) {
        // Count minimum number of changes to make brackets balanced.
        // Stack tracks unmatched open brackets.
        
        stack<char> st;
        int n = s.length();
        
        string opens = "([{";
        string closes = ")]}";
        map<char, char> pairs;
        pairs[')'] = '(';
        pairs[']'] = '[';
        pairs['}'] = '{';
        
        for (char c : s) {
            if (opens.find(c) != string::npos) {
                st.push(c);
            } else if (closes.find(c) != string::npos) {
                if (!st.empty() && st.top() == pairs[c]) {
                    st.pop();
                } else {
                    st.push(c);
                }
            } else if (c == '?') {
                // Wildcard treated as open bracket as per Python reference?
                // Python: elif c == '?': stack.append('(')
                st.push('(');
            }
        }
        
        // Python logic returns len(stack).
        // This implies each remaining char in stack is an unmatched bracket requiring change.
        return st.size();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    // Read all input until EOF
    string s;
    char c;
    while (cin.get(c)) {
        s += c;
    }
    
    // Trim string (remove trailing newline/whitespace if any)
    while (!s.empty() && isspace(s.back())) s.pop_back();
    while (!s.empty() && isspace(s.front())) s.erase(0, 1);

    if (s.empty()) {
        cout << 0 << endl;
        return 0;
    }

    Solution sol;
    cout << sol.countChanges(s) << endl;
    
    return 0;
}
