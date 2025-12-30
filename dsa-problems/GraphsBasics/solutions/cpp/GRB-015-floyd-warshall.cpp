#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<long long>> floydWarshall(vector<vector<long long>> dist) {
        int n = dist.size();
        long long INF = 1e15;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j && dist[i][j] == -1) {
                    dist[i][j] = INF;
                }
            }
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dist[i][k] != INF && dist[k][j] != INF) {
                        if (dist[i][k] + dist[k][j] < dist[i][j]) {
                            dist[i][j] = dist[i][k] + dist[k][j];
                        }
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (dist[i][i] < 0) return {};
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (dist[i][j] >= INF / 2) {
                    dist[i][j] = -1;
                }
            }
        }
        return dist;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<vector<long long>> dist(n, vector<long long>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> dist[i][j];
        }
    }

    Solution solution;
    vector<vector<long long>> ans = solution.floydWarshall(dist);
    if (ans.empty()) {
        cout << "NEGATIVE CYCLE";
    } else {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (j) cout << ' ';
                cout << ans[i][j];
            }
            if (i + 1 < n) cout << "\n";
        }
    }
    return 0;
}
