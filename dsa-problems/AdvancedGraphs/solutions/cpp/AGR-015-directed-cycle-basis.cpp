#include <iostream>
#include <vector>
#include <queue>
#include <bitset>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> cycleBasis(int n, const vector<pair<int, int>>& edges) {
        int m = edges.size();
        vector<vector<pair<int, int>>> adj(n);
        for (int i = 0; i < m; i++) {
            adj[edges[i].first].push_back({edges[i].second, i});
        }

        // Calc basis size
        int c = 0;
        vector<bool> visited(n, false);
        vector<vector<int>> undirAdj(n);
        for (const auto& e : edges) {
            undirAdj[e.first].push_back(e.second);
            undirAdj[e.second].push_back(e.first);
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                c++;
                queue<int> q;
                q.push(i);
                visited[i] = true;
                while (!q.empty()) {
                    int u = q.front(); q.pop();
                    for (int v : undirAdj[u]) {
                        if (!visited[v]) {
                            visited[v] = true;
                            q.push(v);
                        }
                    }
                }
            }
        }
        int D = m - n + c;

        // Basis using bitset
        // M <= 2000. bitset<2000>
        vector<bitset<2000>> basis(m);
        vector<bool> hasBasis(m, false);
        vector<vector<int>> result;

        for (int i = 0; i < m; i++) {
            if (result.size() == D) break;

            int u = edges[i].first;
            int v = edges[i].second;

            // BFS v -> u
            vector<int> parentEdge(n, -1);
            vector<int> parentNode(n, -1);
            queue<int> q;
            q.push(v);
            parentNode[v] = v;

            bool found = false;
            while (!q.empty()) {
                int curr = q.front(); q.pop();
                if (curr == u) {
                    found = true;
                    break;
                }
                for (auto& edge : adj[curr]) {
                    int next = edge.first;
                    int idx = edge.second;
                    if (parentNode[next] == -1) {
                        parentNode[next] = curr;
                        parentEdge[next] = idx;
                        q.push(next);
                    }
                }
            }

            if (!found) continue;

            bitset<2000> vec;
            vec[i] = 1;
            
            vector<int> path;
            int curr = u;
            while (curr != v) {
                int idx = parentEdge[curr];
                vec[idx] = 1;
                path.push_back(idx);
                curr = parentNode[curr];
            }
            // Path is u <- ... <- v. Reverse to get v -> ... -> u
            reverse(path.begin(), path.end());

            // Insert
            bool inserted = false;
            for (int j = 0; j < m; j++) {
                if (vec[j]) {
                    if (!hasBasis[j]) {
                        basis[j] = vec;
                        hasBasis[j] = true;
                        inserted = true;
                        break;
                    } else {
                        vec ^= basis[j];
                    }
                }
            }

            if (inserted) {
                vector<int> cycle;
                cycle.push_back(u);
                cycle.push_back(v);
                for (int idx : path) {
                    cycle.push_back(edges[idx].second);
                }
                result.push_back(cycle);
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
    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    Solution solution;
    vector<vector<int>> cycles = solution.cycleBasis(n, edges);
    cout << cycles.size() << "\n";
    for (const auto& cyc : cycles) {
        cout << cyc.size();
        for (int v : cyc) cout << ' ' << v;
        cout << "\n";
    }
    return 0;
}
