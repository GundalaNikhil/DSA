#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <map>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    int weight;
};

struct Path {
    vector<int> nodes;
    long long cost;

    bool operator<(const Path& other) const {
        if (cost != other.cost) return cost < other.cost;
        return nodes < other.nodes;
    }
    bool operator>(const Path& other) const {
        return other < *this;
    }
    bool operator==(const Path& other) const {
        return cost == other.cost && nodes == other.nodes;
    }
};

class Solution {
    vector<vector<Edge>> adj;
    int N;

    Path getShortestPath(int s, int t, const set<int>& forbiddenNodes, const set<pair<int, int>>& forbiddenEdges) {
        vector<long long> dist(N, INF);
        vector<int> parent(N, -1);
        dist[s] = 0;

        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        pq.push({0, s});

        while (!pq.empty()) {
            long long d = pq.top().first;
            int u = pq.top().second;
            pq.pop();

            if (d > dist[u]) continue;
            if (u == t) break;

            for (const auto& e : adj[u]) {
                if (forbiddenNodes.count(e.to)) continue;
                if (forbiddenEdges.count({u, e.to})) continue;

                if (dist[u] + e.weight < dist[e.to]) {
                    dist[e.to] = dist[u] + e.weight;
                    parent[e.to] = u;
                    pq.push({dist[e.to], e.to});
                }
            }
        }

        if (dist[t] == INF) return {{}, -1};

        vector<int> nodes;
        int curr = t;
        while (curr != -1) {
            nodes.push_back(curr);
            curr = parent[curr];
        }
        reverse(nodes.begin(), nodes.end());
        return {nodes, dist[t]};
    }

public:
    vector<long long> kShortestPaths(int n, const vector<vector<pair<int, int>>>& adjList, int s, int t, int k) {
        N = n;
        adj.assign(n, vector<Edge>());
        for (int u = 0; u < n; u++) {
            for (auto& p : adjList[u]) {
                adj[u].push_back({p.first, p.second});
            }
        }

        vector<Path> A;
        set<Path> B; // Use set to keep sorted and unique candidates

        Path p0 = getShortestPath(s, t, {}, {});
        if (p0.cost == -1) return {};
        A.push_back(p0);

        for (int i = 1; i < k; i++) {
            Path prevPath = A.back();

            for (size_t j = 0; j < prevPath.nodes.size() - 1; j++) {
                int spurNode = prevPath.nodes[j];
                vector<int> rootPathNodes(prevPath.nodes.begin(), prevPath.nodes.begin() + j + 1);
                
                long long rootCost = 0;
                for (size_t x = 0; x < j; x++) {
                    int u = prevPath.nodes[x];
                    int v = prevPath.nodes[x+1];
                    for (auto& e : adj[u]) if (e.to == v) { rootCost += e.weight; break; }
                }

                set<int> forbiddenNodes(rootPathNodes.begin(), rootPathNodes.end());
                forbiddenNodes.erase(spurNode);

                set<pair<int, int>> forbiddenEdges;
                for (const auto& p : A) {
                    if (p.nodes.size() > j && 
                        vector<int>(p.nodes.begin(), p.nodes.begin() + j + 1) == rootPathNodes) {
                        forbiddenEdges.insert({p.nodes[j], p.nodes[j+1]});
                    }
                }

                Path spurPath = getShortestPath(spurNode, t, forbiddenNodes, forbiddenEdges);

                if (spurPath.cost != -1) {
                    vector<int> totalNodes = rootPathNodes;
                    totalNodes.pop_back();
                    totalNodes.insert(totalNodes.end(), spurPath.nodes.begin(), spurPath.nodes.end());
                    
                    Path totalPath = {totalNodes, rootCost + spurPath.cost};
                    B.insert(totalPath);
                }
            }

            if (B.empty()) break;
            
            // Move best from B to A
            // Since B is a set, begin() is the smallest
            A.push_back(*B.begin());
            B.erase(B.begin());
        }

        vector<long long> result;
        for (const auto& p : A) result.push_back(p.cost);
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t, k;
    if (!(cin >> n >> m >> s >> t >> k)) return 0;
    vector<vector<pair<int, int>>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }

    Solution solution;
    vector<long long> paths = solution.kShortestPaths(n, adj, s, t, k);
    cout << paths.size() << "\n";
    for (int i = 0; i < (int)paths.size(); i++) {
        if (i) cout << ' ';
        cout << paths[i];
    }
    return 0;
}
