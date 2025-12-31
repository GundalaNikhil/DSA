#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
    vector<int> adjMask;
    vector<int> memo; // -1: unknown, 0: Losing, 1: Winning

    bool canWin(int mask, int n) {
        if (mask == 0) return false;
        if (memo[mask] != -1) return memo[mask] == 1;

        bool canReachLosing = false;
        for (int u = 0; u < n; u++) {
            if ((mask >> u) & 1) {
                int removeMask = (1 << u) | adjMask[u];
                int nextMask = mask & ~removeMask;
                if (!canWin(nextMask, n)) {
                    canReachLosing = true;
                    break;
                }
            }
        }

        memo[mask] = canReachLosing ? 1 : 0;
        return canReachLosing;
    }

public:
    string kaylesOnGraph(int n, vector<vector<int>>& edges) {
        adjMask.assign(n, 0);
        for (const auto& e : edges) {
            adjMask[e[0]] |= (1 << e[1]);
            adjMask[e[1]] |= (1 << e[0]);
        }

        memo.assign(1 << n, -1);
        return canWin((1 << n) - 1, n) ? "First" : "Second";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    if (cin >> n >> m) {
        vector<vector<int>> edges(m, vector<int>(2));
        for (int i = 0; i < m; i++) {
            cin >> edges[i][0] >> edges[i][1];
        }
        
        Solution solution;
        cout << solution.kaylesOnGraph(n, edges) << "\n";
    }
    return 0;
}
