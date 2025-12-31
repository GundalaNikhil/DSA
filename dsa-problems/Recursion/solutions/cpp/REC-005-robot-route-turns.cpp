#include <vector>
#include <utility>

using namespace std;

class Solution {
    int rows, cols;
    int dr[4] = {-1, 1, 0, 0};
    int dc[4] = {0, 0, -1, 1};
    vector<pair<int, int>> path;
    vector<vector<bool>> visited;

public:
    vector<pair<int, int>> findPath(const vector<vector<int>>& grid, int T) {
        rows = grid.size();
        cols = grid[0].size();
        visited.assign(rows, vector<bool>(cols, false));
        path.clear();
        
        path.push_back({0, 0});
        visited[0][0] = true;
        
        if (dfs(0, 0, -1, 0, T, grid)) {
            return path;
        }
        return {};
    }

    bool dfs(int r, int c, int lastDir, int turns, int maxTurns, const vector<vector<int>>& grid) {
        if (r == rows - 1 && c == cols - 1) return true;

        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !visited[nr][nc] && grid[nr][nc] == 0) {
                int newTurns = turns;
                if (lastDir != -1 && i != lastDir) newTurns++;

                if (newTurns <= maxTurns) {
                    visited[nr][nc] = true;
                    path.push_back({nr, nc});
                    if (dfs(nr, nc, i, newTurns, maxTurns, grid)) return true;
                    path.pop_back();
                    visited[nr][nc] = false;
                }
            }
        }
        return false;
    }
};
