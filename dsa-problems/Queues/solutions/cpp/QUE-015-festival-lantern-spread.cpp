#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int minutesToLight(vector<vector<int>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;

        int r = grid.size();
        int c = grid[0].size();
        queue<pair<int, int>> q;
        int freshCount = 0;

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[i][j] == 1) {
                    q.push({i, j});
                } else {
                    freshCount++;
                }
            }
        }

        if (freshCount == 0) return 0;
        if (q.empty()) return -1;

        int minutes = 0;
        int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while (!q.empty() && freshCount > 0) {
            minutes++;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                pair<int, int> curr = q.front();
                q.pop();

                for (auto& d : dirs) {
                    int ni = curr.first + d[0];
                    int nj = curr.second + d[1];

                    if (ni >= 0 && ni < r && nj >= 0 && nj < c && grid[ni][nj] == 0) {
                        grid[ni][nj] = 1;
                        freshCount--;
                        q.push({ni, nj});
                    }
                }
            }
        }

        return freshCount == 0 ? minutes : -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> remaining;
        int val;
        while (cin >> val) {
            remaining.push_back(val);
        }

        vector<vector<int>> grid;

        // If we have exactly n remaining values, treat as 1D grid (1 x n)
        if ((int)remaining.size() == n) {
            grid.push_back(remaining);
        } else if ((int)remaining.size() > n) {
            // Check if we have r and c explicitly
            int r = n;
            int c = remaining[0];
            if ((int)remaining.size() >= r * c) {
                grid.resize(r);
                int pos = 1;
                for (int i = 0; i < r; i++) {
                    for (int j = 0; j < c; j++) {
                        grid[i].push_back(remaining[pos++]);
                    }
                }
            } else {
                // Fallback: treat as 1D
                vector<int> row;
                for (int i = 0; i < n && i < (int)remaining.size(); i++) {
                    row.push_back(remaining[i]);
                }
                grid.push_back(row);
            }
        } else {
            // Fallback: treat as 1D
            grid.push_back(remaining);
        }

        Solution sol;
        cout << sol.minutesToLight(grid) << endl;
    }
    return 0;
}
