#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

class Solution {
public:
    string processQueueOperations(const vector<vector<string>>& operations) {
        queue<int> q;
        long long total = 0;

        for (const auto& opData : operations) {
            const string& cmd = opData[0];

            if (cmd == "ENQUEUE") {
                q.push(stoi(opData[1]));
            } else if (cmd == "DEQUEUE") {
                if (!q.empty()) {
                    q.pop();
                }
            } else if (cmd == "FRONT") {
                // Just read
            } else if (cmd == "REAR") {
                // Just read
            } else if (cmd == "SIZE") {
                total += q.size();
            } else if (cmd == "ISEMPTY") {
                // Just read
            }
        }

        return to_string(total);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m;
    if (cin >> m) {
        vector<vector<string>> operations;
        operations.reserve(m);

        for (int i = 0; i < m; i++) {
            string op;
            cin >> op;
            if (op == "ENQUEUE") {
                string val;
                cin >> val;
                operations.push_back({op, val});
            } else {
                operations.push_back({op});
            }
        }

        Solution solution;
        string result = solution.processQueueOperations(operations);
        cout << result << "\n";
    }
    return 0;
}
