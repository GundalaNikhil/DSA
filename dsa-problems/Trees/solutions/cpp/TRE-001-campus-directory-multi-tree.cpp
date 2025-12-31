#include <iostream>
#include <vector>
#include <string>
#include <array>
#include <algorithm>

using namespace std;

class Solution {
    void dfs(int u, const vector<array<int, 3>>& nodes, 
             vector<int>& pre, vector<int>& in, vector<int>& post) {
        if (u == -1) return;
        
        pre.push_back(nodes[u][0]);
        dfs(nodes[u][1], nodes, pre, in, post);
        in.push_back(nodes[u][0]);
        dfs(nodes[u][2], nodes, pre, in, post);
        post.push_back(nodes[u][0]);
    }

    bool checkStruct(int u1, const vector<array<int, 3>>& t1,
                     int u2, const vector<array<int, 3>>& t2) {
        if (u1 == -1 && u2 == -1) return true;
        if (u1 == -1 || u2 == -1) return false;
        
        // Check children existence
        bool l1 = t1[u1][1] != -1;
        bool l2 = t2[u2][1] != -1;
        if (l1 != l2) return false;
        
        bool r1 = t1[u1][2] != -1;
        bool r2 = t2[u2][2] != -1;
        if (r1 != r2) return false;
        
        return checkStruct(t1[u1][1], t1, t2[u2][1], t2) &&
               checkStruct(t1[u1][2], t1, t2[u2][2], t2);
    }

public:
    vector<vector<int>> traverseAll(int n, const vector<array<int, 3>>& nodes) {
        vector<vector<int>> res(3);
        if (n == 0) return res;
        dfs(0, nodes, res[0], res[1], res[2]);
        return res;
    }

    bool structuralIdentical(int n1, const vector<array<int, 3>>& t1,
                             int n2, const vector<array<int, 3>>& t2) {
        if (n1 == 0 && n2 == 0) return true;
        if (n1 == 0 || n2 == 0) return false;
        return checkStruct(0, t1, 0, t2);
    }

    vector<string> matchingTraversals(const vector<vector<int>>& t1,
                                      const vector<vector<int>>& t2) {
        vector<string> matches;
        if (t1[0] == t2[0]) matches.push_back("preorder");
        if (t1[1] == t2[1]) matches.push_back("inorder");
        if (t1[2] == t2[2]) matches.push_back("postorder");
        return matches;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n1;
    if (!(cin >> n1)) return 0;
    vector<array<int, 3>> t1(n1);
    for (int i = 0; i < n1; i++) {
        cin >> t1[i][0] >> t1[i][1] >> t1[i][2];
    }
    int n2;
    cin >> n2;
    vector<array<int, 3>> t2(n2);
    for (int i = 0; i < n2; i++) {
        cin >> t2[i][0] >> t2[i][1] >> t2[i][2];
    }

    Solution solution;
    vector<vector<int>> trav1 = solution.traverseAll(n1, t1);
    vector<vector<int>> trav2 = solution.traverseAll(n2, t2);
    bool same = solution.structuralIdentical(n1, t1, n2, t2);
    vector<string> matches = solution.matchingTraversals(trav1, trav2);

    auto printList = [](const vector<int>& v) {
        for (int i = 0; i < (int)v.size(); i++) {
            if (i) cout << ' ';
            cout << v[i];
        }
        cout << "\n";
    };

    for (int i = 0; i < 3; i++) printList(trav1[i]);
    for (int i = 0; i < 3; i++) printList(trav2[i]);
    cout << (same ? "true" : "false") << "\n";
    if (matches.empty()) {
        cout << "NONE";
    } else {
        for (int i = 0; i < (int)matches.size(); i++) {
            if (i) cout << ' ';
            cout << matches[i];
        }
    }
    return 0;
}
