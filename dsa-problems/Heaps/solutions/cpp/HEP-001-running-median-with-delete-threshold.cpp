#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_map>

using namespace std;

class Solution {
    priority_queue<int> left; // Max heap
    priority_queue<int, vector<int>, greater<int>> right; // Min heap
    unordered_map<int, int> leftDebt;
    unordered_map<int, int> rightDebt;
    unordered_map<int, int> global_counts;
    int validLeft = 0;
    int validRight = 0;

    void cleanLeft() {
        while (!left.empty() && leftDebt[left.top()] > 0) {
            leftDebt[left.top()]--;
            left.pop();
        }
    }

    void cleanRight() {
        while (!right.empty() && rightDebt[right.top()] > 0) {
            rightDebt[right.top()]--;
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
                    // debt[x]++; // REMOVED
                    
                    cleanLeft();
                    cleanRight();
                    
                    bool inLeft = false;
                    // Decision logic: same as python
                    // if left is not empty and x <= left.top, it belongs to left
                    if (!left.empty() && x <= left.top()) inLeft = true;
                    else inLeft = false;
                    
                    if (inLeft) {
                        leftDebt[x]++;
                        validLeft--;
                    } else {
                        rightDebt[x]++;
                        validRight--;
                    }
                    
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
