#include <vector>
#include <string>
#include <stack>
#include <iostream>

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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    if (!(cin >> m)) return 0;
    vector<vector<string>> ops;
    ops.reserve(m);
    for (int i = 0; i < m; i++) {
        string op;
        cin >> op;
        if (op == "PUSH") {
            string x;
            cin >> x;
            ops.push_back({op, x});
        } else {
            ops.push_back({op});
        }
    }

    Solution solution;
    vector<string> out = solution.process(ops);
    for (const string& s : out) cout << s << "\n";
    return 0;
}
