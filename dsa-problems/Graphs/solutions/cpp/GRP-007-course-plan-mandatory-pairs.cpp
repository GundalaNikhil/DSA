#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
private:
    vector<int> parent;

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    void unionNodes(int x, int y) {
        int px = find(x);
        int py = find(y);
        if (px != py) {
            parent[px] = py;
        }
    }

public:
    vector<int> courseSchedule(int n, vector<pair<int,int>>& prerequisites, vector<pair<int,int>>& pairs) {
        parent.resize(n);
        for (int i = 0; i < n; i++) parent[i] = i;

        // Union pairs
        for (auto& [a, b] : pairs) {
            unionNodes(a, b);
        }

        // Build contracted graph
        unordered_map<int, vector<int>> contracted;
        unordered_map<int, int> inDegree;
        unordered_set<int> rootSet;

        for (int i = 0; i < n; i++) {
            rootSet.insert(find(i));
        }

        // Sort roots for deterministic behavior
        vector<int> roots(rootSet.begin(), rootSet.end());
        sort(roots.begin(), roots.end());

        for (int root : roots) {
            inDegree[root] = 0;
        }

        for (auto& [u, v] : prerequisites) {
            int from = find(u);
            int to = find(v);
            if (from != to) {
                contracted[from].push_back(to);
                inDegree[to]++;
            }
        }

        // Topological sort with sorted neighbors
        queue<int> q;
        for (int root : roots) {
            if (inDegree[root] == 0) {
                q.push(root);
            }
        }

        vector<int> topoOrder;
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            topoOrder.push_back(node);

            // Sort neighbors for deterministic processing
            vector<int> neighbors = contracted[node];
            sort(neighbors.begin(), neighbors.end());
            for (int neighbor : neighbors) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }

        if (topoOrder.size() != roots.size()) {
            return {}; // Cycle detected
        }

        // Expand super-nodes
        vector<int> result;
        for (int superNode : topoOrder) {
            vector<int> members;
            for (int i = 0; i < n; i++) {
                if (find(i) == superNode) {
                    members.push_back(i);
                }
            }
            sort(members.begin(), members.end());
            for (int member : members) {
                result.push_back(member);
            }
        }

        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<pair<int,int>> prerequisites;
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        prerequisites.push_back({u, v});
    }

    int p = 0;
    cin >> p;
    vector<pair<int,int>> pairs;
    for (int i = 0; i < p; i++) {
        int a, b;
        cin >> a >> b;
        pairs.push_back({a, b});
    }

    Solution solution;
    vector<int> result = solution.courseSchedule(n, prerequisites, pairs);

    if (result.empty()) {
        cout << -1 << endl;
    } else {
        for (int i = 0; i < result.size(); i++) {
            cout << result[i];
            if (i < result.size() - 1) cout << " ";
        }
        cout << endl;
    }

    return 0;
}
