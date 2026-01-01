#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <tuple>
#include <string>
using namespace std;

class Solution {
private:
    int dirs[4][2] = {{0,1}, {1,0}, {0,-1}, {-1,0}};

public:
    int shortestPathWithFood(vector<vector<char>>& grid) {
        int rows = grid.size();
        if (rows == 0) return -1;
        int cols = grid[0].size();

        int startR = -1, startC = -1;

        // Find starting position
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 'S') {
                    startR = i;
                    startC = j;
                    break;
                }
            }
            if (startR != -1) break;
        }

        if (startR == -1) return -1;

        // State: (r, c, has_food, steps)
        queue<tuple<int,int,int,int>> q;
        set<tuple<int,int,int>> visited;

        q.push({startR, startC, 0, 0});
        visited.insert({startR, startC, 0});

        while (!q.empty()) {
            auto [r, c, hasFood, steps] = q.front();
            q.pop();

            int currentFood = hasFood;
            if (grid[r][c] == 'F') {
                currentFood = 1;
            }

            if (grid[r][c] == 'E' && currentFood) {
                return steps;
            }

            for (auto& dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];

                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
                if (grid[nr][nc] == '#') continue;

                if (visited.find({nr, nc, currentFood}) == visited.end()) {
                    visited.insert({nr, nc, currentFood});
                    q.push({nr, nc, currentFood, steps + 1});
                }
            }
        }

        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int r, c;
    cin >> r >> c;

    vector<vector<char>> grid(r, vector<char>(c));
    for (int i = 0; i < r; i++) {
        string line;
        cin >> line;
        for (int j = 0; j < c && j < line.length(); j++) {
            grid[i][j] = line[j];
        }
    }

    Solution solution;
    cout << solution.shortestPathWithFood(grid) << endl;

    return 0;
}
