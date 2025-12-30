#include <array>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
    struct Edge {
        int to;
        long long capacity;
        long long flow;
        int rev;
    };

    vector<vector<Edge>> adj;
    vector<int> level;
    vector<int> ptr;

    void addEdge(int from, int to, long long cap) {
        Edge a = {to, cap, 0, (int)adj[to].size()};
        Edge b = {from, 0, 0, (int)adj[from].size()};
        adj[from].push_back(a);
        adj[to].push_back(b);
    }

    bool bfs(int s, int t) {
        fill(level.begin(), level.end(), -1);
        level[s] = 0;
        queue<int> q;
        q.push(s);
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (const auto& e : adj[u]) {
                if (e.capacity - e.flow > 0 && level[e.to] == -1) {
                    level[e.to] = level[u] + 1;
                    q.push(e.to);
                }
            }
        }
        return level[t] != -1;
    }

    long long dfs(int u, int t, long long pushed) {
        if (pushed == 0) return 0;
        if (u == t) return pushed;
        for (int& cid = ptr[u]; cid < adj[u].size(); ++cid) {
            auto& e = adj[u][cid];
            if (level[u] + 1 != level[e.to] || e.capacity - e.flow == 0) continue;
            long long tr = dfs(e.to, t, min(pushed, e.capacity - e.flow));
            if (tr == 0) continue;
            e.flow += tr;
            adj[e.to][e.rev].flow -= tr;
            return tr;
        }
        return 0;
    }

public:
    long long maxFlowVertexCap(int n, int s, int t, const vector<long long>& cap,
                               const vector<array<int, 3>>& edges) {
        int numNodes = 2 * n;
        adj.assign(numNodes, vector<Edge>());
        level.resize(numNodes);
        ptr.resize(numNodes);

        long long INF = 1e15;

        for (int i = 0; i < n; i++) {
            long long c = (cap[i] == -1 || i == s || i == t) ? INF : cap[i];
            addEdge(2 * i, 2 * i + 1, c);
        }

        for (const auto& e : edges) {
            addEdge(2 * e[0] + 1, 2 * e[1], e[2]);
        }

        int sNode = 2 * s;
        int tNode = 2 * t + 1;
        long long maxFlow = 0;

        while (bfs(sNode, tNode)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(sNode, tNode, INF)) {
                maxFlow += pushed;
            }
        }

        return maxFlow;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;
    vector<long long> cap(n);
    for (int i = 0; i < n; i++) cin >> cap[i];
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    cout << solution.maxFlowVertexCap(n, s, t, cap, edges) << "\n";
    return 0;
}
