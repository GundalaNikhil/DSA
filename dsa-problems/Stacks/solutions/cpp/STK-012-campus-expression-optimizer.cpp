#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <map>

using namespace std;

class Solution {
public:
    string solve(const string& expr) {
        string postfix = "";
        stack<char> ops;
        int redundant = 0;
        
        map<char, int> prec;
        prec['+'] = 1; prec['-'] = 1;
        prec['*'] = 2; prec['/'] = 2; prec['%'] = 2;
        prec['^'] = 3;
        prec['('] = 0;
        
        int lastType = 0; // 0: Start, 1: Operand, 2: Operator, 3: Open, 4: Close
        
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
                    postfix += ops.top();
                    ops.pop();
                    hasOp = true;
                }
                
                if (ops.empty()) return "ERROR Mismatched parentheses 0";
                ops.pop();
                
                if (!hasOp) redundant++;
                
                lastType = 4;
            } else if (prec.count(c)) {
                if (lastType == 0 || lastType == 2 || lastType == 3) return "ERROR Invalid syntax 0";
                
                while (!ops.empty() && ops.top() != '(' && 
                       (prec[ops.top()] > prec[c] || 
                       (prec[ops.top()] == prec[c] && c != '^'))) {
                    postfix += ops.top();
                    ops.pop();
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
            postfix += ops.top();
            ops.pop();
        }
        
        return "POSTFIX " + postfix + " " + to_string(redundant);
    }
};
