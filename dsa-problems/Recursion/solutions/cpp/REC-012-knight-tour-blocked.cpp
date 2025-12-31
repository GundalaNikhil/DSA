#include <vector>
#include <utility>

using namespace std;

class Solution {
    int N;
    int moves[8][2] = {
        {-2, -1}, {-2, 1}, {-1, -2}, {-1, 2},
        {1, -2}, {1, 2}, {2, -1}, {2, 1}
    };

public:
    vector<pair<int, int>> knightTour(int n, const vector<vector<bool>>& blocked) {
        N = n;
        int totalUnblocked = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!blocked[i][j]) totalUnblocked++;
            }
        }

        vector<vector<bool>> visited(n, vector<bool>(n, false));
        vector<pair<int, int>> path;
        
        visited[0][0] = true;
        path.push_back({0, 0});
        
        if (dfs(0, 0, 1, totalUnblocked, blocked, visited, path)) {
            return path;
        }
        return {};
    }

    bool dfs(int r, int c, int count, int target, const vector<vector<bool>>& blocked, 
             vector<vector<bool>>& visited, vector<pair<int, int>>& path) {
        if (count == target) return true;

        for (auto& m : moves) {
            int nr = r + m[0];
            int nc = c + m[1];

            if (nr >= 0 && nr < N && nc >= 0 && nc < N && !blocked[nr][nc] && !visited[nr][nc]) {
                visited[nr][nc] = true;
                path.push_back({nr, nc});
                if (dfs(nr, nc, count + 1, target, blocked, visited, path)) return true;
                path.pop_back();
                visited[nr][nc] = false;
            }
        }
        return false;
    }
};
