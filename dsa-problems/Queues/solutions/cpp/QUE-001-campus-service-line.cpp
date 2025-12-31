#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

class Solution {
public:
    vector<string> processCommands(const vector<vector<string>>& commands) {
        queue<string> q;
        vector<string> result;
        
        for (const auto& cmd : commands) {
            const string& op = cmd[0];
            if (op == "ENQUEUE") {
                q.push(cmd[1]);
            } else if (op == "DEQUEUE") {
                if (q.empty()) {
                    result.push_back("EMPTY");
                } else {
                    result.push_back(q.front());
                    q.pop();
                }
            } else if (op == "FRONT") {
                if (q.empty()) {
                    result.push_back("EMPTY");
                } else {
                    result.push_back(q.front());
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
    if (cin >> m) {
        vector<vector<string>> commands;
        commands.reserve(m);
        for (int i = 0; i < m; i++) {
            string op;
            cin >> op;
            if (op == "ENQUEUE") {
                string val;
                cin >> val;
                commands.push_back({op, val});
            } else {
                commands.push_back({op});
            }
        }
    
        Solution solution;
        vector<string> result = solution.processCommands(commands);
        for (const string& line : result) {
            cout << line << "\n";
        }
    }
    return 0;
}
