#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <unordered_map>
#include <set>

using namespace std;

// Use multiset for easier deletion in C++
struct Group {
    multiset<int> left, right;
    
    void add(int val) {
        if (left.empty() || val <= *left.rbegin()) {
            left.insert(val);
        } else {
            right.insert(val);
        }
        rebalance();
    }
    
    void rebalance() {
        while (left.size() > right.size() + 1) {
            right.insert(*left.rbegin());
            left.erase(prev(left.end()));
        }
        while (right.size() > left.size()) {
            left.insert(*right.begin());
            right.erase(right.begin());
        }
    }
    
    int getMedian() {
        if (left.empty()) return 0;
        return *left.rbegin();
    }
    
    int size() { return left.size() + right.size(); }
    
    void mergeFrom(Group& other) {
        for (int x : other.left) add(x);
        for (int x : other.right) add(x);
        other.left.clear();
        other.right.clear();
    }
};

class Solution {
    unordered_map<string, Group> groups;
    multiset<int> gLeft, gRight;
    
    void addToGlobal(int val) {
        if (gLeft.empty() || val <= *gLeft.rbegin()) {
            gLeft.insert(val);
        } else {
            gRight.insert(val);
        }
        rebalanceGlobal();
    }
    
    void removeFromGlobal(int val) {
        auto it = gLeft.find(val);
        if (it != gLeft.end()) {
            gLeft.erase(it);
        } else {
            it = gRight.find(val);
            if (it != gRight.end()) gRight.erase(it);
        }
        rebalanceGlobal();
    }
    
    void rebalanceGlobal() {
        while (gLeft.size() > gRight.size() + 1) {
            gRight.insert(*gLeft.rbegin());
            gLeft.erase(prev(gLeft.end()));
        }
        while (gRight.size() > gLeft.size()) {
            gLeft.insert(*gRight.begin());
            gRight.erase(gRight.begin());
        }
    }
    
public:
    vector<string> processOperations(const vector<vector<string>>& operations) {
        vector<string> results;
        
        for (const auto& op : operations) {
            if (op[0] == "NEW") {
                string id = op[1];
                Group g;
                for (size_t i = 2; i < op.size(); i++) {
                    g.add(stoi(op[i]));
                }
                groups[id] = g;
                if (g.size() > 0) addToGlobal(g.getMedian());
                
            } else if (op[0] == "ADD") {
                string id = op[1];
                int x = stoi(op[2]);
                if (groups.count(id)) {
                    if (groups[id].size() > 0) removeFromGlobal(groups[id].getMedian());
                    groups[id].add(x);
                    if (groups[id].size() > 0) addToGlobal(groups[id].getMedian());
                }
                
            } else if (op[0] == "MERGE") {
                string id1 = op[1];
                string id2 = op[2];
                if (groups.count(id1) && groups.count(id2)) {
                    if (groups[id1].size() > 0) removeFromGlobal(groups[id1].getMedian());
                    if (groups[id2].size() > 0) removeFromGlobal(groups[id2].getMedian());
                    
                    if (groups[id1].size() < groups[id2].size()) {
                        groups[id2].mergeFrom(groups[id1]);
                        groups[id1] = move(groups[id2]); // Move content
                    } else {
                        groups[id1].mergeFrom(groups[id2]);
                    }
                    groups.erase(id2);
                    if (groups[id1].size() > 0) addToGlobal(groups[id1].getMedian());
                }
                
            } else if (op[0] == "QUERY") {
                if (gLeft.empty()) results.push_back("EMPTY");
                else results.push_back(to_string(*gLeft.rbegin()));
            }
        }
        return results;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int q;
    if (cin >> q) {
        vector<vector<string>> operations;
        for (int i = 0; i < q; i++) {
            string op;
            cin >> op;
            if (op == "NEW") {
                string gid;
                int m;
                cin >> gid >> m;
                vector<string> line = {op, gid};
                for (int j = 0; j < m; j++) {
                    string x;
                    cin >> x;
                    line.push_back(x);
                }
                operations.push_back(line);
            } else if (op == "ADD") {
                string gid, x;
                cin >> gid >> x;
                operations.push_back({op, gid, x});
            } else if (op == "MERGE") {
                string gid1, gid2;
                cin >> gid1 >> gid2;
                operations.push_back({op, gid1, gid2});
            } else {
                operations.push_back({op});
            }
        }
        
        Solution solution;
        vector<string> result = solution.processOperations(operations);
        for (const string& s : result) cout << s << "\n";
    }
    return 0;
}
