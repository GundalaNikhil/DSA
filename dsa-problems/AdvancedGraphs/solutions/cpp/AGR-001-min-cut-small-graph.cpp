#include <array>
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    long long minCut(int n, const vector<array<int, 3>>& edges) {
        vector<vector<long long>> adj(n, vector<long long>(n, 0));
        for (const auto& e : edges) {
            adj[e[0]][e[1]] += e[2];
            adj[e[1]][e[0]] += e[2];
        }

        long long globalMinCut = LLONG_MAX;
        vector<bool> merged(n, false);
        int nodesRemaining = n;

        while (nodesRemaining > 1) {
            vector<long long> weights(n, 0);
            vector<bool> inSet(n, false);
            int prev = -1, curr = -1;

            for (int step = 0; step < nodesRemaining; step++) {
                prev = curr;
                curr = -1;
                long long maxW = -1;

                for (int i = 0; i < n; i++) {
                    if (!merged[i] && !inSet[i]) {
                        if (weights[i] > maxW) {
                            maxW = weights[i];
                            curr = i;
                        }
                    }
                }

                if (curr == -1) break;
                inSet[curr] = true;

                for (int i = 0; i < n; i++) {
                    if (!merged[i] && !inSet[i]) {
                        weights[i] += adj[curr][i];
                    }
                }
            }

            globalMinCut = min(globalMinCut, weights[curr]);

            // Merge curr into prev
            for (int i = 0; i < n; i++) {
                if (i != curr && i != prev && !merged[i]) {
                    adj[prev][i] += adj[curr][i];
                    adj[i][prev] += adj[curr][i];
                }
            }
            merged[curr] = true;
            nodesRemaining--;
        }

        return globalMinCut == LLONG_MAX ? 0 : globalMinCut;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    cout << solution.minCut(n, edges) << "\n";
    return 0;
}
