#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> topoSort(int n, const vector<vector<int>>& adj) {
        vector<int> indegree(n, 0);
        for (int u = 0; u < n; u++) {
            for (int v : adj[u]) {
                indegree[v]++;
            }
        }

        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }

        vector<int> result;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            result.push_back(u);

            for (int v : adj[u]) {
                indegree[v]--;
                if (indegree[v] == 0) {
                    q.push(v);
                }
            }
        }

        return result;
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
    vector<int> order = solution.topoSort(n, adj);
    for (int i = 0; i < (int)order.size(); i++) {
        if (i) cout << ' ';
        cout << order[i];
    }
    return 0;
}
