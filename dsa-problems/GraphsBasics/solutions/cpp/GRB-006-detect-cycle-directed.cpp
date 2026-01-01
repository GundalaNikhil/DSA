#include <iostream>
#include <vector>

using namespace std;

class Solution {
    bool dfs(int u, const vector<vector<int>>& adj, vector<int>& state) {
        state[u] = 1; // Visiting
        for (int v : adj[u]) {
            if (state[v] == 1) return true;
            if (state[v] == 0) {
                if (dfs(v, adj, state)) return true;
            }
        }
        state[u] = 2; // Visited
        return false;
    }

public:
    bool hasCycle(int n, const vector<vector<int>>& adj) {
        vector<int> state(n, 0);
        for (int i = 0; i < n; i++) {
            if (state[i] == 0) {
                if (dfs(i, adj, state)) return true;
            }
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
    }

    Solution solution;
    cout << (solution.hasCycle(n, adj) ? "1" : "0");
    return 0;
}
