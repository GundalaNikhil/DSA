#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <map>
#include <sstream>

using namespace std;

class Solution {
    long long MOD = 1000000007;
    
    bool isNumber(const string& s) {
        if (s.empty()) return false;
        size_t i = 0;
        if (s[0] == '-') i = 1;
        if (i == s.length()) return false;
        for (; i < s.length(); i++) {
            if (!isdigit(s[i])) return false;
        }
        return true;
    }
    
    long long pythonMod(long long a, long long b) {
        return ((a % b) + b) % b;
    }
    
    long long pythonDiv(long long a, long long b) {
        long long res = a / b;
        if ((a < 0) != (b < 0) && (a % b != 0)) {
            res--;
        }
        return res;
    }

public:
    long long evalPostfix(vector<string>& tokens, map<string, int>& vars) {
        stack<long long> st;
        
        for (const string& token : tokens) {
            if (vars.count(token)) {
                st.push(vars[token] % MOD);
            } else if (isNumber(token)) {
                st.push(stoll(token) % MOD);
            } else if (token == "DUP") {
                st.push(st.top());
            } else if (token == "SWAP") {
                long long a = st.top(); st.pop();
                long long b = st.top(); st.pop();
                st.push(a);
                st.push(b);
            } else {
                long long b = st.top(); st.pop();
                long long a = st.top(); st.pop();
                long long res = 0;
                
                if (token == "+") {
                    res = (a + b) % MOD;
                } else if (token == "-") {
                    res = (a - b + MOD) % MOD;
                } else if (token == "*") {
                    res = (a * b) % MOD;
                } else if (token == "/") {
                    res = pythonDiv(a, b);
                } else if (token == "%") {
                    res = pythonMod(a, b);
                }
                st.push(res);
            }
        }
        return st.top();
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int numVars;
    if (!(cin >> numVars)) return 0;
    
    map<string, int> vars;
    for (int i = 0; i < numVars; i++) {
        string name;
        int val;
        cin >> name >> val;
        vars[name] = val;
    }
    
    string line;
    getline(cin >> ws, line); // Consume newline and read line
    // Wait, cin >> ws consumes whitespace.
    // If expr is on next line, this works.
    
    stringstream ss(line);
    string token;
    vector<string> tokens;
    while (ss >> token) {
        tokens.push_back(token);
    }
    
    Solution sol;
    cout << sol.evalPostfix(tokens, vars) << endl;
    
    return 0;
}
