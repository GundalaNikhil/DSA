#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> processOperations(int k, const vector<vector<string>>& operations) {
        vector<int> buffer(k);
        int head = 0;
        int tail = 0;
        int count = 0;
        vector<string> result;
        
        for (const auto& op_data : operations) {
            const string& cmd = op_data[0];
            
            if (cmd == "ENQ") {
                if (count == k) {
                    result.push_back("false");
                } else {
                    buffer[tail] = stoi(op_data[1]);
                    tail = (tail + 1) % k;
                    count++;
                    result.push_back("true");
                }
            } else if (cmd == "ENQ_OVR") {
                int val = stoi(op_data[1]);
                if (count == k) {
                    // Overwrite and return the overwritten value
                    int overwritten = buffer[head];
                    buffer[head] = val;
                    head = (head + 1) % k;
                    tail = (tail + 1) % k;
                    result.push_back(to_string(overwritten));
                } else {
                    // Just add
                    buffer[tail] = val;
                    tail = (tail + 1) % k;
                    count++;
                    result.push_back("NONE");
                }
            } else if (cmd == "DEQ") {
                if (count == 0) {
                    result.push_back("EMPTY");
                } else {
                    result.push_back(to_string(buffer[head]));
                    head = (head + 1) % k;
                    count--;
                }
            } else if (cmd == "FRONT") {
                if (count == 0) result.push_back("EMPTY");
                else result.push_back(to_string(buffer[head]));
            } else if (cmd == "REAR") {
                if (count == 0) result.push_back("EMPTY");
                else {
                    int idx = (tail - 1 + k) % k;
                    result.push_back(to_string(buffer[idx]));
                }
            } else if (cmd == "ISEMPTY") {
                result.push_back(count == 0 ? "true" : "false");
            } else if (cmd == "ISFULL") {
                result.push_back(count == k ? "true" : "false");
            } else if (cmd == "SIZE") {
                result.push_back(to_string(count));
            }
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k, m;
    if (cin >> k >> m) {
        vector<vector<string>> operations;
        operations.reserve(m);
        for (int i = 0; i < m; i++) {
            string op;
            cin >> op;
            if (op == "ENQ" || op == "ENQ_OVR") {
                string val;
                cin >> val;
                operations.push_back({op, val});
            } else {
                operations.push_back({op});
            }
        }
    
        Solution solution;
        vector<string> result = solution.processOperations(k, operations);
        for (const string& line : result) {
            cout << line << "\n";
        }
    }
    return 0;
}
