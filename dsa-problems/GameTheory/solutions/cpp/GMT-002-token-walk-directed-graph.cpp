#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
    vector<vector<int>> adj;
    vector<int> memo; // -1: unknown, 0: Losing, 1: Winning

    bool dfs(int u) {
        if (memo[u] != -1) return memo[u] == 1;

        bool canReachLosing = false;
        for (int v : adj[u]) {
            if (!dfs(v)) {
                canReachLosing = true;
                break;
            }
        }

        memo[u] = canReachLosing ? 1 : 0;
        return canReachLosing;
    }

public:
    vector<string> determineWinningNodes(int n, vector<vector<int>>& edges) {
        adj.assign(n, vector<int>());
        for (const auto& e : edges) {
            adj[e[0]].push_back(e[1]);
        }

        memo.assign(n, -1);
        vector<string> result;
        for (int i = 0; i < n; i++) {
            if (dfs(i)) result.push_back("Winning");
            else result.push_back("Losing");
        }
        return result;
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
        vector<string> result = solution.determineWinningNodes(n, edges);
        
        for (int i = 0; i < result.size(); i++) {
            cout << result[i] << (i == result.size() - 1 ? "" : " ");
        }
        cout << "\n";
    }
    return 0;
}
