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
    
    int r, c;
    if (cin >> r >> c) {
        vector<vector<int>> grid(r, vector<int>(c));
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) cin >> grid[i][j];
        }
        
        Solution sol;
        cout << sol.minutesToLight(grid) << endl;
    }
    return 0;
}
