#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <sstream>

using namespace std;

class Solution {
public:
    vector<string> process(const vector<vector<string>>& ops) {
        vector<string> result;
        stack<int> mainStack;
        stack<int> maxStack;
        
        for (const auto& op : ops) {
            string cmd = op[0];
            
            if (cmd == "PUSH") {
                int val = stoi(op[1]);
                mainStack.push(val);
                if (maxStack.empty() || val >= maxStack.top()) {
                    maxStack.push(val);
                }
            } else if (cmd == "POP") {
                if (mainStack.empty()) {
                    result.push_back("EMPTY");
                } else {
                    int val = mainStack.top();
                    mainStack.pop();
                    result.push_back(to_string(val));
                    if (val == maxStack.top()) {
                        maxStack.pop();
                    }
                }
            } else if (cmd == "TOP") {
                if (mainStack.empty()) {
                    result.push_back("EMPTY");
                } else {
                    result.push_back(to_string(mainStack.top()));
                }
            } else if (cmd == "GETMAX") {
                if (mainStack.empty()) {
                    result.push_back("EMPTY");
                } else {
                    result.push_back(to_string(maxStack.top()));
                }
            }
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int m;
    if (!(cin >> m)) return 0;
    
    vector<vector<string>> ops;
    string method;
    
    for (int i = 0; i < m; i++) {
        cin >> method;
        if (method == "PUSH") {
            string val;
            cin >> val;
            ops.push_back({method, val});
        } else {
            ops.push_back({method});
        }
    }
    
    Solution sol;
    vector<string> res = sol.process(ops);
    
    for (const string& s : res) {
        cout << s << "\n";
    }
    
    return 0;
}
