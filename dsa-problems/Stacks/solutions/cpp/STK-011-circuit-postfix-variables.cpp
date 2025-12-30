#include <vector>
#include <string>
#include <stack>
#include <unordered_map>

using namespace std;

class Solution {
    long long MOD = 1000000007;
    
    bool isNumber(const string& s) {
        if (s.empty()) return false;
        if (isdigit(s[0])) return true;
        if (s.size() > 1 && s[0] == '-' && isdigit(s[1])) return true;
        return false;
    }

public:
    long long eval(const vector<string>& tokens, const unordered_map<string, long long>& vars) {
        stack<long long> st;
        
        for (const string& token : tokens) {
            if (vars.count(token)) {
                st.push((vars.at(token) % MOD + MOD) % MOD); // Normalize input
            } else if (isNumber(token)) {
                st.push((stoll(token) % MOD + MOD) % MOD);
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
                
                if (token == "+") res = (a + b) % MOD;
                else if (token == "-") res = (a - b + MOD) % MOD;
                else if (token == "*") res = (a * b) % MOD;
                else if (token == "/") res = a / b;
                else if (token == "%") res = a % b;
                
                st.push(res);
            }
        }
        return st.top();
    }
};
