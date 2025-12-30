#include <iostream>
#include <vector>

using namespace std;

class Solution {
    vector<vector<int>> adj;
    vector<vector<int>> memo; // 0: unknown, 1: losing, 2: winning

    bool canWin(int u, int v) {
        if (memo[u][v] != 0) return memo[u][v] == 2;

        bool canReachLosing = false;

        // Try moving u
        for (int nextU : adj[u]) {
            if (nextU == v) continue;
            if (!canWin(nextU, v)) {
                canReachLosing = true;
                break;
            }
        }

        // Try moving v
        if (!canReachLosing) {
            for (int nextV : adj[v]) {
                if (nextV == u) continue;
                if (!canWin(u, nextV)) {
                    canReachLosing = true;
                    break;
                }
            }
        }

        memo[u][v] = canReachLosing ? 2 : 1;
        return canReachLosing;
    }

public:
    string blockingTokens(int n, vector<vector<int>>& edges, int u, int v) {
        adj.assign(n + 1, vector<int>());
        for (const auto& e : edges) {
            adj[e[0]].push_back(e[1]);
        }

        memo.assign(n + 1, vector<int>(n + 1, 0));
        return canWin(u, v) ? "First" : "Second";
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
        int u, v;
        cin >> u >> v;
        
        Solution solution;
        cout << solution.blockingTokens(n, edges, u, v) << "\n";
    }
    return 0;
}
