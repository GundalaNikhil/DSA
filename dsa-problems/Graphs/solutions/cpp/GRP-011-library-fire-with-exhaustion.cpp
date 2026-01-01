#include <iostream>
#include <vector>
#include <queue>
#include <set>
using namespace std;

class Solution {
private:
    int dirs[4][2] = {{0,1}, {1,0}, {0,-1}, {-1,0}};

public:
    int fireSpreadTime(vector<vector<int>>& grid, vector<vector<int>>& stamina) {
        int rows = grid.size();
        int cols = grid[0].size();
        queue<tuple<int,int,int,int>> q;  // row, col, stamina, time
        set<pair<int,int>> ignited;

        // Initialize with fire sources
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 2) {
                    q.push({i, j, stamina[i][j], 0});
                    ignited.insert({i, j});
                }
            }
        }

        int maxTime = 0;

        while (!q.empty()) {
            auto [r, c, stam, time] = q.front();
            q.pop();
            maxTime = max(maxTime, time);

            if (stam > 0) {
                for (auto& dir : dirs) {
                    int nr = r + dir[0];
                    int nc = c + dir[1];

                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols &&
                        grid[nr][nc] == 0 && ignited.find({nr, nc}) == ignited.end()) {
                        ignited.insert({nr, nc});
                        q.push({nr, nc, stam - 1, time + 1});
                    }
                }
            }
        }

        // Check if all empty cells ignited
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 0 && ignited.find({i, j}) == ignited.end()) {
                    return -1;
                }
            }
        }

        return maxTime;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int r, c;
    cin >> r >> c;

    vector<vector<int>> grid(r, vector<int>(c));
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> grid[i][j];
        }
    }

    vector<vector<int>> stamina(r, vector<int>(c, 0));
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            if (cin.peek() != EOF) {
                cin >> stamina[i][j];
            }
        }
    }

    Solution solution;
    cout << solution.fireSpreadTime(grid, stamina) << endl;

    return 0;
}
