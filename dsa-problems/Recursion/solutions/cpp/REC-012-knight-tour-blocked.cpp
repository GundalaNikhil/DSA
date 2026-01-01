#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    int N;
    int total_unblocked;
    vector<vector<bool>> blocked;
    vector<vector<bool>> visited;
    int dr[8] = {-2, -2, -1, -1, 1, 1, 2, 2};
    int dc[8] = {-1, 1, -2, 2, -2, 2, -1, 1};

public:
    bool knightTour(int n, const vector<vector<bool>>& blk) {
        N = n;
        blocked = blk;
        total_unblocked = 0;
        for(int i=0; i<n; i++) 
            for(int j=0; j<n; j++) 
                if(!blocked[i][j]) total_unblocked++;
        
        if(total_unblocked == 0) return true; // Should not happen if start is 0,0
        if(blocked[0][0]) return false;
        if(total_unblocked == 1) return true; // Just start cell

        visited.assign(n, vector<bool>(n, false));
        visited[0][0] = true;
        return dfs(0, 0, 1);
    }

    int countOnward(int r, int c) {
        int cnt = 0;
        for(int i=0; i<8; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if(nr >= 0 && nr < N && nc >= 0 && nc < N && !blocked[nr][nc] && !visited[nr][nc]) {
                cnt++;
            }
        }
        return cnt;
    }

    bool dfs(int r, int c, int count) {
        if (count == total_unblocked) return true;

        vector<pair<int, int>> moves; // priority, index in dr/dc
        for(int i=0; i<8; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if(nr >= 0 && nr < N && nc >= 0 && nc < N && !blocked[nr][nc] && !visited[nr][nc]) {
                moves.push_back({countOnward(nr, nc), i});
            }
        }
        
        if(moves.empty()) return false;
        
        sort(moves.begin(), moves.end());

        for(auto p : moves) {
            int i = p.second;
            int nr = r + dr[i];
            int nc = c + dc[i];
            
            visited[nr][nc] = true;
            if(dfs(nr, nc, count + 1)) return true;
            visited[nr][nc] = false;
        }
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, b;
    if (!(cin >> n >> b)) return 0;
    
    vector<vector<bool>> blocked(n, vector<bool>(n, false));
    for(int i=0; i<b; i++) {
        int r, c;
        cin >> r >> c;
        if(r >= 0 && r < n && c >= 0 && c < n) blocked[r][c] = true;
    }
    
    Solution sol;
    if(sol.knightTour(n, blocked)) cout << "YES" << endl;
    else cout << "NO" << endl;
    return 0;
}
