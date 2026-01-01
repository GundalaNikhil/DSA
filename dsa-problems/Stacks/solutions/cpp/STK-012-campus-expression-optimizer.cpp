#include <iostream>
#include <string>
#include <stack>
#include <map>
#include <cctype>

using namespace std;

class Solution {
    map<char, int> prec;

public:
    Solution() {
        prec['+'] = 1; prec['-'] = 1;
        prec['*'] = 2; prec['/'] = 2; prec['%'] = 2;
        prec['^'] = 3;
        prec['('] = 0;
    }

    string solve(string expr) {
        string postfix = "";
        stack<char> ops;
        int redundant = 0;
        
        // 0: Start, 1: Operand, 2: Operator, 3: Open, 4: Close
        int lastType = 0;
        
        for (char c : expr) {
            if (isalnum(c)) {
                if (lastType == 1 || lastType == 4) return "ERROR Invalid syntax 0";
                postfix += c;
                lastType = 1;
            } else if (c == '(') {
                if (lastType == 1 || lastType == 4) return "ERROR Invalid syntax 0";
                ops.push(c);
                lastType = 3;
            } else if (c == ')') {
                if (lastType == 0 || lastType == 2 || lastType == 3) return "ERROR Invalid syntax 0";
                
                bool hasOp = false;
                while (!ops.empty() && ops.top() != '(') {
                    postfix += ops.top(); ops.pop();
                    hasOp = true;
                }
                
                if (ops.empty()) return "ERROR Mismatched parentheses 0";
                ops.pop(); // Pop '('
                
                if (!hasOp) {
                    redundant++;
                }
                lastType = 4;
            } else if (prec.count(c)) {
                if (lastType == 0 || lastType == 2 || lastType == 3) return "ERROR Invalid syntax 0";
                
                while (!ops.empty() && ops.top() != '(' &&
                       (prec[ops.top()] > prec[c] ||
                       (prec[ops.top()] == prec[c] && c != '^'))) {
                    postfix += ops.top(); ops.pop();
                }
                ops.push(c);
                lastType = 2;
            } else {
                return "ERROR Invalid character 0";
            }
        }
        
        if (lastType == 0 || lastType == 2 || lastType == 3) return "ERROR Invalid syntax 0";
        
        while (!ops.empty()) {
            if (ops.top() == '(') return "ERROR Mismatched parentheses 0";
            postfix += ops.top(); ops.pop();
        }
        
        return "POSTFIX " + postfix + " " + to_string(redundant);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string expr;
    if (getline(cin, expr)) {
        // Trim right usage of trailing newlines if any
        while (!expr.empty() && isspace(expr.back())) expr.pop_back();
        while (!expr.empty() && isspace(expr.front())) expr.erase(0, 1);
        
        Solution sol;
        cout << sol.solve(expr) << endl;
    }
    
    return 0;
}
