#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <array>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    long long cap;
    long long flow;
    long long cost;
    int rev;
};

class MinCostMaxFlow {
    int n;
    vector<vector<Edge>> adj;
    vector<long long> dist;
    vector<long long> h;
    vector<int> parentNode;
    vector<int> parentEdge;

public:
    MinCostMaxFlow(int n) : n(n), adj(n), dist(n), h(n), parentNode(n), parentEdge(n) {}

    void addEdge(int u, int v, long long cap, long long cost) {
        Edge a = {v, cap, 0, cost, (int)adj[v].size()};
        Edge b = {u, 0, 0, -cost, (int)adj[u].size()};
        adj[u].push_back(a);
        adj[v].push_back(b);
    }

    bool spfa(int s) {
        fill(h.begin(), h.end(), INF);
        h[s] = 0;
        vector<bool> inQueue(n, false);
        queue<int> q;
        q.push(s);
        inQueue[s] = true;

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            inQueue[u] = false;
            for (const auto& e : adj[u]) {
                if (e.cap - e.flow > 0 && h[e.to] > h[u] + e.cost) {
                    h[e.to] = h[u] + e.cost;
                    if (!inQueue[e.to]) {
                        q.push(e.to);
                        inQueue[e.to] = true;
                    }
                }
            }
        }
        return h[s] != INF; // Should check if any reachable
    }

    bool dijkstra(int s, int t) {
        fill(dist.begin(), dist.end(), INF);
        dist[s] = 0;
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        pq.push({0, s});

        while (!pq.empty()) {
            long long d = pq.top().first;
            int u = pq.top().second;
            pq.pop();

            if (d > dist[u]) continue;

            for (int i = 0; i < adj[u].size(); ++i) {
                const auto& e = adj[u][i];
                long long reducedCost = e.cost + h[u] - h[e.to];
                if (e.cap - e.flow > 0 && dist[e.to] > dist[u] + reducedCost) {
                    dist[e.to] = dist[u] + reducedCost;
                    parentNode[e.to] = u;
                    parentEdge[e.to] = i;
                    pq.push({dist[e.to], e.to});
                }
            }
        }
        return dist[t] != INF;
    }

    pair<long long, long long> solve(int s, int t) {
        long long flow = 0;
        long long cost = 0;
        spfa(s); // Init potentials

        while (dijkstra(s, t)) {
            for (int i = 0; i < n; ++i) {
                if (dist[i] != INF) h[i] += dist[i];
            }

            long long push = INF;
            int curr = t;
            while (curr != s) {
                int p = parentNode[curr];
                int idx = parentEdge[curr];
                push = min(push, adj[p][idx].cap - adj[p][idx].flow);
                curr = p;
            }

            flow += push;
            curr = t;
            while (curr != s) {
                int p = parentNode[curr];
                int idx = parentEdge[curr];
                adj[p][idx].flow += push;
                int revIdx = adj[p][idx].rev;
                adj[curr][revIdx].flow -= push;
                cost += push * adj[p][idx].cost;
                curr = p;
            }
        }
        return {flow, cost};
    }
};

class Solution {
public:
    bool minCostFlow(int n, const vector<long long>& b, const vector<array<int, 5>>& edges, long long& costOut) {
        long long baseCost = 0;
        vector<long long> supply = b;
        int S = n;
        int T = n + 1;
        MinCostMaxFlow mcmf(n + 2);

        for (const auto& e : edges) {
            int u = e[0];
            int v = e[1];
            int low = e[2];
            int high = e[3];
            int cost = e[4];

            if (high < low) return false;

            baseCost += (long long)low * cost;
            supply[u] -= low;
            supply[v] += low;
            mcmf.addEdge(u, v, high - low, cost);
        }

        long long totalSupply = 0;
        for (int i = 0; i < n; i++) {
            if (supply[i] > 0) {
                mcmf.addEdge(S, i, supply[i], 0);
                totalSupply += supply[i];
            } else if (supply[i] < 0) {
                mcmf.addEdge(i, T, -supply[i], 0);
            }
        }

        pair<long long, long long> res = mcmf.solve(S, T);
        if (res.first != totalSupply) return false;

        costOut = baseCost + res.second;
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> b(n);
    for (int i = 0; i < n; i++) cin >> b[i];
    vector<array<int, 5>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2] >> edges[i][3] >> edges[i][4];
    }

    Solution solution;
    long long cost = 0;
    bool ok = solution.minCostFlow(n, b, edges, cost);
    if (!ok) {
        cout << "INFEASIBLE";
    } else {
        cout << "FEASIBLE\n" << cost;
    }
    return 0;
}
