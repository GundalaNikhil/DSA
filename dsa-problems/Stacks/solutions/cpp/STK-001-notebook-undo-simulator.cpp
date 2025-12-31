#include <vector>
#include <string>
#include <stack>

using namespace std;

class Solution {
public:
    vector<string> process(const vector<vector<string>>& ops) {
        vector<string> result;
        stack<string> s;
        
        for (const auto& op : ops) {
            string command = op[0];
            
            if (command == "PUSH") {
                s.push(op[1]);
            } else if (command == "POP") {
                if (s.empty()) {
                    result.push_back("EMPTY");
                } else {
                    result.push_back(s.top());
                    s.pop();
                }
            } else if (command == "TOP") {
                if (s.empty()) {
                    result.push_back("EMPTY");
                } else {
                    result.push_back(s.top());
                }
            }
        }
        return result;
    }
};
