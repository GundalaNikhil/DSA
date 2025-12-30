#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    vector<vector<int>> adj, revAdj;
    vector<int> order, component;
    vector<bool> visited;
    int N;

    int map(int literal) {
        if (literal > 0) return literal;
        return -literal + N;
    }

    int neg(int literal) {
        if (literal > 0) return literal + N;
        return -literal;
    }

    void addEdge(int u, int v) {
        adj[u].push_back(v);
        revAdj[v].push_back(u);
    }

    void addImplication(int a, int b) {
        // a -> b  <=>  ¬b -> ¬a
        addEdge(map(a), map(b));
        addEdge(neg(b), neg(a));
    }

    void dfs1(int u) {
        visited[u] = true;
        for (int v : adj[u]) {
            if (!visited[v]) dfs1(v);
        }
        order.push_back(u);
    }

    void dfs2(int u, int c) {
        component[u] = c;
        for (int v : revAdj[u]) {
            if (component[v] == -1) dfs2(v, c);
        }
    }

public:
    vector<int> solveTwoSat(int n, const vector<pair<int, int>>& clauses,
                            const vector<vector<int>>& groups) {
        int totalGroupSize = 0;
        for (const auto& g : groups) totalGroupSize += g.size();

        N = n + totalGroupSize;
        int totalNodes = 2 * N + 2;

        adj.assign(totalNodes, vector<int>());
        revAdj.assign(totalNodes, vector<int>());

        // Clauses
        for (const auto& p : clauses) {
            // a OR b <=> ¬a -> b
            addImplication(-p.first, p.second);
        }

        // AMO
        int currentAux = n + 1;
        for (const auto& group : groups) {
            int k = group.size();
            if (k <= 1) continue;

            for (int i = 0; i < k; i++) {
                int x = group[i];
                int p = currentAux + i;

                // x -> P_i
                addImplication(x, p);

                // P_i -> P_{i+1}
                if (i < k - 1) {
                    addImplication(p, p + 1);
                }

                // P_{i-1} -> ¬x
                if (i > 0) {
                    addImplication(p - 1, -x);
                }
            }
            currentAux += k;
        }

        // SCC
        visited.assign(totalNodes, false);
        order.clear();
        for (int i = 1; i <= 2 * N; i++) {
            if (!visited[i]) dfs1(i);
        }

        reverse(order.begin(), order.end());
        component.assign(totalNodes, -1);
        int compCount = 0;

        for (int u : order) {
            if (component[u] == -1) {
                dfs2(u, compCount++);
            }
        }

        vector<int> result;
        for (int i = 1; i <= n; i++) {
            if (component[i] == component[i + N]) return {};
            result.push_back(component[i] > component[i + N] ? 1 : 0);
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<pair<int, int>> clauses(m);
    for (int i = 0; i < m; i++) {
        cin >> clauses[i].first >> clauses[i].second;
    }
    int g;
    cin >> g;
    vector<vector<int>> groups(g);
    for (int i = 0; i < g; i++) {
        int k;
        cin >> k;
        groups[i].resize(k);
        for (int j = 0; j < k; j++) cin >> groups[i][j];
    }

    Solution solution;
    vector<int> assign = solution.solveTwoSat(n, clauses, groups);
    if (assign.empty()) {
        cout << "UNSAT";
    } else {
        cout << "SAT\n";
        for (int i = 0; i < n; i++) {
            if (i) cout << ' ';
            cout << assign[i];
        }
    }
    return 0;
}
