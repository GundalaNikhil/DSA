#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

class Solution {
    vector<vector<int>> adj;
    vector<int> trail;

    void dfs(int u) {
        while (!adj[u].empty()) {
            int v = adj[u].back();
            adj[u].pop_back();
            dfs(v);
        }
        trail.push_back(u);
    }

public:
    vector<int> eulerTrail(int n, const vector<pair<int, int>>& edges) {
        int m = edges.size();
        if (m == 0) return {0};

        vector<int> in(n, 0), out(n, 0);
        adj.assign(n, vector<int>());

        for (const auto& e : edges) {
            out[e.first]++;
            in[e.second]++;
            adj[e.first].push_back(e.second);
        }

        int startNode = -1;
        int endNode = -1;
        int diffCount = 0;

        for (int i = 0; i < n; i++) {
            if (out[i] == in[i] + 1) {
                if (startNode != -1) return {};
                startNode = i;
                diffCount++;
            } else if (in[i] == out[i] + 1) {
                if (endNode != -1) return {};
                endNode = i;
                diffCount++;
            } else if (in[i] != out[i]) {
                return {};
            }
        }

        if (diffCount == 0) {
            for (int i = 0; i < n; i++) {
                if (out[i] > 0) {
                    startNode = i;
                    break;
                }
            }
        } else if (diffCount != 2) {
            return {};
        }

        if (startNode == -1) return {};

        dfs(startNode);

        if (trail.size() != m + 1) return {};

        reverse(trail.begin(), trail.end());
        return trail;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    Solution solution;
    vector<int> trail = solution.eulerTrail(n, edges);
    if (trail.empty()) {
        cout << "NO";
    } else {
        cout << "YES\n";
        for (int i = 0; i < (int)trail.size(); i++) {
            if (i) cout << ' ';
            cout << trail[i];
        }
    }
    return 0;
}
