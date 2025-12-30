#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> bipartiteColors(int n, const vector<vector<int>>& adj) {
        vector<int> colors(n, -1);
        
        for (int i = 0; i < n; i++) {
            if (colors[i] == -1) {
                queue<int> q;
                q.push(i);
                colors[i] = 0;
                
                while (!q.empty()) {
                    int u = q.front();
                    q.pop();
                    
                    for (int v : adj[u]) {
                        if (colors[v] == -1) {
                            colors[v] = 1 - colors[u];
                            q.push(v);
                        } else if (colors[v] == colors[u]) {
                            return {}; // Empty vector signals false
                        }
                    }
                }
            }
        }
        return colors;
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
        adj[v].push_back(u);
    }

    Solution solution;
    vector<int> colors = solution.bipartiteColors(n, adj);
    
    if (colors.empty()) {
        cout << "false";
    } else {
        cout << "true\n";
        for (int i = 0; i < n; i++) {
            if (i) cout << ' ';
            cout << colors[i];
        }
    }
    return 0;
}
