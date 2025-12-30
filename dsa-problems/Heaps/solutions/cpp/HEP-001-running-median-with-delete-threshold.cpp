#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_map>

using namespace std;

class Solution {
    priority_queue<int> left; // Max heap
    priority_queue<int, vector<int>, greater<int>> right; // Min heap
    unordered_map<int, int> debt;
    unordered_map<int, int> global_counts;
    int validLeft = 0;
    int validRight = 0;

    void cleanLeft() {
        while (!left.empty() && debt[left.top()] > 0) {
            debt[left.top()]--;
            left.pop();
        }
    }

    void cleanRight() {
        while (!right.empty() && debt[right.top()] > 0) {
            debt[right.top()]--;
            right.pop();
        }
    }

    void rebalance() {
        while (validLeft > validRight + 1) {
            cleanLeft();
            int val = left.top(); left.pop();
            validLeft--;
            right.push(val);
            validRight++;
        }
        while (validRight > validLeft) {
            cleanRight();
            int val = right.top(); right.pop();
            validRight--;
            left.push(val);
            validLeft++;
        }
        cleanLeft();
        cleanRight();
    }

public:
    vector<string> processOperations(int T, const vector<vector<string>>& operations) {
        vector<string> results;
        
        for (const auto& op : operations) {
            if (op[0] == "ADD") {
                int x = stoi(op[1]);
                global_counts[x]++;
                
                cleanLeft();
                if (left.empty() || x <= left.top()) {
                    left.push(x);
                    validLeft++;
                } else {
                    right.push(x);
                    validRight++;
                }
                rebalance();
            } else if (op[0] == "DEL") {
                int x = stoi(op[1]);
                if (global_counts[x] > 0) {
                    global_counts[x]--;
                    debt[x]++;
                    
                    cleanLeft();
                    cleanRight();
                    
                    bool inLeft = false;
                    if (!left.empty() && x <= left.top()) inLeft = true;
                    else if (!right.empty() && x >= right.top()) inLeft = false;
                    else {
                        if (!left.empty()) inLeft = true;
                        else inLeft = false;
                    }
                    
                    if (inLeft) validLeft--;
                    else validRight--;
                    
                    rebalance();
                }
            } else {
                cleanLeft();
                int total = validLeft + validRight;
                if (total == 0) results.push_back("EMPTY");
                else if (total < T) results.push_back("NA");
                else results.push_back(to_string(left.top()));
            }
        }
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int q, T;
    if (cin >> q >> T) {
        vector<vector<string>> operations;
        for (int i = 0; i < q; i++) {
            string op;
            cin >> op;
            if (op == "ADD" || op == "DEL") {
                string x;
                cin >> x;
                operations.push_back({op, x});
            } else {
                operations.push_back({op});
            }
        }
        
        Solution solution;
        vector<string> result = solution.processOperations(T, operations);
        for (const string& s : result) cout << s << "\n";
    }
    return 0;
}
