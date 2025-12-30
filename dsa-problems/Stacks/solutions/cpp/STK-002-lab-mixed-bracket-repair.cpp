#include <string>
#include <stack>
#include <vector>

using namespace std;

class Solution {
    bool isMatch(char open, char close) {
        return (open == '(' && close == ')') ||
               (open == '[' && close == ']') ||
               (open == '{' && close == '}');
    }

public:
    bool canRepair(const string& s) {
        int n = s.length();
        if (n % 2 != 0) return false;
        
        vector<int> leftStack;
        vector<int> starStack;
        
        for (int i = 0; i < n; i++) {
            char c = s[i];
            if (c == '(' || c == '[' || c == '{') {
                leftStack.push_back(i);
            } else if (c == '?') {
                starStack.push_back(i);
            } else {
                // Closer
                if (!leftStack.empty() && isMatch(s[leftStack.back()], c)) {
                    leftStack.pop_back();
                } else if (!starStack.empty()) {
                    starStack.pop_back();
                } else {
                    return false;
                }
            }
        }
        
        while (!leftStack.empty()) {
            if (starStack.empty()) return false;
            if (leftStack.back() < starStack.back()) {
                leftStack.pop_back();
                starStack.pop_back();
            } else {
                return false;
            }
        }
        
        return starStack.size() % 2 == 0;
    }
};
