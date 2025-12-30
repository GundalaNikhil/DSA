#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    vector<vector<int>> adj;
    vector<int> height, diam;
    vector<int> upHeight, upDiam;
    int maxDiam = 0;

    void dfs1(int u, int p) {
        int maxH1 = -1, maxH2 = -1;
        int maxD = 0;

        for (int v : adj[u]) {
            if (v == p) continue;
            dfs1(v, u);
            maxD = max(maxD, diam[v]);
            if (height[v] > maxH1) {
                maxH2 = maxH1;
                maxH1 = height[v];
            } else if (height[v] > maxH2) {
                maxH2 = height[v];
            }
        }

        height[u] = 1 + maxH1;
        diam[u] = max(maxD, (maxH1 + 1) + (maxH2 + 1));
    }

    void dfs2(int u, int p) {
        if (p != -1) {
            maxDiam = max(maxDiam, max(diam[u], upDiam[u]));
        }

        // Collect arms: {len, diam}
        // Up arm
        vector<pair<int, int>> arms;
        if (p != -1) arms.push_back({upHeight[u], upDiam[u]});
        else arms.push_back({-1, 0}); // Dummy

        for (int v : adj[u]) {
            if (v != p) arms.push_back({height[v] + 1, diam[v]});
        }

        // We need top 3 lengths and top 2 diams
        // Partial sort is efficient
        vector<int> lens, diams;
        for(auto& p : arms) {
            lens.push_back(p.first);
            diams.push_back(p.second);
        }
        
        // Sort descending
        sort(lens.rbegin(), lens.rend());
        sort(diams.rbegin(), diams.rend());
        
        // Pad
        while(lens.size() < 3) lens.push_back(-1);
        while(diams.size() < 2) diams.push_back(0);

        for (int v : adj[u]) {
            if (v == p) continue;
            
            int vLen = height[v] + 1;
            int vDiam = diam[v];

            // Exclude vLen from lens
            int bestLen = (lens[0] == vLen) ? lens[1] : lens[0];
            // Handle duplicates correctly:
            // If lens[0] == vLen, we use lens[1].
            // If lens[0] != vLen, we use lens[0].
            // BUT if lens has {5, 5, 4} and vLen is 5.
            // lens[0] is 5. We skip it. lens[1] is 5. So best is 5. Correct.
            
            upHeight[v] = 1 + bestLen;

            // Exclude vDiam from diams
            int bestDiam = (diams[0] == vDiam) ? diams[1] : diams[0];
            // Duplicate logic: {10, 10}. vDiam=10. Skip first, take second. Correct.
            // Yes, if unique. If duplicate, doesn't matter.
            // If vDiam is 5, and top are {10, 8}.
            // diams[0] != vDiam. best = 10. Correct.
            // If vDiam is 10, and top are {10, 8}.
            // diams[0] == vDiam. best = 8. Correct.
            // If vDiam is 10, and top are {10, 10}.
            // diams[0] == vDiam. best = 10. Correct.
            
            // Path through u
            int path = 0;
            // Sum of top 2 lengths excluding vLen
            if (lens[0] == vLen) {
                path = lens[1] + lens[2];
            } else if (lens[1] == vLen) {
                path = lens[0] + lens[2];
            } else {
                path = lens[0] + lens[1];
            }
            
            upDiam[v] = max(bestDiam, path);
            
            dfs2(v, u);
        }
    }

public:
    int maxDiameterAfterRemoval(int n, const vector<pair<int, int>>& edges) {
        adj.assign(n, vector<int>());
        for (const auto& e : edges) {
            adj[e.first].push_back(e.second);
            adj[e.second].push_back(e.first);
        }

        height.assign(n, 0);
        diam.assign(n, 0);
        upHeight.assign(n, 0);
        upDiam.assign(n, 0);

        dfs1(0, -1);
        dfs2(0, -1);

        return maxDiam;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<pair<int, int>> edges(n - 1);
    for (int i = 0; i < n - 1; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    Solution solution;
    cout << solution.maxDiameterAfterRemoval(n, edges) << "\n";
    return 0;
}
