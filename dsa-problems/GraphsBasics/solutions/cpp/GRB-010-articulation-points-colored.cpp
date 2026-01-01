#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

class Solution {
public:
    vector<int> criticalNodes(int n, const vector<array<int, 3>>& edges) {
        // Build adjacency list with colors
        vector<vector<pair<int, int>>> adj(n); // adj[u] = [(v, color), ...]
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }
        
        vector<int> critNodes;
        
        // Brute force: try removing each node
        for (int removed = 0; removed < n; removed++) {
            vector<bool> visited(n, false);
            visited[removed] = true;
            
            vector<pair<bool, bool>> components; // (hasRed, hasBlue)
            
            for (int start = 0; start < n; start++) {
                if (!visited[start]) {
                    bool hasRed = false;
                    bool hasBlue = false;
                    
                    vector<int> compNodes;
                    vector<int> stack;
                    stack.push_back(start);
                    visited[start] = true;
                    
                    while (!stack.empty()) {
                        int u = stack.back();
                        stack.pop_back();
                        compNodes.push_back(u);
                        for (auto& [v, c] : adj[u]) {
                            if (v == removed) continue;
                            if (!visited[v]) {
                                visited[v] = true;
                                stack.push_back(v);
                            }
                        }
                    }
                    
                    // Check edges within this component
                    set<int> compSet(compNodes.begin(), compNodes.end());
                    for (int u : compNodes) {
                        for (auto& [v, color] : adj[u]) {
                            if (v == removed) continue;
                            if (compSet.count(v)) {
                                if (color == 0) hasRed = true;
                                else hasBlue = true;
                            }
                        }
                    }
                    
                    components.push_back({hasRed, hasBlue});
                }
            }
            
            // Check criticality condition
            vector<int> redComps, blueComps;
            for (int i = 0; i < (int)components.size(); i++) {
                if (components[i].first) redComps.push_back(i);
                if (components[i].second) blueComps.push_back(i);
            }
            
            bool isCritical = false;
            if (!redComps.empty() && !blueComps.empty()) {
                if (redComps.size() > 1 || blueComps.size() > 1) {
                    isCritical = true;
                } else if (redComps[0] != blueComps[0]) {
                    isCritical = true;
                }
            }
            
            if (isCritical) {
                critNodes.push_back(removed);
            }
        }
        
        return critNodes;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<array<int, 3>> edges;
    edges.reserve(m);
    for (int i = 0; i < m; i++) {
        int u, v; char c;
        cin >> u >> v >> c;
        edges.push_back({u, v, c == 'R' ? 0 : 1});
    }

    Solution solution;
    vector<int> ans = solution.criticalNodes(n, edges);
    // Output count and node IDs (as per problem statement)
    cout << ans.size() << "\n";
    for (int i = 0; i < (int)ans.size(); i++) {
        if (i) cout << ' ';
        cout << ans[i];
    }
    cout << "\n";
    return 0;
}
