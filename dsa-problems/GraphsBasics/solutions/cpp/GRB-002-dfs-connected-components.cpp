#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> components(int n, const vector<vector<int>>& adj) {
        vector<int> comp(n, 0);
        int count = 0;
        vector<int> stack;
        stack.reserve(n);

        for (int i = 0; i < n; i++) {
            if (comp[i] != 0) continue;
            count++;
            stack.clear();
            stack.push_back(i);
            comp[i] = count;
            while (!stack.empty()) {
                int u = stack.back();
                stack.pop_back();
                for (int v : adj[u]) {
                    if (comp[v] == 0) {
                        comp[v] = count;
                        stack.push_back(v);
                    }
                }
            }
        }
        return comp;
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
    vector<int> comp = solution.components(n, adj);
    int maxComp = 0;
    for (int id : comp) maxComp = max(maxComp, id);
    cout << maxComp << "\n";
    return 0;
}
