#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int lcaBlocked(int n, const vector<int>& values, const vector<int>& blocked,
                   const vector<int>& left, const vector<int>& right, int u, int v) {
        vector<int> parent(n, -1);
        
        // 1. Build Parent Map
        queue<int> q;
        q.push(0);
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            if (left[curr] != -1) {
                parent[left[curr]] = curr;
                q.push(left[curr]);
            }
            if (right[curr] != -1) {
                parent[right[curr]] = curr;
                q.push(right[curr]);
            }
        }
        
        // 2. Find Standard LCA
        unordered_set<int> ancestors;
        int curr = u;
        while (curr != -1) {
            ancestors.insert(curr);
            curr = parent[curr];
        }
        
        int lca = -1;
        curr = v;
        while (curr != -1) {
            if (ancestors.count(curr)) {
                lca = curr;
                break;
            }
            curr = parent[curr];
        }
        
        if (lca == -1) return -1;
        
        // 3. Climb up
        while (lca != -1 && blocked[lca] == 1) {
            lca = parent[lca];
        }
        
        return (lca != -1) ? values[lca] : -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> values(n), blocked(n), left(n), right(n);
    for (int i = 0; i < n; i++) {
        cin >> values[i] >> blocked[i] >> left[i] >> right[i];
    }
    int u, v;
    cin >> u >> v;

    Solution solution;
    cout << solution.lcaBlocked(n, values, blocked, left, right, u, v) << "\n";
    return 0;
}
